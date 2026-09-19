"""Cria o review do Mchose V9 Pro (produto + artigo) no banco local.

Uso:
    python create_mchose_review.py

Depois rode `python export_content.py` para atualizar content_backup/.
"""

import os
import sys
import django

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from django.contrib.auth.models import User
from reviews.models import Category, Product, Review

BRAND = 'Mchose'
MODEL = 'V9 Pro'
SLUG = 'mchose-v9-pro'
TITLE = 'Mchose V9 Pro: o headset custo-benefício que parece muito mais caro'
ALIEXPRESS = 'https://s.click.aliexpress.com/e/_c4o3jANb'

CONTENT = """
<h2>O achado silencioso que está todo mundo usando</h2>
<p>Sabe aquela sensação horrível de estar perdendo algo incrível? Enquanto muita gente gasta fortunas em equipamentos de áudio, existe uma galera silenciosa que descobriu um headset absurdamente bom e barato — o <strong>Mchose V9 Pro</strong>. Hoje eu vou te mostrar por que ele é esse achado e por que vale a pena correr antes que o preço suba.</p>

<h2>Construção e design: visual de headset de R$ 800</h2>
<p>Começando direto e reto pela construção e pelo design. Ele lembra muito o <strong>Logitech G Pro</strong>, ou seja, remete a headsets bem mais caros do que o que ele realmente custa hoje: você encontra ele na faixa de <strong>R$ 250 a R$ 350 importando</strong> (já contando impostos e frete) ou entre <strong>R$ 400 e R$ 450 no mercado nacional</strong>.</p>
<p>A haste é de <strong>alumínio reforçado</strong>, com cerca de 3 cm de ajuste de altura, e a envergadura é excelente: ele não faz muita pressão e dá para usar com óculos tranquilamente. A headband tem costuras detalhadas e o logo da Mchose. Tudo muito bem construído e bonito.</p>
<p>As earpads são <strong>over-ear de courino</strong>, criando uma vedação passiva impressionante. Só de colocar na cabeça ele já abafa o som externo muito bem: com o volume em 50%, barulho de ventilador ou da limpeza de casa praticamente somem. Um detalhe: a concha é levemente justa — se você for um pouco "orelhudo", ele fica quase on-ear, mas nada que tire o mérito. Sobre a durabilidade do courino, com bons cuidados ele deve durar de 1 a 2 anos antes de precisar trocar.</p>

<h2>Bateria e carregamento inteligente</h2>
<p>Na parte externa ele tem o botão de power (que alterna entre Bluetooth e Wi-Fi), botão de mute e potenciômetro de volume. Ele entrega cerca de <strong>250 horas de bateria</strong> e o carregamento via <strong>USB-C</strong> é bem inteligente: diferente de outros modelos, você consegue usar e mexer nos botões enquanto carrega, seja no computador ou num power bank.</p>
<p>Por segurança e longevidade da bateria, eu recomendo carregar durante o uso só em emergências (entrevista de emprego, reunião importante). No mais, é bom saber que a opção existe.</p>

<h2>Um bônus enorme de usabilidade: o dongle reversível</h2>
<p>O adaptador Wi-Fi dele é um diferencial gigante: o dongle em geral é <strong>USB-A</strong>, mas você desencaixa uma pecinha e ele vira <strong>USB-C</strong>. Se você tem um notebook que só tem entradas USB-C, está resolvido. E eu sempre recomendo usar o <strong>modo Wi-Fi em vez do Bluetooth</strong> para não perder qualidade de áudio — o Bluetooth ainda gasta um pouco mais de bateria.</p>

<h2>Software: muito, muito, muito recheado</h2>
<p>A Mchose caprichou demais no software do V9 Pro. Você vê a bateria restante e, na captação de áudio, tem:
<ul>
<li><strong>Redução de ruído por IA</strong>;</li>
<li><strong>Magic Sound</strong>, para alterar a voz diretamente;</li>
<li><strong>Volume inteligente</strong>, que ajusta o volume ideal para o tipo de conteúdo — ótimo para filmes, onde a voz às vezes fica baixa e a explosão alta.</li>
</ul></p>
<p>O áudio padrão já é muito bom. Mas no <strong>equalizador</strong> a brincadeira fica séria: nos presets de música, o destaque absoluto vai para o <strong>heavy metal</strong> — os graves ficam tão potentes que as conchas vibram na cabeça, parecendo um mini subwoofer. Para jogos, ele já vem com perfis pré-configurados para <strong>Valorant, CS, Apex, PUBG</strong> e vários outros, que realmente ajudam a identificar os adversários. Você ainda pode baixar configurações da nuvem de outros usuários para jogos como <strong>God of War</strong> e <strong>The Last of Us</strong>.</p>
<p>Também há funções que dão mais brilho ao áudio e deixam os graves mais aparentes, e modos de jogo que não fizeram muita diferença na minha experiência — pode ser que para você faça.</p>

<h2>O 7.1 virtual que realmente funciona</h2>
<p>Surpreendentemente, o 7.1 virtual dele funciona de verdade — enquanto a maioria dos headsets nessa faixa estraga completamente o áudio no 7.1, o V9 Pro faz diferente. Recomendo deixar o tamanho da sala em <strong>small</strong>/pequeno. Ele entrega imersão espacial real: você percebe se o som vem de cima, de baixo ou de trás.</p>

<h2>Volume e vedação: chega a ser demais</h2>
<p>O resultado final em todos os quesitos de saída de áudio é impressionante em relação ao custo-benefício. O que mais me impressiona é a altura de volume junto com a vedação passiva: em <strong>50%</strong> você já fica imerso e isolado, em <strong>70%</strong> totalmente imerso, e em <strong>100%</strong> eu não consigo usar de tão alto. Para quem gosta de som muito alto mesmo, ele atende com louvor.</p>

<h2>Microfone com nota 10</h2>
<p>O microfone do V9 Pro é o grande destaque. Em ambiente silencioso a captura é muito aceitável — acima da média. Ligando um <strong>ventilador gigante</strong> na minha direção com o filtro de ruído desligado, o captador pega bastante vento. Já com o <strong>filtro de antirruído ligado</strong>, a diferença é brincadeira: o ruído praticamente some. Simplesmente nota 10 na captura de áudio.</p>
<p>Outro ponto forte: mesmo colocando o áudio das conchas em 100%, vaza quase nada para o microfone. É raro ver isso nessa faixa de preço.</p>

<h2>Pontos negativos</h2>
<p>Comparado a outros headsets nessa faixa, ele deixa a desejar um pouco nos <strong>graves</strong> frente a alguns modelos (só nesse quesito na saída de áudio). E ele <strong>não tem RGB</strong> — apenas o microfone tem luz para sinalizar se está mutado ou não. Se você faz questão de headset iluminado, isso pode pesar.</p>

<h2>Conclusão: é compra obrigatória?</h2>
<p>Na minha opinião, o Mchose V9 Pro é basicamente uma <strong>compra obrigatória</strong>, estando no meu top 3 de custo-benefício até R$ 400. Mas calma: ele não ganha em absolutamente tudo. O <strong>Redragon Zeus Pro</strong> é fisicamente muito mais robusto (um tanque de guerra) e no áudio estéreo puro empata ou fica ligeiramente à frente. O <strong>Havit H7 SE</strong> tem o trunfo de ser um achado muito barato no mercado nacional, com pads de tecido que muita gente prefere por não descascar.</p>
<p>Então por que o V9 Pro se destaca? Porque ele <strong>ganha de lavada no microfone</strong>, entrega um <strong>7.1 que realmente funciona</strong> (coisa que o Zeus erra) e dá uma <strong>surra de 10 a 0 no software</strong>, recheado de funções que nem Zeus nem Havit possuem.</p>
<p>Detalhe muito importante: comprei o meu <strong>importado direto da loja fabricante no AliExpress</strong>, e o AliExpress tem aquele adesivo antifalsificação no site. Fique muito atento e compre apenas de lojas confiáveis. Comprando pelo meu link de afiliado você apoia o trabalho do André Indica sem pagar nada a mais.</p>
"""


