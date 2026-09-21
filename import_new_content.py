"""Importa o conteudo versionado de forma incremental, idempotente e resiliente.

Usado automaticamente no deploy (CMD do Dockerfile) para puxar artigos novos
para o EasyPanel sem conflitar com o que ja existe no banco.

Recursos:
- Ordenação topológica estrita (User -> Category -> Product -> Guide -> GuideItem -> Review -> Comparison)
- Mapeamento e resolução de ForeignKeys por PK e fallback por Slug/Nome
- Verificação de existência por PK e Slug
- Suporte a multi-pass para resolver dependências cruzadas
- Preservação de categorias presentes no fixture
- Reset de sequences no PostgreSQL
"""

import json
import os
import shutil
import sys
import django

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.conf import settings
from django.contrib.auth.models import User
from django.db import transaction, connection
from django.db.models import ForeignKey
from reviews import models as reviews_models

BACKUP_DIR = os.path.join(os.getcwd(), 'content_backup')
FIXTURE = os.path.join(BACKUP_DIR, 'fixture.json')
MEDIA_BACKUP = os.path.join(BACKUP_DIR, 'media')

MODELS = {
    'auth.user': User,
    'reviews.category': reviews_models.Category,
    'reviews.tag': reviews_models.Tag,
    'reviews.product': reviews_models.Product,
    'reviews.guide': reviews_models.Guide,
    'reviews.guideitem': reviews_models.GuideItem,
    'reviews.review': reviews_models.Review,
    'reviews.reviewimage': reviews_models.ReviewImage,
    'reviews.comparison': reviews_models.Comparison,
}

MODEL_ORDER = [
    'auth.user',
    'reviews.category',
    'reviews.tag',
    'reviews.product',
    'reviews.guide',
    'reviews.guideitem',
    'reviews.review',
    'reviews.reviewimage',
    'reviews.comparison',
]

M2M_FIELDS = {'reviews.review': 'tags', 'reviews.comparison': 'tags'}


def restore_media():
    if not os.path.isdir(MEDIA_BACKUP):
        print('   (sem pasta media no backup)')
        return
    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
    shutil.copytree(MEDIA_BACKUP, settings.MEDIA_ROOT, dirs_exist_ok=True)
    print(f'   OK -> {settings.MEDIA_ROOT}')


def entry_exists(model_name, entry):
    if entry['model'] == 'auth.user':
        return User.objects.filter(username=entry['fields']['username']).exists()

    model_cls = MODELS[model_name]
    # Se possui slug, verifica primeiro por slug
    if 'slug' in entry['fields']:
        if model_cls.objects.filter(slug=entry['fields']['slug']).exists():
            return True

    # Para guideitem, verifica por guide_id e position
    if model_name == 'reviews.guideitem':
        guide_val = entry['fields'].get('guide')
        pos = entry['fields'].get('position')
        if guide_val and pos:
            if model_cls.objects.filter(guide_id=guide_val, position=pos).exists():
                return True

    pk = entry.get('pk')
    if pk is not None:
        return model_cls.objects.filter(pk=pk).exists()
    return False


def create_entry(model_name, entry, fixture_pk_map=None):
    model_cls = MODELS[model_name]
    fields = dict(entry['fields'])

    if model_name == 'auth.user':
        kwargs = {k: v for k, v in fields.items() if k not in ('groups', 'user_permissions')}
        User(**kwargs).save()
        return True

    m2m = M2M_FIELDS.get(model_name)
    m2m_ids = None
    if m2m and m2m in fields:
        m2m_ids = fields.pop(m2m)
        if m2m == 'tags' and 'tags_input' in fields:
            fields.pop('tags_input', None)

    for f in model_cls._meta.fields:
        if not isinstance(f, ForeignKey) or f.name not in fields:
            continue
        val = fields[f.name]
        if isinstance(val, f.related_model):
            continue
        if val is None:
            fields[f.name] = None
            continue

        # Autor (User)
        if f.related_model == User:
            if isinstance(val, list) and val and isinstance(val[0], str):
                user = User.objects.filter(username=val[0]).first()
            elif isinstance(val, int):
                user = User.objects.filter(pk=val).first()
            else:
                user = None
            if not user:
                user = User.objects.first()
            fields[f.name] = user
            continue

        # Outras ForeignKeys por PK ou fallback por Slug/Nome
        rel_obj = f.related_model.objects.filter(pk=val).first()
        if not rel_obj and fixture_pk_map:
            # Fallback por mapeamento do fixture
            fixture_rel = fixture_pk_map.get((f.related_model, val))
            if fixture_rel:
                if 'slug' in fixture_rel and hasattr(f.related_model, 'slug'):
                    rel_obj = f.related_model.objects.filter(slug=fixture_rel['slug']).first()
                elif 'name' in fixture_rel and hasattr(f.related_model, 'name'):
                    rel_obj = f.related_model.objects.filter(name=fixture_rel['name']).first()

        if not rel_obj:
            raise ValueError(f"ForeignKey '{f.name}' para {f.related_model.__name__} (pk={val}) não encontrada.")

        fields[f.name] = rel_obj

    # Se já existe por slug, atualiza ao invés de estourar erro de unicidade
    if 'slug' in fields and model_cls.objects.filter(slug=fields['slug']).exists():
        obj = model_cls.objects.get(slug=fields['slug'])
        for k, v in fields.items():
            setattr(obj, k, v)
        obj.save()
    else:
        pk_val = entry.get('pk')
        if pk_val is not None:
            obj = model_cls(pk=pk_val, **fields)
        else:
            obj = model_cls(**fields)
        obj.save()

    if m2m_ids:
        getattr(obj, m2m).set(m2m_ids)
    return True


