import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from reviews.models import Category

mapping = {
    'Mobile': 'icon-mobile',
    'Laptops': 'icon-laptop',
    'Áudio': 'icon-audio',
    'Microfones': 'icon-mic',
    'Placas de Vídeo': 'icon-gpu',
    'Placas Mãe': 'icon-cpu'
}

for name, icon_id in mapping.items():
    try:
        cat = Category.objects.get(name=name)
        cat.icon = icon_id
        cat.save()
        print(f"Updated {name} to {icon_id}")
    except Category.DoesNotExist:
        pass

print("Icons convertidos para identificadores SVG com sucesso!")