def create_placeholder_image():
    main_dir = os.path.join(settings.MEDIA_ROOT, 'reviews', 'main')
    os.makedirs(main_dir, exist_ok=True)
    path = os.path.join(main_dir, f'{SLUG}.webp')
    if os.path.exists(path):
        return f'reviews/main/{SLUG}.webp'
    img = Image.new('RGB', (1280, 720), '#0f172a')
    draw = ImageDraw.Draw(img)
    for y in range(720):
        draw.line([(0, y), (1280, y)], fill=(30, 41, 59 + int(y * 0.15)))
    try:
        font_title = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 56)
        font_sub = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 28)
    except OSError:
        font_title = ImageFont.load_default()
        font_sub = font_title
    t = 'Mchose V9 Pro'
    s = 'André Indica'
    bbox = draw.textbbox((0, 0), t, font=font_title)
    tw = bbox[2] - bbox[0]
    draw.text(((1280 - tw) / 2, 260), t, fill=(255, 255, 255), font=font_title)
    bbox = draw.textbbox((0, 0), s, font=font_sub)
    tw = bbox[2] - bbox[0]
    draw.text(((1280 - tw) / 2, 370), s, fill=(253, 186, 116), font=font_sub)
    img.save(path, format='WEBP', quality=80)
    return f'reviews/main/{SLUG}.webp'


