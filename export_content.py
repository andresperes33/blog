"""Exporta o conteudo do blog (artigos + imagens) para versionar no git.

Uso:
    python export_content.py

Gera:
    content_backup/fixture.json   -> dump do banco (reviews + usuario autor)
    content_backup/media/         -> copia das imagens de media/

Depois basta commitar a pasta content_backup/ e fazer o deploy.
"""

import os
import sys
import shutil
import django

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.conf import settings
from django.core.management import call_command

BACKUP_DIR = os.path.join(os.getcwd(), 'content_backup')
FIXTURE = os.path.join(BACKUP_DIR, 'fixture.json')
MEDIA_BACKUP = os.path.join(BACKUP_DIR, 'media')


def main():
    os.makedirs(BACKUP_DIR, exist_ok=True)

    print('=> Exportando banco (reviews + usuarios)...')
    from io import StringIO
    import json

    buf = StringIO()
    call_command(
        'dumpdata',
        'reviews',
        'auth.User',
        '--natural-foreign',
        '--natural-primary',
        '--indent', '2',
        stdout=buf,
    )
    raw_data = json.loads(buf.getvalue())

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

    def sort_key(e):
        m = e.get('model', '')
        return (MODEL_ORDER.index(m) if m in MODEL_ORDER else 99, e.get('pk', 0))

    sorted_data = sorted(raw_data, key=sort_key)
    with open(FIXTURE, 'w', encoding='utf-8') as f:
        json.dump(sorted_data, f, indent=2, ensure_ascii=False)
    print(f'   OK -> {FIXTURE}')

    print('=> Copiando imagens de media/ ...')
    if os.path.isdir(settings.MEDIA_ROOT):
        if os.path.isdir(MEDIA_BACKUP):
            shutil.rmtree(MEDIA_BACKUP)
        shutil.copytree(settings.MEDIA_ROOT, MEDIA_BACKUP)
        print(f'   OK -> {MEDIA_BACKUP}')
    else:
        print('   (media/ nao existe, nada a copiar)')

    print('Concluido. Commit a pasta content_backup/ e faca o deploy.')


if __name__ == '__main__':
    main()
