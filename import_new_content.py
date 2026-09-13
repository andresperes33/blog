"""Importa o conteudo versionado de forma incremental e idempotente.

Usado automaticamente no deploy (CMD do Dockerfile) para puxar artigos novos
para o EasyPanel sem conflitar com o que ja existe no banco: registros cujo
pk (ou username, para usuarios) ja existem sao ignorados.

Uso:
    python import_new_content.py
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
from django.db import transaction
from django.db.models import ForeignKey
from reviews import models as reviews_models

BACKUP_DIR = os.path.join(os.getcwd(), 'content_backup')
FIXTURE = os.path.join(BACKUP_DIR, 'fixture.json')
MEDIA_BACKUP = os.path.join(BACKUP_DIR, 'media')

MODELS = {
    'reviews.category': reviews_models.Category,
    'reviews.tag': reviews_models.Tag,
    'reviews.product': reviews_models.Product,
    'reviews.review': reviews_models.Review,
    'reviews.reviewimage': reviews_models.ReviewImage,
    'reviews.comparison': reviews_models.Comparison,
    'reviews.guide': reviews_models.Guide,
    'reviews.guideitem': reviews_models.GuideItem,
    'auth.user': User,
}

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
    return MODELS[model_name].objects.filter(pk=entry['pk']).exists()


def create_entry(model_name, entry):
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
        if isinstance(val, list) and val and isinstance(val[0], str):
            fields[f.name] = f.related_model.objects.get(username=val[0])
        else:
            fields[f.name] = f.related_model.objects.get(pk=val)

    obj = model_cls(pk=entry['pk'], **fields)
    obj.save()

    if m2m_ids:
        getattr(obj, m2m).set(m2m_ids)
    return True


def main():
    print('=> Restaurando imagens para media/ ...')
    restore_media()

    if not os.path.isfile(FIXTURE):
        print('ERRO: fixture.json nao encontrado em', FIXTURE)
        sys.exit(1)

    print('=> Importando entradas novas (fixture.json) ...')
    with open(FIXTURE, encoding='utf-8') as f:
        entries = json.load(f)

    created = 0
    skipped = 0
    failed = 0
    for entry in entries:
        model_name = entry['model']
        if model_name not in MODELS:
            continue
        with transaction.atomic():
            if entry_exists(model_name, entry):
                skipped += 1
                continue
            try:
                if create_entry(model_name, entry):
                    created += 1
                    print(f'   + {model_name} {entry.get("pk", "")}')
                else:
                    skipped += 1
            except Exception as e:  # noqa: BLE001
                failed += 1
                print(f'   ! {model_name} {entry.get("pk", "")}: {e}')

    print(f'Concluido: {created} criado(s), {skipped} existente(s), {failed} erro(s).')


if __name__ == '__main__':
    main()