def main():
    category, _ = Category.objects.get_or_create(name='Áudio')
    product, _ = Product.objects.get_or_create(
        brand=BRAND,
        name=MODEL,
        category=category,
    )
    author = User.objects.filter(username='admin').first() or User.objects.first()

    Review.objects.get_or_create(
        slug=SLUG,
        defaults={
            'product': product,
            'title': TITLE,
            'excerpt': 'Review completo do Mchose V9 Pro: headset de construção premium que parece muito mais caro do que é. De ~R$ 250 (importado) a ~R$ 450 (nacional), com 250h de bateria, 7.1 virtual que funciona e microfone nota 10.',
            'content': CONTENT,
            'conclusion': '\nO Mchose V9 Pro é uma compra obrigatória para quem quer um headset de construção premium por preço de entrada. Ele entrega vedação passiva impressionante, 250 horas de bateria, dongle USB-A/C, software absurdamente completo, 7.1 virtual que realmente funciona e um microfone com nota 10. Perde para Redragon Zeus Pro e Havit H7 SE apenas nos graves e no RGB. Pelo preço, está no meu top 3 de custo-benefício até R$ 400.',
            'main_image': create_placeholder_image(),
            'rating': 9.3,
            'pros': ('Custo-benefício absurdo: de ~R$ 250 (importado) a ~R$ 450 (nacional)\n'
                     'Construção premium: haste de alumínio reforçado e headband com costuras detalhadas\n'
                     'Vedação passiva impressionante (earpads over-ear de courino)\n'
                     '250 horas de bateria e carregamento USB-C inteligente (dá para usar carregando)\n'
                     'Dongle USB-A que vira USB-C, perfeito para notebooks\n'
                     'Software completo: equalizador, presets de jogos (Valorant, CS, Apex, PUBG) e perfis na nuvem\n'
                     '7.1 virtual que realmente funciona (tamanho small)\n'
                     'Microfone nota 10 com redução de ruído por IA\n'
                     'Volume altíssimo: imerso em 70%'),
            'cons': ('Graves um pouco atrás de rivais como o Redragon Zeus Pro na saída de áudio\n'
                     'Sem RGB (só o microfone tem luz de mute)\n'
                     'Earpads de courino descascam em 1 a 2 anos\n'
                     'Concha levemente justa para orelhas grandes'),
            'specifications': {
                'Conexão': '2.4GHz (Wi-Fi) / Bluetooth / USB-C',
                'Bateria': '~250 horas (Wi-Fi 2.4GHz), carregamento USB-C',
                'Haste': 'Alumínio reforçado, ~3 cm de ajuste',
                'Earpads': 'Over-ear, courino com vedação passiva',
                'Áudio': '7.1 virtual, equalizador com presets por gênero',
                'Microfone': 'Com redução de ruído por IA e magic sound',
                'Dongle': 'USB-A com adaptador USB-C acoplável',
                'Extras': 'Volume inteligente, presets na nuvem, modos de jogo',
            },
            'tags_input': 'mchose, v9 pro, headset, gamer, wireless, 7.1, custo benefício, 2026',
            'aliexpress_link': ALIEXPRESS,
            'author': author,
            'is_featured': True,
            'is_published': True,
        },
    )

    review = Review.objects.get(slug=SLUG)
    print('Review criado/atualizado:')
    print(f'  URL (local): http://127.0.0.1:8000/review/{review.slug}/')
    print(f'  Produto: {review.product.brand} {review.product.name}')
    print(f'  Nota: {review.rating}')
    print(f'  Imagem: {review.main_image.name}')


if __name__ == '__main__':
    main()