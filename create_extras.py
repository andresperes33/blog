import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from reviews.models import Category

Category.objects.get_or_create(name='Microfones', defaults={'icon': '🎙️'})
Category.objects.get_or_create(name='Placas de Vídeo', defaults={'icon': '🎮'})
Category.objects.get_or_create(name='Placas Mãe', defaults={'icon': '⚙️'})

print("Categorias criadas com sucesso!")
