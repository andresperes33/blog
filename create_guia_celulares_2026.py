"""Cria o guia de compra "Melhores celulares 2026" (Guide + GuideItems) no banco local.

Uso:
    python create_guia_celulares_2026.py

Depois edite manualmente content_backup/fixture.json (o export_content.py nao pode
ser rodado porque apagaria o review do Positivo) e copie o conteudo de media/guides
para content_backup/media/guides/.
"""

import os
import sys
import django

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from PIL import Image, ImageDraw, ImageFont  # noqa: E402
from django.conf import settings  # noqa: E402
from django.contrib.auth.models import User  # noqa: E402
from reviews.models import Category, Guide, GuideItem  # noqa: E402

SLUG = 'melhores-celulares-2026'
TITLE = 'Melhores celulares para comprar em 2026: guia completo de custo-benefício'
EXCERPT = ('Descubra os melhores celulares de 2026 por faixa de preço: do Samsung Galaxy A07 '
           '(abaixo de R$ 1.000) ao Galaxy S25 Ultra, passando por Redmi Note 15, Galaxy A36, '
           'Moto G86, Galaxy A57, Edge 60 Neo, Poco X8 Pro e Xiaomi 17. Guia de compra completo '
           'com preços, pros e contras de cada modelo e links das melhores ofertas.')

CONTENT = """
<p>Nunca foi tão difícil escolher um celular: só no último ano foram dezenas de modelos novos, alguns já fora de estoque e outros aparecendo com preço surreal. Por isso este guia reúne os <strong>melhores celulares para comprar em 2026</strong>, organizados por faixa de preço, do mais barato ao mais topo de linha — com o foco em <strong>custo-benefício</strong>.</p>

<h2>Como escolhemos os melhores celulares de 2026</h2>
<p>Analisamos desempenho (AnTuTu), tela, câmera, bateria, resistência à água (IP67/IP68/IP69) e, principalmente, o <strong>preço que o aparelho costuma aparecer em promoção</strong> no Brasil. Também levamos em conta o suporte de atualizações, que hoje ultrapassa os 5 anos nos principais modelos.</p>

<h2>Melhores celulares abaixo de R$ 1.000</h2>
<p>Nesta faixa a recomendação principal é o <strong>Samsung Galaxy A07</strong>: é o conjunto mais completinho que você encontra, com <strong>8 GB de RAM e 256 GB de armazenamento</strong>, tela de 6.7 polegadas a 90 Hz, bateria de 5.000 mAh e desempenho que dá conta do dia a dia e até um game leve. A média de preço gira em torno de R$ 870, mas aparece bem mais barato em promoção.</p>

<h2>Melhores celulares até R$ 1.500</h2>
<p>Aqui o <strong>Redmi Note 15 4G</strong> é a aposta da Xiaomi com tela AMOLED de 120 Hz, até 8 GB de RAM, bateria de 6.000 mAh e 6 anos de atualizações. Quase que pelo mesmo preço, o <strong>Galaxy A36 5G</strong> rouba a cena nas promoções: tela Super AMOLED 120 Hz, resistência IP67, gravação em 4K a 30 fps, Galaxy AI e <strong>7 anos de atualização</strong>. Quem quer mais armazenamento leva o <strong>Galaxy A17 4G</strong> (256 GB + 8 GB de RAM) ou o <strong>Moto G86</strong>, com IP68/IP69, OLED 120 Hz e 256 GB.</p>

<h2>Melhores celulares até R$ 2.000</h2>
<p>O campeão da faixa é o <strong>Galaxy A57 5G</strong>, que hoje vale mais a pena que o A56: construção em metal e vidro, IP67, Exynos 1680 com mais de <strong>1,1 milhão de pontos no AnTuTu</strong>, Galaxy AI e conjunto de câmeras excelente. Para quem prefere a Motorola, os <strong>Edge 60 Neo</strong> e <strong>Edge 70 Fusion</strong> entregam muito armazenamento e câmera com telefoto pelo preço. E o <strong>Poco X8 Pro</strong> é o celular mais completo para quem não quer dor de cabeça: <strong>Dimensity 8500 Ultra</strong>, bateria de 6.500 mAh com carga de <strong>100 W e carregador na caixa</strong>, e resistência IP69K.</p>

<h2>Melhores celulares de R$ 2.500 a R$ 3.500</h2>
<p>O <strong>Poco X8 Pro Max</strong> é a melhor alternativa abaixo de R$ 3.000 para um aparelho extremamente completo: Dimensity 9500, 12 GB de RAM e bateria absurda de <strong>8.500 mAh</strong>. Quem prioriza câmera leva o <strong>Edge 70 Pro</strong> (telefoto de 50 MP) ou o <strong>Poco F8 Pro</strong>, com Snapdragon 8 Elite e tela AMOLED de 144 Hz. Já o <strong>Galaxy S25</strong> só vale a pena em promoção, quando aparece perto dos R$ 3.000.</p>

<h2>Melhores celulares topo de linha em 2026</h2>
<p>Acima de R$ 4.000, o destaque é o <strong>Galaxy S25 Ultra</strong>: construção em titânio, S Pen com Bluetooth, câmera principal de 200 MP, Snapdragon 8 Elite e 7 anos de suporte — na nossa opinião, o <strong>melhor celular que você pode comprar hoje</strong>. De perto aparecem a <strong>Motorola Signature</strong> (ótima tela e 512 GB, mas gravação abaixo da concorrência), o <strong>Xiaomi 17</strong> e o <strong>Xiaomi 17T Pro</strong>, tops de linha da Xiaomi que finalmente recomendamos.</p>
"""

