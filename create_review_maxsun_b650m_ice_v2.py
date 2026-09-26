"""
Cria o review: MAXSUN Challenger B650M WiFi ICE V2 (placa-mãe AM5 / B650 / mATX).

Uso:
    $env:SECRET_KEY="test"; $env:DEBUG="True"; python create_review_maxsun_b650m_ice_v2.py
    $env:SECRET_KEY="test"; $env:DEBUG="True"; python export_content.py

Specs conferidas na fonte oficial da Maxsun (maxsun.com) e no PDF oficial
de especificações. Nenhum valor foi estimado.

lembre: troque a imagem placeholder pela foto real do produto.
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
from reviews.models import Category, Product, Review  # noqa: E402

BRAND = 'Maxsun'
MODEL = 'Challenger B650M WiFi Ice V2'
SLUG = 'maxsun-challenger-b650m-wifi-ice-v2'
# MPN/código do fabricante. Vai para o JSON-LD como sku/mpn para que
# buscadores e IAs resolvam a entidade do produto.
SKU = 'MS-CHA-B650MWIFIICEV2'

TITLE = 'Maxsun Challenger B650M WiFi Ice V2: review da placa-mãe AM5 branca e barata'

# Link de afiliado enxuto: mantém o identificador de afiliado
# (utm_medium=affiliates + utm_source), descarta os parâmetros de sessão
# (gads_t_sig, mmp_pid, uls_trackid) que só poluem e estouram o
# URLField(max_length=500).
SHOPEE = (
    'https://shopee.com.br/'
    'Placa-M%C3%A3e-Maxsun-Challenger-B650M-WiFi-Ice-V2-Chipset-B650-AMD-AM5-mATX-DDR5-i.'
    '1552226494.58261833810'
    '?utm_medium=affiliates&utm_source=an_18339371295'
)

EXCERPT = (
    'Análise da Maxsun Challenger B650M WiFi Ice V2, placa-mãe AM5 branca em mATX com '
    'chipset B650, VRM 6+2+1 e WiFi integrado. Bom custo-benefício para Ryzen 5 e 7, '
    'mas com limitações reais: WiFi 5 com Bluetooth 4.2 e apenas um slot M.2.'
)

CONTENT = """
<p>A Maxsun Challenger B650M WiFi Ice V2 é uma placa-mãe de entrada que resolve um
problema específico muito bem: montar um PC AM5 branco, compacto e barato sem
renunciar ao chipset B650 e ao WiFi integrado. Fora desse nicho, as duas
concessões da placa (um slot M.2 e um módulo WiFi de 2019) pesam.</p>

<h2>Resumo rápido: para quem serve</h2>
<p>Se você busca <strong>Ryzen 5 7500F, 7600 ou Ryzen 7 7700/7800X3D</strong> em um
gabinete mATX branco, com WiFi integrado e sem estourar o orçamento, ela faz
sentido. Se você quer dois SSDs, WiFi 6 ou suporte a um Ryzen 9 de alto consumo,
procure outra.</p>

<h2>Especificações técnicas</h2>
<p>Estrutura resumida. A ficha completa, com 24 campos, fica na lateral direita
do review.</p>
<table>
  <thead><tr><th>Especifica\u00e7\u00e3o</th><th>Detalhe</th></tr></thead>
  <tbody>
    <tr><td>Chipset</td><td>AMD B650</td></tr>
    <tr><td>Socket</td><td>AM5 (LGA1718)</td></tr>
    <tr><td>Formato</td><td>mATX (245 \u00d7 210 mm)</td></tr>
    <tr><td>Processadores</td><td>AMD Ryzen 7000 e 8000</td></tr>
    <tr><td>VRM</td><td>6+2+1 fases, Dr.MOS de 50A, TDP de 155W</td></tr>
    <tr><td>Mem\u00f3ria</td><td>2 slots DDR5, at\u00e9 64GB, 4800/5200 MHz + EXPO/XMP</td></tr>
    <tr><td>Expans\u00e3o</td><td>1\u00d7 PCIe 4.0 x16, 1\u00d7 PCIe 3.0 x1</td></tr>
    <tr><td>Armazenamento</td><td>1\u00d7 M.2 PCIe 4.0 x4, 3\u00d7 SATA 6Gb/s</td></tr>
    <tr><td>Rede</td><td>1\u00d7 RJ45 Gigabit + WiFi 5 (Realtek RTL8821CE)</td></tr>
    <tr><td>Bluetooth</td><td>4.2</td></tr>
  </tbody>