def reset_sequences():
    try:
        from django.core.management.color import no_style
        sequence_sql = connection.ops.sequence_reset_sql(no_style(), list(MODELS.values()))
        with connection.cursor() as cursor:
            for sql in sequence_sql:
                cursor.execute(sql)
        print('=> Sequences de banco sincronizadas com sucesso.')
    except Exception as e:
        pass


def main():
    print('=> Restaurando imagens para media/ ...')
    restore_media()

    if not os.path.isfile(FIXTURE):
        print('ERRO: fixture.json nao encontrado em', FIXTURE)
        sys.exit(1)

    print('=> Importando entradas novas (fixture.json) ...')
    with open(FIXTURE, encoding='utf-8') as f:
        entries = json.load(f)

    # Mapeamento auxiliar: (related_model, pk) -> fields do fixture
    fixture_pk_map = {}
    for e in entries:
        m = e.get('model')
        if m in MODELS and 'pk' in e:
            fixture_pk_map[(MODELS[m], e['pk'])] = e['fields']

    # Ordena topologicamente para criar dependências primeiro
    def get_sort_key(e):
        m = e['model']
        return MODEL_ORDER.index(m) if m in MODEL_ORDER else 99

    sorted_entries = sorted(entries, key=get_sort_key)

    created = 0
    skipped = 0
    failed = 0
    failed_entries = []

    for entry in sorted_entries:
        model_name = entry['model']
        if model_name not in MODELS:
            continue
        with transaction.atomic():
            if entry_exists(model_name, entry):
                skipped += 1
                continue
            try:
                if create_entry(model_name, entry, fixture_pk_map):
                    created += 1
                    print(f'   + {model_name} {entry.get("pk", "")}')
                else:
                    skipped += 1
            except Exception as e:  # noqa: BLE001
                failed_entries.append((entry, str(e)))

    # Segunda passada para eventuais itens que dependiam de registros criados depois
    if failed_entries:
        print(f'=> Executando 2ª passada para {len(failed_entries)} item(ns) pendente(s)...')
        still_failed = []
        for entry, first_err in failed_entries:
            model_name = entry['model']
            with transaction.atomic():
                if entry_exists(model_name, entry):
                    skipped += 1
                    continue
                try:
                    if create_entry(model_name, entry, fixture_pk_map):
                        created += 1
                        print(f'   + [retry] {model_name} {entry.get("pk", "")}')
                    else:
                        skipped += 1
                except Exception as e:
                    still_failed.append((entry, str(e)))
                    print(f'   ! {model_name} {entry.get("pk", "")}: {e}')
        failed = len(still_failed)

    # Remove categorias vazias residuais no banco (excluindo as que estão ativas no fixture)
    fixture_cat_slugs = {
        e['fields']['slug'] for e in entries if e['model'] == 'reviews.category' and 'slug' in e.get('fields', {})
    }
    empty_cats = reviews_models.Category.objects.filter(
        products__isnull=True,
        guides__isnull=True
    ).exclude(slug__in=fixture_cat_slugs)

    if empty_cats.exists():
        count_empty = empty_cats.count()
        empty_cats.delete()
        print(f'=> Removidas {count_empty} categoria(s) vazia(s) do banco.')

    reset_sequences()

    print(f'Concluido: {created} criado(s), {skipped} existente(s), {failed} erro(s).')
    return {'created': created, 'skipped': skipped, 'failed': failed}


if __name__ == '__main__':
    main()