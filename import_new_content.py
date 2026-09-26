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


def find_natural_key(model_cls, model_name, fields):
    """Retorna o objeto pelo seu identificador natural (slug/username/brand+nome).

    PK nao serve como identificador natural: os numeros do fixture vem do banco
    local e nao batem com o banco de producao, que acumula registros de varios
    deploys. Um objeto que tem o mesmo PK do fixture pode ser outra categoria
    inteira, e ai aimportacao pula a entrada ou aponta a FK para o registro
    errado sem avisar.
    """
    if model_name == 'auth.user':
        return User.objects.filter(username=fields.get('username')).first()

    # Categoria, guia, review, comparacao e tag tem slug
    if 'slug' in fields and hasattr(model_cls, 'slug'):
        return model_cls.objects.filter(slug=fields['slug']).first()

    # Produto nao tem slug: a chave natural e brand + name
    if model_name == 'reviews.product':
        return model_cls.objects.filter(
            brand=fields.get('brand', ''), name=fields.get('name', '')
        ).first()

    return None


def entry_exists(model_name, entry):
    fields = entry['fields']

    # Chave natural tem prioridade sobre qualquer outra verificacao
    if find_natural_key(MODELS[model_name], model_name, fields) is not None:
        return True

    # Guia e um caso especial: dentro dele o par (guide, position) e a chave
    if model_name == 'reviews.guideitem':
        guide_val = fields.get('guide')
        pos = fields.get('position')
        if guide_val and pos:
            if MODELS[model_name].objects.filter(guide_id=guide_val, position=pos).exists():
                return True

    # So cai para o PK quando o modelo nao tem nenhuma chave natural
    if 'slug' not in fields and 'brand' not in fields and model_name != 'auth.user':
        pk = entry.get('pk')
        if pk is not None:
            return MODELS[model_name].objects.filter(pk=pk).exists()
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

        # Outras ForeignKeys: a chave natural do fixture tem prioridade sobre o
        # PK. Resolver por PK primeiro apontava a FK para o registro errado
        # quando os numeros do fixture nao batem com a producao, sem avisar.
        rel_obj = None
        if fixture_pk_map:
            fixture_rel = fixture_pk_map.get((f.related_model, val))
            if fixture_rel:
                if 'slug' in fixture_rel and hasattr(f.related_model, 'slug'):
                    rel_obj = f.related_model.objects.filter(slug=fixture_rel['slug']).first()
                elif 'name' in fixture_rel and hasattr(f.related_model, 'name'):
                    rel_obj = f.related_model.objects.filter(name=fixture_rel['name']).first()

        if not rel_obj:
            rel_obj = f.related_model.objects.filter(pk=val).first()

        if not rel_obj:
            raise ValueError(f"ForeignKey '{f.name}' para {f.related_model.__name__} (pk={val}) não encontrada.")

        fields[f.name] = rel_obj

    # Se ja existe pela chave natural, atualiza ao inves de estourar erro de
    # unicidade. Isso tambem reconcilia FKs que ficaram erradas em import
    # anterior: sem este caminho o produto ja criado continuaria apontando
    # para a categoria errada para sempre, porque o import so cria o que falta.
    existing = find_natural_key(model_cls, model_name, fields)
    if existing is not None:
        for k, v in fields.items():
            setattr(existing, k, v)
        existing.save()
        obj = existing
    else:
        pk_val = entry.get('pk')
        if pk_val is not None and model_cls.objects.filter(pk=pk_val).exists():
            # PK do fixture ja ocupado por outro registro: deixa o banco
            # gerar o proximo, em vez de sobrescrever o objeto existente.
            obj = model_cls(**fields)
        elif pk_val is not None:
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