</table>

<h2>O que o chipset B650 entrega (e o que não entrega)</h2>
<p>O B650 é o chipset intermediário da linha AM5. Ele cobre o essencial: suporte a
Ryzen 7000 e 8000, PCIe 4.0 na placa de vídeo e no M.2, e update de BIOS por
Q-Flash. O que ele <em>não</em> traz é PCIe 5.0 para GPU ou SSD — recurso do B650E
e do X670E. Na prática, para uma placa em mATX e nessa faixa de preço, perder o
Gen5 quase sempre não pesa, porque a diferença só aparece com hardware de nova
geração que ainda é caro.</p>

<h2>VRM: dá conta do Ryzen 5 e do Ryzen 7, não do 7950X</h2>
<p>O sistema de alimentação é de 6+2+1 fases com Dr.MOS de 50A. É dimensionado para o TDP de 155W, o que cobre com folga o Ryzen 5
7500F, o 7600 e o Ryzen 7 7700. O 7800X3D também roda bem, porque o X3D tem
consumo parecido com o 7700X.</p>
<p>Já processadores como Ryzen 9 7900X, 7950X e 7950X3D têm PPT de até 230W e
vão forçar a placa no limite, com mais temperatura e possível throttling. Não é
que não funcione — é que você estaria gastando em uma CPU cara sobre a
estrutura de alimentação mais barata do conjunto.</p>

<h2>Memória: 2 slots, e isso é uma limitação real</h2>
<p>A placa tem apenas <strong>dois slots DIMM</strong>, o que limita a capacidade
a 64GB na especificação oficial. Não existe caminho para quatro pentes.</p>
<p>Há um lado positivo que a maioria ignora: com dois módulos a planilha de memória
fica mais simples, o que <em>ajuda</em> a alcançar a frequência ideal do AM5. O
ponto ótimo do Ryzen 5000/7000 é <strong>DDR5-6000 CL30 com EXPO</strong>, e dois
pentes desse perfil atingem esse patamar com mais facilidade do que quatro. Se
você não pretende passar de 32GB, a falta dos slots extras quase não aparece.</p>

<h2>Armazenamento: o ponto fraco mais visível</h2>
<p>Existe <strong>um único slot M.2</strong>. Isso é o que mais vai incomodar
quem monta um PC para games e trabalho ao mesmo tempo: o sistema vai no NVMe e,
se quiser um segundo armazenamento, precisa ocupar um dos três portas SATA, o
que significa perder a BENEFÍCIO de banda do NVMe.</p>
<p>Para um PC de jogo com um SSD, é suficiente. Para quem guarda biblioteca de
jogos ou trabalha com vídeo, é um limite que define a compra.</p>

<h2>WiFi e Bluetooth: a concessão mais séria</h2>
<p>Este é o ponto que exige atenção. A placa traz o módulo <strong>Realtek
RTL8821CE</strong>, que oferece:</p>
<ul>
  <li>WiFi 5 (802.11ac) a até 866 Mbps na faixa de 5 GHz</li>
  <li><strong>Bluetooth 4.2</strong></li>
</ul>
<p>Para navegar, é suficiente. Para periféricos, não é. O principal: o Bluetooth
4.2 é uma versão de 2019. Periféricos modernos que pedem BT 5.0 ou 5.3 —
fones com baixa latência, mouses sem fio, teclados — vão operar com codecs
antigos e, em alguns casos, parear sem os recursos de LE Audio. E o módulo usa
slot M.2 Key-M sem suporte a Intel CNVi, ou seja, a troca exigiria um
adaptador específico.</p>
<p>Se o seu plano é usar headset Bluetooth no PC, leve isso em conta. Para
teclado e mouse com dongle USB 2.4 GHz, não faz diferença nenhuma.</p>