CONCLUSION = """
<p>Para 2026, a nossa opinião final é a seguinte:</p>
<ul>
<li><strong>Melhor custo-benefício geral:</strong> Samsung Galaxy A57 5G — potência, câmera e construção premium por menos de R$ 2.000.</li>
<li><strong>Melhor abaixo de R$ 1.000:</strong> Samsung Galaxy A07, o básico bem feito.</li>
<li><strong>Melhor para bateria:</strong> Poco X8 Pro Max, com 8.500 mAh.</li>
<li><strong>Melhor topo de linha:</strong> Samsung Galaxy S25 Ultra, o celular mais completo do momento.</li>
<li><strong>Melhor para câmera na faixa:</strong> Edge 70 Pro e Galaxy S25.</li>
</ul>
<p>Comprando pelos links deste guia você ajuda o André Indica a continuar trazendo análises honestas, sem pagar nada a mais.</p>
"""

ITEMS = [
    {
        'position': 1,
        'name': 'Samsung Galaxy A07',
        'slug': 'samsung-galaxy-a07',
        'description': ('<p>O <strong>Galaxy A07</strong> é a melhor opção abaixo de R$ 1.000 — e quem usa diz que não existe concorrente com a mesma qualidade nessa faixa. O destaque é a configuração: <strong>8 GB de RAM e 256 GB de armazenamento</strong>, além de um processador que lidera a categoria e ainda dá conta de um game leve.</p>'
                        '<p>Tela LCD de 6.7 polegadas a 90 Hz, conjunto de câmeras OK e bateria de <strong>5.000 mAh</strong> completam o pacote. Custa em média R$ 870 e aparece bastante em promoção.</p>'),
        'pros': ('Melhor custo-benefício abaixo de R$ 1.000\n'
                 'Versão recomendada com 8 GB de RAM e 256 GB\n'
                 'Tela 6.7" com 90 Hz\n'
                 'Bateria de 5.000 mAh\n'
                 'Rodar game leve sem engasgos'),
        'cons': ('Tela LCD (não é AMOLED)\n'
                 'Conjunto de câmeras apenas OK pela faixa\n'
                 'Versão 4 GB/128 GB deve ser evitada'),
        'amazon': 'https://www.amazon.com.br/dp/B0iEJLc2w?tag=andre0cda-20',
        'ml': 'https://www.mercadolivre.com.br/p/MLB54964804?matt_tool=83406274&matt_word=camilamartinstar',
    },
    {
        'position': 2,
        'name': 'Xiaomi Redmi Note 15 4G',
        'slug': 'xiaomi-redmi-note-15-4g',
        'description': ('<p>O <strong>Redmi Note 15 4G</strong> é a porta de entrada premium da Xiaomi: tela <strong>AMOLED de 120 Hz</strong>, 6 ou 8 GB de RAM, bateria enorme de <strong>6.000 mAh</strong> e um pacote de <strong>6 anos de atualizações de segurança</strong>.</p>'
                        '<p>O conjunto de câmeras é OK pela faixa de preço (nada excepcional), mas o desempenho é excelente para quem quer um patamar acima sem gastar muito. Custa entre R$ 1.100 e R$ 1.300, e costuma aparecer perto de R$ 1.000 em promoção.</p>'),
        'pros': ('Tela AMOLED de 120 Hz\n'
                 'Bateria de 6.000 mAh\n'
                 '6 ou 8 GB de RAM\n'
                 '6 anos de atualizações de segurança\n'
                 'Ótimo desempenho da Xiaomi para o processador'),
        'cons': ('Câmeras apenas OK pela faixa\n'
                 'Carregamento não é o mais rápido do segmento'),
        'amazon': 'https://www.amazon.com.br/dp/B0dpkSi6o?tag=andre0cda-20',
        'ml': 'https://www.mercadolivre.com.br/smartphone-xiaomi-redmi-note-15-4g-6gb-ram-128gb-tela-amoled-677-camera-108mp-azul/p/MLB67657658?matt_tool=83406274&matt_word=camilamartinstar',
        'shopee': 'https://s.shopee.com.br/7ptDKJlOZm',
    },
    {
        'position': 3,
        'name': 'Samsung Galaxy A36 5G',
        'slug': 'samsung-galaxy-a36-5g',
        'description': ('<p>Na nossa opinião, o <strong>Galaxy A36 5G</strong> é o melhor celular por volta de R$ 1.000 — principalmente quando pega promoção (já apareceu por R$ 800). Tela <strong>Super AMOLED 120 Hz</strong>, resistência <strong>IP67</strong>, 6 GB de RAM e um conjunto de câmeras absurdo para a faixa, com gravação em <strong>4K a 30 fps</strong>.</p>'
                        '<p>O <strong>Snapdragon 6 Gen 3</strong> marca quase 800 mil pontos no AnTuTu V11, e ainda tem <strong>Galaxy AI</strong> e 7 anos de atualização da Samsung. Único ponto fraco: a versão acessível tem só 128 GB (a de 256 GB fica bem mais cara).</p>'),
        'pros': ('Snapdragon 6 Gen 3 (~800 mil no AnTuTu)\n'
                 'Tela Super AMOLED 120 Hz\n'
                 'Resistência IP67\n'
                 'Câmeras top pela faixa, grava em 4K 30 fps\n'
                 'Galaxy AI + 7 anos de atualização'),
        'cons': ('Versão acessível tem apenas 128 GB\n'
                 'Versão de 256 GB custa bem mais caro'),
        'amazon': 'https://www.amazon.com.br/dp/B0aNVs1C9?tag=andre0cda-20',
        'ml': 'https://www.mercadolivre.com.br/smartphone-samsung-galaxy-a36-5g-256gb-8gb-ram/p/MLB47111905?matt_tool=83406274&matt_word=camilamartinstar',
    },
    {
        'position': 4,
        'name': 'Samsung Galaxy A17 4G',
        'slug': 'samsung-galaxy-a17-4g',
        'description': ('<p>O <strong>Galaxy A17 4G</strong> é basicamente um A07 melhorado: tela AMOLED, câmeras com resultado um pouco superior e, na versão que recomendamos, <strong>256 GB + 8 GB de RAM</strong>. Custa em torno de R$ 1.000 a R$ 1.100.</p>'
                        '<p>Se passar disso, não recomendamos — existem opções melhores na faixa. É a escolha certa para quem precisa de bastante armazenamento sem sair dos R$ 1.100.</p>'),
        'pros': ('Versão ideal com 256 GB e 8 GB de RAM\n'
                 'Tela AMOLED melhor que a do A07\n'
                 'Câmeras com resultado superior ao A07'),
        'cons': ('Acima de ~R$ 1.100 perde a graça\n'
                 'É um A07 melhorado cobrando mais caro'),
        'amazon': 'https://www.amazon.com.br/dp/B06Hyzp1H?tag=andre0cda-20',
    },
    {
        'position': 5,
        'name': 'Motorola Moto G86 5G',
        'slug': 'moto-g86',
        'description': ('<p>O <strong>Moto G86</strong> é a melhor alternativa ao Galaxy A36 para quem quer mais armazenamento: <strong>256 GB e 8 GB de RAM</strong>, tela OLED 120 Hz, resistência à água <strong>IP68/IP69</strong> e carregamento mais rápido de 30 W.</p>'
                        '<p>O <strong>Dimensity 7300</strong> entrega potência até um pouco superior ao A36 (cerca de 900 mil no AnTuTu V11) e as câmeras gravam em 4K. Bateria de 5.200 mAh. Excelente pacote na faixa dos R$ 1.500 a R$ 1.600.</p>'),
        'pros': ('256 GB e 8 GB de RAM\n'
                 'Resistência IP68/IP69\n'
                 'Dimensity 7300 (~900 mil no AnTuTu)\n'
                 'Tela OLED 120 Hz\n'
                 'Carga de 30 W com 5.200 mAh'),
        'cons': ('Preço costuma ficar um pouco acima do A36\n'
                 'Marca menos forte em fotografia que a Samsung'),
        'amazon': 'https://www.amazon.com.br/dp/B08VRqD9Q?tag=andre0cda-20',
        'ml': 'https://www.mercadolivre.com.br/smartphone-motorola-moto-g86-5g-256gb-24gb-8gb-ram16gb-ram-boost-tela-15k-poled-50mp-sony-camera-ois-moto-ai-videos-em-4k-ip68-ip69-vermelho/p/MLB51340616?matt_tool=83406274&matt_word=camilamartinstar',
    },
    {
        'position': 6,
        'name': 'Samsung Galaxy A57 5G',
        'slug': 'samsung-galaxy-a57-5g',
        'description': ('<p>O <strong>Galaxy A57 5G</strong> é a nossa escolha de melhor custo-benefício do guia. Ele é como um A36 melhorado: construção em <strong>metal e vidro</strong> (contra plástico do A36), mantendo o IP67, tela AMOLED 120 Hz e bateria de 5.000 mAh.</p>'
                        '<p>O grande salto é o <strong>Exynos 1680</strong>, que passa de <strong>1,1 milhão de pontos no AnTuTu</strong>. Tem Galaxy AI, 7 anos de atualização e o melhor conjunto de câmeras da linha — impecável na foto e no vídeo. Custa de R$ 1.800 (128 GB) a R$ 2.100 (256 GB).</p>'),
        'pros': ('Exynos 1680 com mais de 1,1 milhão no AnTuTu\n'
                 'Construção em metal e vidro com IP67\n'
                 'Conjunto de câmeras excelente (foto e vídeo)\n'
                 'Galaxy AI + 7 anos de atualização\n'
                 'Tela AMOLED 120 Hz e 5.000 mAh'),
        'cons': ('Versão de 256 GB chega perto de R$ 2.100\n'
                 'Acabamento premium quase sem concorrência na faixa'),
        'amazon': 'https://www.amazon.com.br/dp/B01aCEDt2?tag=andre0cda-20',
        'ml': 'https://www.mercadolivre.com.br/celular-samsung-galaxy-a57-5g-128gb-8gb-ram-camera-50mp-ip68-super-amoled-67/p/MLB68213520?matt_tool=83406274&matt_word=camilamartinstar',
    },
    {
        'position': 7,
        'name': 'Motorola Edge 60 Neo',
        'slug': 'motorola-edge-60-neo',
        'description': ('<p>O <strong>Edge 60 Neo</strong> é um dos intermediários mais completos da Motorola abaixo de R$ 2.000: <strong>12 GB de RAM e 256 GB de armazenamento</strong>, tela OLED 120 Hz e bateria de 5.200 mAh.</p>'
                        '<p>Traz um diferencial raro: câmera <strong>telefoto de 10 MP</strong> além da principal de 50 MP e ultra-wide de 13 MP — ou seja, zoom de verdade, coisa que o Galaxy A57 não tem. O <strong>Dimensity 7400</strong> marca cerca de 900 mil no AnTuTu. Custa por volta de R$ 1.900 a R$ 2.000.</p>'),
        'pros': ('12 GB de RAM e 256 GB de armazenamento\n'
                 'Câmera com telefoto (zoom real)\n'
                 'Dimensity 7400 (~900 mil no AnTuTu)\n'
                 'Tela OLED 120 Hz\n'
                 'Bateria de 5.200 mAh'),
        'cons': ('Fica na casa dos R$ 2.000, não abaixo\n'
                 'Câmera frontal apenas regular'),
        'amazon': 'https://www.amazon.com.br/dp/B0aXH4SrQ?tag=andre0cda-20',
        'ml': 'https://www.mercadolivre.com.br/p/MLB58684601?matt_tool=83406274&matt_word=camilamartinstar',
    },
    {
        'position': 8,
        'name': 'Motorola Edge 70 Fusion',
        'slug': 'motorola-edge-70-fusion',
        'description': ('<p>O <strong>Edge 70 Fusion</strong> entrega mais potência que o Edge 60 Neo — passa de <strong>1 milhão de pontos no AnTuTu</strong>. Em compensação, tem menos bateria (4.800 mAh) e conjunto de câmeras mais simples (principal + ultra-wide, sem telefoto).</p>'
                        '<p>Se você encontrar o Edge 60 Neo com preço melhor, ele continua sendo o pacote mais completo. O Fusion vale mais quando o preço competitivo compensa: parte de cerca de R$ 2.100.</p>'),
        'pros': ('Mais de 1 milhão de pontos no AnTuTu\n'
                 'Boa construção e tela OLED de alta taxa\n'
                 'Carregamento rápido'),
        'cons': ('Bateria menor: 4.800 mAh\n'
                 'Conjunto de câmeras menos completo (sem telefoto)\n'
                 'A partir de R$ 2.100'),
        'amazon': 'https://www.amazon.com.br/dp/B0fVuuS1f?tag=andre0cda-20',
        'ml': 'https://www.mercadolivre.com.br/smartphone-motorola-edge-70-fusion-5g-256gb-24gb-8gb-ram-16gb-ram-boost-camera-50mp-sony-lytia-710-tela-15k-extreme-amoled-144hz-roxo/p/MLB65919757?matt_tool=83406274&matt_word=camilamartinstar',
    },
    {
        'position': 9,
        'name': 'Motorola Edge 70 5G',
        'slug': 'motorola-edge-70-5g',
        'description': ('<p>O <strong>Edge 70 5G</strong> é o irmão do Fusion com um pouco mais de potência, mas com menos bateria (4.800 mAh) e câmeras mais simples (principal + ultra-wide, sem telefoto).</p>'
                        '<p>Por custar em torno de R$ 2.200, ele só faz sentido quando o preço está abaixo do esperado. Em geral, o Edge 60 Neo com desconto é uma compra mais completa.</p>'),
        'pros': ('Potência levemente superior ao Fusion\n'
                 'Tela 120 Hz de alta qualidade\n'
                 'Design ultrafino'),
        'cons': ('Bateria de 4.800 mAh\n'
                 'Câmeras menos completas (sem telefoto)\n'
                 'Dificilmente compensa sobre o Edge 60 Neo'),
        'amazon': 'https://www.amazon.com.br/dp/B013SNUlv?tag=andre0cda-20',
        'ml': 'https://www.mercadolivre.com.br/smartphone-motorola-edge-70-5g-256gb-24gb-8gb-ram16gb-ram-boost-ultrafino-3-cameras-50mp-tela-15k-extreme-amoled-120hz-preto/p/MLB65304413?matt_tool=83406274&matt_word=camilamartinstar',
    },
    {
        'position': 10,
        'name': 'Xiaomi Poco X8 Pro',
        'slug': 'poco-x8-pro',
        'description': ('<p>O <strong>Poco X8 Pro</strong> é o celular mais completo para quem quer parada boa e não quer dor de cabeça. Tela <strong>AMOLED 120 Hz</strong>, construção em vidro e metal com melhor resistência à água (<strong>IP69K</strong>) e o processador mais potente da faixa: <strong>Dimensity 8500 Ultra</strong>, com quase 2,6 milhões no AnTuTu.</p>'
                        '<p>Bateria de <strong>6.500 mAh com carga de 100 W e carregador na caixa</strong>. E as câmeras, que eram ponto fraco, melhoraram muito. Oscila entre R$ 2.000 e R$ 2.300 e aparece com frequência em promoção.</p>'),
        'pros': ('Dimensity 8500 Ultra (~2,6 milhões no AnTuTu)\n'
                 'Bateria 6.500 mAh com carga de 100 W (carregador na caixa)\n'
                 'Resistência IP69K\n'
                 'Tela AMOLED 120 Hz, vidro e metal\n'
                 'Câmeras boas na faixa (melhoraram muito)'),
        'cons': ('Oscila muito de preço\n'
                 'Câmeras não superam Samsung/Motorola na faixa'),
        'amazon': 'https://www.amazon.com.br/dp/B04bD9FjD?tag=andre0cda-20',
        'ml': 'https://www.mercadolivre.com.br/celular-xiaomi-poco-x8-pro-5g-8gb-256gb-dual-sim-cor-preto/p/MLB69327206?matt_tool=83406274&matt_word=camilamartinstar',
        'shopee': 'https://s.shopee.com.br/W6carURIg',
    },
    {
        'position': 11,
        'name': 'Xiaomi Poco X8 Pro Max',
        'slug': 'poco-x8-pro-max',
        'description': ('<p>O <strong>Poco X8 Pro Max</strong> é a melhor alternativa abaixo de R$ 3.000 para um celular extremamente completo: processador <strong>Dimensity 9500</strong> com cerca de 3,1 milhões de pontos no AnTuTu — um dos mais potentes da faixa — e <strong>12 GB de RAM</strong>.</p>'
                        '<p>O diferencial de verdade é a bateria gigantesca de <strong>8.500 mAh</strong>: mesmo com consumo não tão baixo, dura absurdamente no dia a dia. Custa em média R$ 3.300, mas aparece bastante entre R$ 2.700 e R$ 2.900.</p>'
                        '<p><a href="https://s.shopee.com.br/6AkzLHHfNU" target="_blank" rel="nofollow">Oferta alternativa na Shopee</a></p>'),
        'pros': ('Dimensity 9500 (~3,1 milhões no AnTuTu)\n'
                 'Bateria absurda de 8.500 mAh\n'
                 '12 GB de RAM\n'
                 'Aparece em promoção de R$ 2.700 a R$ 2.900'),
        'cons': ('Conjunto de câmeras não é excepcional\n'
                 'Preço cheio de ~R$ 3.300'),
        'shopee': 'https://s.shopee.com.br/4VclMDJgF7',
    },
    {
        'position': 12,
        'name': 'Motorola Edge 70 Pro',
        'slug': 'motorola-edge-70-pro',
        'description': ('<p>O <strong>Edge 70 Pro</strong> é o combo mais completinho para foto com boa potência: <strong>12 GB de RAM e 256 ou 512 GB</strong>, conjunto de câmeras com principal, ultra-wide e <strong>telefoto de 50 MP</strong>, gravação excelente e tela AMOLED de 144 Hz.</p>'
                        '<p>O <strong>Dimensity 8500 Extreme</strong> entrega potência muito próxima do Poco X8 Pro, com bateria de 6.500 mAh e IP68/IP69. É como um X8 Pro para quem quer câmeras melhores — opção excelente para foto.</p>'),
        'pros': ('Telefoto de 50 MP + gravação excelente\n'
                 '12 GB de RAM e 256/512 GB\n'
                 'Dimensity 8500 Extreme (~2,6 milhões no AnTuTu)\n'
                 'Bateria de 6.500 mAh com IP68/IP69'),
        'cons': ('Preço perto de R$ 3.000\n'
                 'Disponibilidade varia muito'),
        'amazon': 'https://www.amazon.com.br/dp/B00R8xKRs?tag=andre0cda-20',
        'ml': 'https://www.mercadolivre.com.br/smartphone-motorola-edge-70-pro-5g-256gb-24gb-12gb-ram12gb-ram-boost-4-cameras-de-50mp-tela-15k-extreme-amoled-144hz-bateria-6500-mah-ip68ip69-vinho/p/MLB69322379?matt_tool=83406274&matt_word=camilamartinstar',
    },
    {
        'position': 13,
        'name': 'Xiaomi Poco F8 Pro',
        'slug': 'poco-f8-pro',
        'description': ('<p>O <strong>Poco F8 Pro</strong> é um X8 Pro Max com câmeras melhores: <strong>Snapdragon 8 Elite</strong>, câmera principal de 50 MP com telefoto de 8 MP, tela <strong>AMOLED de 144 Hz</strong> e bateria de 6.500 mAh.</p>'
                        '<p>Dentro da linha Poco, é o resultado mais completo em foto e vídeo, mantendo potência de topo. Custa em torno de R$ 3.000 a R$ 3.400, com frequentes promoções.</p>'),
        'pros': ('Snapdragon 8 Elite\n'
                 'Tela AMOLED de 144 Hz\n'
                 'Câmeras mais completas da linha Poco\n'
                 'Bateria de 6.500 mAh'),
        'cons': ('Custa mais que o X8 Pro Max\n'
                 'Disponibilidade menor no Brasil'),
        'ml': 'https://www.mercadolivre.com.br/smartphone-poco-f8-pro-5g-nfc-br-1212gb-ram-virtual-512gb-preto/p/MLB67289426?matt_tool=83406274&matt_word=camilamartinstar',
        'shopee': 'https://s.shopee.com.br/7KwwjQdgwV',
    },
    {
        'position': 14,
        'name': 'Samsung Galaxy S25',
        'slug': 'samsung-galaxy-s25',
        'description': ('<p>O <strong>Galaxy S25</strong> só vale a pena se comprado em promoção: em média custa R$ 4.000, mas aparece por cerca de R$ 3.000. Aí sim é uma excelente compra: <strong>256 GB e 12 GB de RAM</strong>, <strong>Snapdragon 8 Elite</strong> e o melhor conjunto de câmeras da faixa, principalmente em gravação de vídeo.</p>'
                        '<p>Único ponto fraco real é a bateria de <strong>4.000 mAh</strong>. A versão Plus não vale a pena pelo preço de R$ 4.500, e a linha S26 também não compensa em 2026.</p>'),
        'pros': ('Câmeras top da faixa (principalmente em vídeo)\n'
                 'Snapdragon 8 Elite\n'
                 '256 GB e 12 GB de RAM\n'
                 'Já aparece por ~R$ 3.000 em promoção'),
        'cons': ('Bateria de apenas 4.000 mAh\n'
                 'Preço cheio de R$ 4.000 é alto'),
        'amazon': 'https://www.amazon.com.br/dp/B018BUEjO?tag=andre0cda-20',
        'ml': 'https://www.mercadolivre.com.br/p/MLB45513356?matt_tool=83406274&matt_word=camilamartinstar',
    },
    {
        'position': 15,
        'name': 'Motorola Signature',
        'slug': 'motorola-signature',
        'description': ('<p>A <strong>Motorola Signature</strong> é um topo de linha que hoje aparece em torno de R$ 4.000 a R$ 4.500 (já custou R$ 6.000+). Traz <strong>Snapdragon 8 Gen 5</strong> com 3 milhões de pontos no AnTuTu, tela excelente, <strong>512 GB de armazenamento</strong> e bateria de 5.200 mAh.</p>'
                        '<p>As câmeras são boas, principalmente a frontal, mas têm <strong>muita IA/pós-processamento</strong> e a gravação fica bem abaixo de iPhone, Samsung e até Xiaomi. Pelo preço de R$ 4.000 é aceitável; acima disso, é um celular superestimado.</p>'),
        'pros': ('Snapdragon 8 Gen 5 (~3 milhões no AnTuTu)\n'
                 'Tela excelente\n'
                 '512 GB de armazenamento\n'
                 'Bateria de 5.200 mAh'),
        'cons': ('Gravação de vídeo abaixo de iPhone/Samsung/Xiaomi\n'
                 'Muita IA no pós-processamento das fotos\n'
                 'Preço cheio é alto (superestimado)'),
        'amazon': 'https://www.amazon.com.br/dp/B09Y3xdbz?tag=andre0cda-20',
        'ml': 'https://www.mercadolivre.com.br/p/MLB65938141?matt_tool=83406274&matt_word=camilamartinstar',
    },
    {
        'position': 16,
        'name': 'Samsung Galaxy S25 Ultra',
        'slug': 'samsung-galaxy-s25-ultra',
        'description': ('<p>Na nossa opinião, o <strong>Galaxy S25 Ultra</strong> é o melhor celular que você pode comprar hoje pelo preço praticado. <strong>Snapdragon 8 Elite</strong> (~3 milhões no AnTuTu), construção em <strong>titânio</strong>, S Pen com Bluetooth mantido e o conjunto de câmeras mais completo da categoria: sensor principal de <strong>200 MP</strong> com ultra-wide de 50 MP.</p>'
                        '<p>São 5.000 mAh com excelente eficiência energética, Galaxy AI e 7 anos de atualização. Hoje é fácil achar por volta de R$ 5.000, e já apareceu por R$ 4.400 em promoção.</p>'),
        'pros': ('Melhor conjunto de câmeras pelo preço\n'
                 'Snapdragon 8 Elite (~3 milhões no AnTuTu)\n'
                 'Construção em titânio com S Pen\n'
                 'Galaxy AI + 7 anos de atualização\n'
                 'Ótima eficiência de bateria'),
        'cons': ('Preço cheio de ~R$ 5.000\n'
                 'Grande e pesado para alguns usuários'),
        'amazon': 'https://www.amazon.com.br/dp/B045MHG7G?tag=andre0cda-20',
        'ml': 'https://www.mercadolivre.com.br/p/MLB45517552?matt_tool=83406274&matt_word=camilamartinstar',
    },
    {
        'position': 17,
        'name': 'Xiaomi 17',
        'slug': 'xiaomi-17',
        'description': ('<p>O <strong>Xiaomi 17</strong> é um dos poucos tops de linha da Xiaomi que recomendamos de verdade. <strong>Snapdragon 8 Elite</strong> com quase 3,5 milhões de pontos no AnTuTu, <strong>512 GB</strong> de armazenamento e bateria de <strong>6.330 mAh</strong> em um corpo compacto de 6.3 polegadas.</p>'
                        '<p>Conjunto de câmeras completíssimo (principal, ultra-wide e telefoto de 50 MP) e qualidade de gravação <strong>superior à Motorola</strong>. Custa cerca de R$ 5.500 — só é um pouco mais chato de encontrar.</p>'
                        '<p><a href="https://s.shopee.com.br/3LQny5JJlL" target="_blank" rel="nofollow">Oferta alternativa na Shopee</a></p>'),
        'pros': ('Snapdragon 8 Elite (~3,5 milhões no AnTuTu)\n'
                 '512 GB de armazenamento\n'
                 'Bateria de 6.330 mAh em corpo compacto\n'
                 'Câmeras completas com telefoto de 50 MP'),
        'cons': ('Preço de ~R$ 5.500\n'
                 'Mais difícil de encontrar no Brasil'),
        'shopee': 'https://s.shopee.com.br/7AdWX80KBk',
    },
    {
        'position': 18,
        'name': 'Xiaomi 17T Pro',
        'slug': 'xiaomi-17t-pro',
        'description': ('<p>O <strong>Xiaomi 17T Pro</strong> é basicamente o Xiaomi 17 com mais bateria — <strong>7.100 mAh</strong> — e preço um pouco menor, em torno de <strong>R$ 4.500</strong>. Mantém o mesmo conjunto de câmera, mudando só a ultra-wide para 12 MP.</p>'
                        '<p>O processador passa a ser <strong>Dimensity 9500</strong>, com excelente pontuação e potência sensacional. Para quem quer topo de linha gastando menos que o 17, é a escolha certa.</p>'
                        '<p><a href="https://s.shopee.com.br/2VrgyYV0yP" target="_blank" rel="nofollow">Oferta alternativa na Shopee</a></p>'),
        'pros': ('Bateria gigante de 7.100 mAh\n'
                 'Dimensity 9500 com excelente potência\n'
                 'Preço menor que o Xiaomi 17 (~R$ 4.500)\n'
                 'Conjunto de câmeras completo'),
        'cons': ('Ultra-wide de 12 MP (menor que o 17)\n'
                 'Disponibilidade limitada'),
        'shopee': 'https://s.shopee.com.br/50Z1x9HEfX',
    },
]


