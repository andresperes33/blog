import os
import sys
import django

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from reviews.models import Category, Product, Review

# Create User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')

user = User.objects.get(username='admin')

# Create Categories
cat_mobile, _ = Category.objects.get_or_create(name='Mobile', icon='📱')
cat_laptop, _ = Category.objects.get_or_create(name='Laptops', icon='💻')
cat_audio, _ = Category.objects.get_or_create(name='Áudio', icon='🎧')

# Products
p1, _ = Product.objects.get_or_create(name='Galaxy S24 Ultra', brand='Samsung', category=cat_mobile)
p2, _ = Product.objects.get_or_create(name='MacBook Pro M3', brand='Apple', category=cat_laptop)

# Reviews
r1_img = [f for f in os.listdir('media/reviews/main/') if 'smartphone' in f.lower()][0]
r1, created = Review.objects.get_or_create(
    product=p1,
    title='Galaxy S24 Ultra: O Rei do Android?',
    defaults={
        'excerpt': 'O novo topo de linha da Samsung promete revolucionar com IA e câmeras imbatíveis.',
        'content': '<h2>Design e Tela</h2><p>O Titanium é a grande estrela aqui. A tela plana de 6.8 polegadas com brilho pico de 2600 nits é simplesmente a melhor do mercado...</p><h2>Performance</h2><p>Equipado com o Snapdragon 8 Gen 3 for Galaxy, a fluidez é absurda.</p>',
        'rating': 9.5,
        'pros': 'Câmeras fenomenais\nIA integrada útil\nBateria de longa duração\nTela sensacional',
        'cons': 'Preço muito elevado\nCarregamento ainda lento comparado a rivais',
        'author': user,
        'main_image': f'reviews/main/{r1_img}',
        'is_featured': True,
        'specifications': {'Processador': 'Snapdragon 8 Gen 3', 'RAM': '12GB', 'Bateria': '5000mAh'}
    }
)

r2_img = [f for f in os.listdir('media/reviews/main/') if 'laptop' in f.lower()][0]
r2, created = Review.objects.get_or_create(
    product=p2,
    title='MacBook Pro M3 Max: Poder Bruto e Eficiência',
    defaults={
        'excerpt': 'A Apple eleva o nível novamente com o chip M3 Max. Vale o upgrade?',
        'content': '<h2>O Poder do M3 Max</h2><p>Testamos a versão topo de linha e fomos surpreendidos pela capacidade de renderização em 3D e edição de vídeo 8K sem sequer ligar as ventoinhas em uso moderado...</p>',
        'rating': 9.8,
        'pros': 'Performance inigualável\nDuração de bateria de 22h\nTela Liquid Retina XDR',
        'cons': 'Design idêntico ao anterior\nBase model com apenas 8GB RAM\nExtremamente caro',
        'author': user,
        'main_image': f'reviews/main/{r2_img}',
        'is_featured': True,
        'specifications': {'GPU': '40 Cores', 'Tela': '16.2 Mini-LED', 'Portas': '3x Thunderbolt 4'}
    }
)

print("Dados populados com sucesso!")