<h2>Acabamento: o "Ice" é o diferencial de verdade</h2>
<p>A diferença entre esta e a Maxsun Challenger B650M WiFi V2 (sem "Ice") é
visual. A Ice V2 troca os dissipadores pretos por uma blindagem prata/branca,
com o conjunto pensado para combinar com gabinete e memoria branca. Se o seu
gabinete é branco, a V2 simples entrega o mesmo desempenho por menos dinheiro;
se a estética importa, a Ice V2 é a versão correta.</p>

<h2>Para quem é, para quem não é</h2>
<h3>Compre se você...</h3>
<ul>
  <li>Montar um PC AM5 branco e compacto (mATX)</li>
  <li>Usar Ryzen 5 7500F, 7600 ou Ryzen 7 7700/7800X3D</li>
  <li>Querer WiFi integrado sem comprar adaptador à parte</li>
  <li>Aceita trabalhar com um único SSD NVMe</li>
  <li>Precisa de EXPO/XMP para subir a memória a 6000 MT/s</li>
</ul>
<h3>Não compre se você...</h3>
<ul>
  <li>Quer dois ou mais SSDs NVMe</li>
  <li>Usa periféricos Bluetooth 5.x e depende de baixa latência</li>
  <li>Planeja um Ryzen 9 de alto PPT (7900X, 7950X, 7950X3D)</li>
  <li>Precisa de rede 2.5GbE ou WiFi 6/6E</li>
  <li>Precisa de mais de 32GB de RAM em quatro pentes</li>
</ul>

<h2>Alternativas a considerar</h2>
<p>Se o ponto fraco for o número de slots M.2, placas como a <strong>MSI PRO
B650M-P WiFi</strong> e a <strong>ASRock B650M Pro RS WiFi</strong> entregam dois
slots M.2 e WiFi 6 por uma faixa de preço parecida, e costumam ser escolhas mais
seguras a longo prazo. Se o orçamento for o critério principal e o gabinete não
precisar ser branco, a Maxsun Challenger B650M WiFi V2 (sem "Ice") entrega
praticamente a mesma placa por menos dinheiro.</p>

