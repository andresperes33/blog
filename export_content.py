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
    with open(FIXTURE, 'w', encoding='utf-8') as f:
        call_command(
            'dumpdata',
            'reviews',
            'auth.User',
            '--natural-foreign',
            '--natural-primary',
            '--indent', '2',
            stdout=f,
        )
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
