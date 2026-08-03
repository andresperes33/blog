"""Importa o conteudo do blog a partir do backup versionado.

Uso (na producao, apos o deploy):
    python import_content.py

Restaura:
    content_backup/media/*  -> MEDIA_ROOT (imagens)
    content_backup/fixture.json -> banco (artigos, categorias, produtos, usuarios)

Nao sobrescreve conteudo existente: registros com mesmo slug/nome
sao ignorados (loaddata com chaves naturais).
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
    print('=> Restaurando imagens para media/ ...')
    if os.path.isdir(MEDIA_BACKUP):
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
        shutil.copytree(MEDIA_BACKUP, settings.MEDIA_ROOT, dirs_exist_ok=True)
        print(f'   OK -> {settings.MEDIA_ROOT}')
    else:
        print('   (sem pasta media no backup)')

    print('=> Importando dados do banco ...')
    if os.path.isfile(FIXTURE):
        call_command('loaddata', FIXTURE, verbosity=1)
        print('   OK')
    else:
        print('   ERRO: fixture.json nao encontrado em', FIXTURE)
        sys.exit(1)

    print('Concluido.')


if __name__ == '__main__':
    main()