<h2>Conclusão</h2>
<p>A Maxsun Challenger B650M WiFi Ice V2 é uma placa honesta: faz bem o que
propõe e não esconde as limitações. Entrega B650, WiFi integrado e acabamento
branco em mATX, com VRM suficiente para Ryzen 5 e 7 e espaço de sobra para
o Ryzen 7 X3D.</p>
<p>Os dois limites — um único slot M.2 e um módulo WiFi com Bluetooth 4.2 — são
irreversíveis e definem para quem ela serve. Quem monta jogo com um SSD e
navega por cabo ou por adaptador de Bluetooth 5, tem um conjunto coerente e barato.
Quem precisa de dois NVMe ou de periféricos Bluetooth modernos deve gastar um
pouco mais e escolher uma B650M com dois slots M.2 e WiFi 6.</p>
"""

CONCLUSION = """
<p><strong>Nota 7,2/10.</strong> Uma placa de entrada bem resolvida para o nicho
que atende: AM5 branco, mATX, B650 e WiFi integrado sem funções desnecessárias.</p>
<p>Fica abaixo da média da categoria em dois pontos objetivos: apenas um slot
M.2 e WiFi 5 com Bluetooth 4.2. Nenhum dos dois é erro da placa, é o
orçamento do segmento. Fora isso, VRM à altura para Ryzen 5 e 7, três SATA,
EXPO liberado e acabamento branco consistente.</p>
<p>Se você já sabe que precisa de um SSD só e não depende de Bluetooth 5, ela
cumpre o que promete. Se alguma dessas duas condições não se aplica, a economia
de R$ 100 ou R$ 200 não compensa o retrabalho.</p>
"""

PROS = (
    "Chipset B650 com suporte a Ryzen 7000 e 8000\n"
    "WiFi integrado, dispensa adaptador avulso\n"
    "VRM 6+2+1 com Dr.MOS de 50A aguenta Ryzen 5 e 7 com folga\n"
    "Suporte a EXPO/XMP para levar a DDR5 a 6000 MT/s\n"
    "Formato mATX e blindagem branca, rara nessa faixa de preço\n"
    "Três portas SATA e header ARGB para a placa"
)

CONS = (
    "Apenas um slot M.2 — um único SSD NVMe\n"
    "WiFi 5 (802.11ac) com Bluetooth 4.2, defasado para 2026\n"
    "Somente 2 slots de memória, sem caminho para 4 pentes\n"
    "Sem PCIe 5.0 para GPU ou SSD\n"
    "Rede Gigabit Ethernet, sem 2.5GbE\n"
    "Codec de áudio ALC897, básico para fone de alta fideli"
)

SPECIFICATIONS = {
    'Marca': 'Maxsun',
    'Modelo': 'Challenger B650M WiFi Ice V2',
    'Código do fabricante': SKU,
    'Chipset': 'AMD B650',
    'Socket': 'AM5 (LGA1718)',
    'Formato': 'mATX (245 × 210 mm)',
    'Processadores suportados': 'AMD Ryzen 7000 e 8000',
    'VRM': '6+2+1 fases, Dr.MOS 50A, TDP 155W',
    'Memória': '2 slots DDR5, dual channel, até 64 GB',
    'Frequência de memória': '4800 / 5200 MHz + EXPO e XMP',
    'Slot de vídeo': '1× PCIe 4.0 x16',
    'Slots de expansão': '1× PCIe 4.0 x16, 1× PCIe 3.0 x1',
    'Armazenamento': '1× M.2 PCIe 4.0 x4 (2242/2280)',
    'SATA': '3× SATA 6Gb/s',
    'Rede cabeada': 'Realtek RTL8111H Gigabit (1 Gbps)',
    'WiFi': 'Realtek RTL8821CE, 802.11ac, até 866 Mbps',
    'Bluetooth': '4.2',
    'Áudio': 'Realtek ALC897, 5.1 canais',
    'Saída de vídeo': '1× HDMI e 1× DisplayPort, até 2560×1440 @60Hz',
    'USB traseiro': '4× USB 3.2 Gen1 e 2× USB 2.0',
    'Alimentação': '24-pin ATX + 8-pin EPS',
    'Headers de cooler': '1× CPU_FAN, 2× SYS_FAN',
    'Iluminação': '1× 12V RGB, 2× 5V ARGB',
    'Garantia': '3 anos',
}

FAQ = [
    {
        'question': 'A Maxsun Challenger B650M WiFi Ice V2 é boa para o Ryzen 7 7800X3D?',
        'answer': (
            'Sim. O 7800X3D tem consumo de energia parecido com o 7700X, dentro do '
            'limite de 155W que o VRM 6+2+1 com Dr.MOS de 50A foi dimensionado para '
            'atender. Com um par de memórias DDR5 em perfil EXPO, o conjunto roda com '
            'margem térmica confortável.'
        ),
    },
    {
        'question': 'Quantos slots M.2 essa placa-mãe tem?',
        'answer': (
            'Apenas um slot M.2 PCIe 4.0 x4, que aceita SSDs de 2242 ou 2280. Para um '
            'segundo disco, é preciso usar uma das três portas SATA 6Gb/s, o que '
            'significa abrir mão da velocidade do NVMe.'
        ),
    },
    {
        'question': 'Essa placa tem WiFi 6?',
        'answer': (
            'Não. O módulo integrado é o Realtek RTL8821CE, que oferece WiFi 5 '
            '(802.11ac) a até 866 Mbps na faixa de 5 GHz. Não há suporte a WiFi 6 nem '
            'WiFi 6E. Para internet a cabo, acima de 300 Mbps, isso não faz diferença; '
            'para redes WiFi 6, faz.'
        ),
    },
    {
        'question': 'Qual o Bluetooth dessa placa?',
        'answer': (
            'Bluetooth 4.2, pela limitação do próprio módulo RTL8821CE. Periféricos que '
            'exigem Bluetooth 5.0 ou superior — fones com baixa latência, mouses e '
            'teclados modernos — funcionam, mas sem os recursos de LE Audio e com os '
            'codecs antigos. Teclado e mouse com receptor USB 2.4 GHz não são afetados.'
        ),
    },
    {
        'question': 'Posso usar um Ryzen 9 7950X ou 7950X3D nela?',
        'answer': (
            'Tecnicamente liga e funciona, mas não é recomendado. Esses processadores '
            'têm PPT de até 230W, acima dos 155W que o VRM da placa foi projetado para '
            'entregar. O resultado é temperatura mais alta no VRM e risco de throttling. '
            'O certo nessa faixa é uma placa B650 com VRM mais robusto, como as da MSI '
            'PRO ou ASRock com Dissipação de 10 a 12 fases.'
        ),
    },
    {
        'question': 'Qual a diferença entre a B650M WiFi Ice V2 e a B650M WiFi V2?',
        'answer': (
            'A diferença é o acabamento. A Ice V2 usa blindagem e dissipadores prata e '
            'brancos, pensados para montar um PC branco. A B650M WiFi V2, sem "Ice", tem '
            'os mesmos componentes funcionais em preto. Desempenho idêntico; a Ice V2 '
            'custa um pouco mais e é a escolha certa se o gabinete for branco.'
        ),
    },
    {
        'question': 'Quantos slots de memória DDR5 ela tem?',
        'answer': (
            'Dois slots DIMM, em dual channel, com suporte oficial a até 64 GB. Não há '
            'como usar quatro módulos. A boa notícia é que dois pentes facilitam atingir '
            'a frequência ideal do AM5: DDR5-6000 CL30 com perfil EXPO é o ponto ótimo '
            'para Ryzen 5000 e 7000.'
        ),
    },
    {
        'question': 'Preciso de placa de vídeo para usar essa placa-mãe?',
        'answer': (
            'Depende do processador. O Ryzen 5 7500F não tem vídeo integrado, então exige '
            'placa de vídeo. O Ryzen 5 7600 e o Ryzen 7 7700 têm Radeon Vega integrado e '
            'duram saídas na placa: HDMI e DisplayPort, ambos até 2560×1440 a 60Hz. Com '
            'CPU sem vídeo integrado, as saídas da placa não funcionam.'
        ),
    },
    {
        'question': 'Qual é o preço da Maxsun Challenger B650M WiFi Ice V2?',
        'answer': (
            'O preço varia bastante conforme o vendedor e a região, e a Shopee concentra '
            'a oferta mais barata. Como a faixa é de entrada do segmento B650 mATX, ela '
            'fica abaixo de placas equivalentes com dois slots M.2 e WiFi 6. Confira o '
            'valor atual nos links desta página antes de decidir, porque a diferença de '
            'preço em relação a essas alternativas muda a conta.'
        ),
    },
    {
        'question': 'Vale a pena comprar a Maxsun Challenger B650M WiFi Ice V2?',
        'answer': (
            'Vale se o seu cenário for Ryzen 5 ou 7, um único SSD, gabinete branco e '
            'WiFi integrado sem gastar à parte. Não vale se você precisa de dois slots '
            'M.2, usa periféricos Bluetooth 5.x ou planeja um Ryzen 9. Nesse segundo '
            'caso, modelos como a MSI PRO B650M-P WiFi ou a ASRock B650M Pro RS WiFi '
            'custam pouco mais e resolvem essas limitações.'
        ),
    },
]


def create_main_image():
    main_dir = os.path.join(settings.MEDIA_ROOT, 'reviews', 'main')
    os.makedirs(main_dir, exist_ok=True)
    path = os.path.join(main_dir, f'{SLUG}.webp')
    if os.path.exists(path):
        return f'reviews/main/{SLUG}.webp'

    width, height = 1280, 720
    img = Image.new('RGB', (width, height), '#0b1220')
    draw = ImageDraw.Draw(img)

    # Fundo em diagonal com leve tom prateado, remetendo ao "Ice".
    for y in range(height):
        ratio = y / height
        draw.line(
            [(0, y), (width, y)],
            fill=(11, 18, 32),
        )
        if ratio > 0.55:
            overlay = int((ratio - 0.55) * 90)
            draw.line(
                [(0, y), (width, y)],
                fill=(11 + overlay, 18 + overlay, 32 + overlay),
            )

    # Barra lateral prateada, seguindo o padrão visual dos demais placeholders.
    draw.rectangle([(0, 0), (int(width * 0.03), height)], fill=(198, 205, 215))

    # Silhueta estilizada de uma placa mATX.
    px0, py0, px1, py1 = 150, 190, 470, 540
    draw.rectangle([(px0, py0), (px1, py1)], fill=(24, 32, 48), outline=(120, 132, 150), width=2)
    draw.rectangle([(px0 + 18, py0 + 18), (px0 + 150, py0 + 74)], fill=(48, 58, 76))
    draw.rectangle([(px0 + 20, py0 + 110), (px1 - 20, py0 + 132)], fill=(60, 70, 88))
    draw.rectangle([(px0 + 20, py0 + 150), (px1 - 60, py0 + 172)], fill=(60, 70, 88))
    for i in range(3):
        draw.rectangle(
            [(px0 + 20 + i * 46, py1 - 60), (px0 + 56 + i * 46, py1 - 20)],
            fill=(70, 80, 98),
        )

    try:
        font_title = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 46)
        font_sub = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 27)
        font_brand = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 24)
    except OSError:
        font_title = font_sub = font_brand = ImageFont.load_default()

    def draw_right(text, y, font, fill):
        bbox = draw.textbbox((0, 0), text, font=font)
        draw.text(((width - (bbox[2] - bbox[0])) / 2, y), text, fill=fill, font=font)

    draw_right('Maxsun Challenger', 215, font_title, (245, 247, 250))
    draw_right('B650M WiFi Ice V2', 275, font_title, (245, 247, 250))
    draw_right('AMD B650 · AM5 · mATX · DDR5', 350, font_sub, (198, 205, 215))
    draw_right('Review · André Indica', 560, font_brand, (150, 160, 175))

    img.save(path, format='WEBP', quality=82)
    return f'reviews/main/{SLUG}.webp'


def main():
    category, _ = Category.objects.get_or_create(
        slug='placas-mae',
        defaults={'name': 'Placas Mãe', 'icon': 'icon-cpu'},
    )
    product, _ = Product.objects.get_or_create(
        brand=BRAND,
        name=MODEL,
        defaults={'category': category, 'model_name': MODEL},
    )
    if product.category_id != category.id:
        product.category = category
        product.save()

    author = User.objects.filter(username='admin').first() or User.objects.first()

    assert len(SHOPEE) <= 500, f'Link Shopee excede URLField(500): {len(SHOPEE)}'

    review, created = Review.objects.get_or_create(
        slug=SLUG,
        defaults={
            'product': product,
            'title': TITLE,
            'excerpt': EXCERPT,
            'content': CONTENT.strip(),
            'conclusion': CONCLUSION.strip(),
            'main_image': create_main_image(),
            'rating': 7.2,
            'pros': PROS,
            'cons': CONS,
            'specifications': SPECIFICATIONS,
            'tags_input': 'placa-mae, am5, b650, ddr5, matx, pcinformatica',
            'sku': SKU,
            'faq': FAQ,
            'shopee_link': SHOPEE,
            'author': author,
            'is_featured': False,
            'is_published': True,
        },
    )

    if not created:
        review.product = product
        review.title = TITLE
        review.excerpt = EXCERPT
        review.content = CONTENT.strip()
        review.conclusion = CONCLUSION.strip()
        review.rating = 7.2
        review.pros = PROS
        review.cons = CONS
        review.specifications = SPECIFICATIONS
        review.tags_input = 'placa-mae, am5, b650, ddr5, matx, pcinformatica'
        review.sku = SKU
        review.faq = FAQ
        review.shopee_link = SHOPEE
        review.author = author
        review.is_published = True
        review.save()

    print(f'  Imagem principal: {review.main_image}')
    print(f'  URL             : https://andreindicatech.com.br{review.get_absolute_url()}')
    print(f'  SKU / MPN       : {review.sku}')
    print(f'  Nota            : {review.rating}')
    print(f'  Especificações  : {len(review.parsed_specs)} linhas')
    print(f'  FAQ             : {len(review.faq_items)} perguntas')
    print(f'  Specs (pro/contra): {len(review.pros.splitlines())} / {len(review.cons.splitlines())}')
    print('  (lembre: troque a imagem placeholder pela foto real do produto)')


if __name__ == '__main__':
    main()