def _make_placeholder(path, width, height, title, subtitle, accent='#76b900'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        return
    img = Image.new('RGB', (width, height), '#0f172a')
    draw = ImageDraw.Draw(img)
    for y in range(height):
        draw.line([(0, y), (width, y)], fill=(30, 41, 59 + int(y * (60 / height))))
    try:
        font_title = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', int(height * 0.07))
        font_sub = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', int(height * 0.035))
    except OSError:
        font_title = ImageFont.load_default()
        font_sub = font_title
    for i, line in enumerate(title.split('\n')[:2]):
        bbox = draw.textbbox((0, 0), line, font=font_title)
        tw = bbox[2] - bbox[0]
        draw.text(((width - tw) / 2, height * 0.38 + i * (height * 0.085)), line,
                  fill=(255, 255, 255), font=font_title)
    if subtitle:
        bbox = draw.textbbox((0, 0), subtitle, font=font_sub)
        tw = bbox[2] - bbox[0]
        draw.text(((width - tw) / 2, height * 0.66), subtitle, fill=(253, 186, 116), font=font_sub)
    _ = accent
    img.save(path, format='WEBP', quality=82)


def create_main_image():
    path = os.path.join(settings.MEDIA_ROOT, 'guides', 'main', f'{SLUG}.webp')
    _make_placeholder(path, 1280, 720, 'Melhores\nCelulares 2026', 'André Indica')
    return f'guides/main/{SLUG}.webp'


def create_item_image(slug, name):
    path = os.path.join(settings.MEDIA_ROOT, 'guides', 'items', f'{slug}.webp')
    _make_placeholder(path, 800, 800, name, 'André Indica')
    return f'guides/items/{slug}.webp'


def main():
    category = Category.objects.get_or_create(name='Mobile')[0]
    author = User.objects.filter(username='admin').first() or User.objects.first()

    guide, created = Guide.objects.get_or_create(
        slug=SLUG,
        defaults={
            'title': TITLE,
            'category': category,
            'author': author,
            'excerpt': EXCERPT,
            'content': CONTENT,
            'conclusion': CONCLUSION,
            'main_image': create_main_image(),
            'is_published': True,
            'is_featured': True,
        },
    )
    if not created:
        guide.title = TITLE
        guide.category = category
        guide.author = author
        guide.excerpt = EXCERPT
        guide.content = CONTENT
        guide.conclusion = CONCLUSION
        guide.main_image = create_main_image()
        guide.is_published = True
        guide.is_featured = True
        guide.save()

    GuideItem.objects.filter(guide=guide).delete()
    for item in ITEMS:
        GuideItem.objects.create(
            guide=guide,
            product=None,
            position=item['position'],
            name=item['name'],
            description=item['description'],
            image=create_item_image(item['slug'], item['name']),
            amazon_link=item.get('amazon'),
            mercadolivre_link=item.get('ml'),
            shopee_link=item.get('shopee'),
            aliexpress_link=None,
            kabum_link=None,
            pros=item['pros'],
            cons=item['cons'],
        )

    print('Guia criado/atualizado:')
    print(f'  URL (local): http://127.0.0.1:8000/guia/{guide.slug}/')
    print(f'  Itens: {guide.items.count()}')
    print(f'  Imagem principal: {guide.main_image.name}')


if __name__ == '__main__':
    main()