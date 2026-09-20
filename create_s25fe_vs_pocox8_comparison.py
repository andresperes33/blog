"""Cria o comparativo completo Samsung Galaxy S25 FE vs Poco X8 Pro Max no banco local.

Uso:
    $env:SECRET_KEY="test"; $env:DEBUG="True"; python create_s25fe_vs_pocox8_comparison.py
    $env:SECRET_KEY="test"; $env:DEBUG="True"; python export_content.py
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
from reviews.models import Category, Product, Comparison

SLUG = 'samsung-galaxy-s25-fe-vs-poco-x8-pro-max'
TITLE = 'Samsung Galaxy S25 FE vs Poco X8 Pro Max: Qual Vale Mais a Pena em 2026?'

SHOPEE_LINK = 'https://s.shopee.com.br/3qNFqH9Izq'
AMAZON_LINK = 'https://link.amazon/B0gbJ5R5K'

EXCERPT = (
    'Comparativo completo entre Samsung Galaxy S25 FE e Poco X8 Pro Max: '
    'bateria colossal de 8.500 mAh vs 4.900 mAh, Dimensity 9500s vs Exynos 2400 no AnTuTu, '
    'câmeras com zoom óptico de 3x, tela AMOLED 1.5K de 3.500 nits, 7 anos de updates e qual comprar em 2026.'
)

CONTENT = """
<h2>Bateria de 8.500 mAh vs 4.900 mAh: O embate dos intermediários premium</h2>
<p>Se você está em busca de um smartphone potente sem precisar pagar o preço de um ultra topo de linha de R$ 7.000 ou R$ 8.000, 2026 trouxe dois dos aparelhos mais comentados e disputados do mercado: o <strong>Samsung Galaxy S25 FE</strong> e o recém-chegado <strong>Poco X8 Pro Max</strong>.</p>
<p>De um lado, a Xiaomi chocou o mercado ao equipar o Poco com uma monstruosa <strong>bateria de 8.500 mAh</strong> de silício-carbono, processador com mais de 2,7 milhões de pontos no AnTuTu e carregador de 100 W já na caixa. Do outro lado, o Galaxy S25 FE responde com o refinamento tradicional da linha Galaxy: suporte a <strong>carregamento sem fio</strong>, câmera telefoto com <strong>zoom óptico real de 3x</strong>, gravação de vídeo profissional em 4K60 na frontal e nada menos que <strong>7 anos de atualizações de software garantidas</strong>.</p>
<p>Colocamos os dois aparelhos lado a lado, testamos todos os recursos de cabo a rabo e analisamos o conjunto da obra para revelar qual deles entrega o melhor investimento para o seu perfil e o seu bolso.</p>

<h2>Bateria e carregamento: O Poco humilha ou a Samsung compensa?</h2>
<p>O primeiro ponto que chama a atenção — e talvez a maior disparidade de todo o comparativo — está na capacidade energética. O Poco X8 Pro Max vem com uma impressionante bateria de <strong>8.500 mAh de silício-carbono</strong> contra <strong>4.900 mAh</strong> do Galaxy S25 FE. Estamos falando de uma diferença bruta de <strong>3.600 mAh</strong> a favor do modelo da Xiaomi.</p>
<p>Na prática do dia a dia, isso muda completamente a experiência:</p>
<ul>
    <li><strong>Poco X8 Pro Max:</strong> Foi projetado para aguentar tranquilamente <strong>dois dias inteiros de uso moderado</strong> longe da tomada. Mesmo para quem joga ou consome muito vídeo em alta taxa de quadros, passar de 24 a 30 horas de autonomia é algo comum.</li>
    <li><strong>Galaxy S25 FE:</strong> Entrega um dia completo de uso convencional (em torno de 6 a 7 horas de tela ativa). Se você tiver um uso mais intenso com GPS e câmera, precisará de uma carga ao final da tarde ou começo da noite.</li>
</ul>
<p>No carregamento, a história se repete na velocidade: o Poco já inclui na embalagem um <strong>carregador ultrarrápido de 100 W</strong>, capaz de levar a gigante bateria de 8.500 mAh de <strong>0% a mais de 60% em cerca de 30 minutos</strong>. Já a Samsung envia na caixa um carregador básico de 25 W — o aparelho suporta até 45 W com fio, mas exige a compra de um carregador mais potente à parte.</p>
<p>Onde o Galaxy S25 FE dá o troco? No <strong>carregamento sem fio (wireless charging de 15 W)</strong> e no carregamento reverso para alimentar seus fones de ouvido ou smartwatch nas costas do celular. O Poco não possui bobina de indução. Se você faz questão de colocar o celular na base sem fio da mesa ou do carro, o Samsung é o único com suporte aqui.</p>

<h2>Tela e experiência visual: 3.500 nits contra tecnologia LTPO</h2>
<p>Ambos os smartphones trazem telas de respeito, mas cada marca priorizou virtudes distintas:</p>
<ul>
    <li><strong>Poco X8 Pro Max:</strong> Painel <strong>AMOLED de 6,83 polegadas</strong> com resolução <strong>1,5K (2712 x 1220 pixels)</strong>, taxa de atualização de 120 Hz e um brilho de pico impressionante de <strong>3.500 nits</strong>. Suas bordas frontais são ultrafinas e quase perfeitamente simétricas, gerando uma imersão espetacular para assistir vídeos e jogar sob luz solar direta.</li>
    <li><strong>Samsung Galaxy S25 FE:</strong> Painel <strong>Dynamic AMOLED 2X de 6,7 polegadas</strong> com resolução Full HD+, taxa de atualização de 120 Hz e brilho de pico de 1.900 nits. O grande diferencial técnico é a presença da tecnologia <strong>LTPO variável (1 Hz a 120 Hz)</strong>, que reduz a taxa para 1 Hz ao exibir fotos ou textos estáticos, economizando preciosa energia.</li>
</ul>
<p>Em fidelidade cromática, a Samsung ainda mantém uma calibração mais natural e precisa no modo padrão, além de ângulos de visão exemplares. No entanto, no conjunto da obra, a tela do Poco enche mais os olhos pelo brilho explosivo, pela resolução 1.5K mais definida e pelas bordas visivelmente mais finas.</p>

<h2>Desempenho e jogos: O monstro Dimensity 9500s de 2,7M no AnTuTu</h2>
<p>Para quem busca performance bruta, a disputa é quente. O Poco X8 Pro Max estreia o novo processador <strong>MediaTek Dimensity 9500s</strong> (fabricado em litografia de 4 nanômetros), enquanto o Galaxy S25 FE aposta no <strong>Samsung Exynos 2400</strong> (também de 4 nm).</p>
<p>Os números de benchmark mostram a vantagem clara do aparelho da Poco:</p>
<ul>
    <li><strong>Poco X8 Pro Max (AnTuTu v10):</strong> Mais de <strong>2.732.000 pontos</strong>.</li>
    <li><strong>Galaxy S25 FE (AnTuTu v10):</strong> Cerca de <strong>2.182.000 pontos</strong>.</li>
</ul>
<p>São mais de <strong>550 mil pontos de vantagem para o Poco</strong>. No uso diário convencional (WhatsApp, navegação, multitarefa e redes sociais), ambos são extremamente velozes, sem engasgos ou lentidões perceptíveis. Porém, ao abrir jogos pesadíssimos com gráficos no máximo (como Genshin Impact, Warzone Mobile ou emulação de consoles modernos), o Poco se destaca: ele sustenta taxas de quadros mais elevadas e estáveis por horas, graças ao seu sistema avançado de <strong>refrigeração líquida com câmara de vapor gigante</strong>, esquentando menos as mãos do que o Galaxy.</p>

<h2>Memória e armazenamento: A Xiaomi entrega mais na versão base</h2>
<p>Outro ponto em que o Poco X8 Pro Max sai na frente em custo-benefício é na configuração de memória de entrada:</p>
<ul>
    <li><strong>Poco X8 Pro Max:</strong> Já inicia na versão base com <strong>12 GB de memória RAM</strong> LPDDR5X (com tecnologia de expansão que adiciona mais 6 GB de RAM virtual) e <strong>256 GB de armazenamento interno UFS</strong>, havendo opções de até 16 GB de RAM e 512 GB.</li>
    <li><strong>Galaxy S25 FE:</strong> Inicia na versão base com <strong>8 GB de RAM</strong> e modestos <strong>128 GB de armazenamento</strong>, existindo variantes com 256 GB.</li>
</ul>
<p>Em 2026, com arquivos de vídeo 4K e jogos pesados ultrapassando facilmente 30 GB cada um, sair de fábrica com 256 GB e 12 GB de RAM pelo preço inicial é uma vantagem substancial para o Poco.</p>

<h2>Câmeras: A virada da Samsung com zoom óptico de 3x e vídeo 4K60</h2>
<p>Se em bateria e desempenho o Poco dominou, no departamento fotográfico a Samsung mostra por que a linha Galaxy é referência mundial de versatilidade e qualidade de imagem.</p>

<h3>Câmera principal de 50 MP (OIS)</h3>
<p>Ambos contam com sensores principais de <strong>50 megapixels com estabilização óptica (OIS)</strong>. Sob a luz do dia, ambos capturam fotos excelentes, com altíssimo nível de textura e grande alcance dinâmico (HDR). A assinatura é diferente: a Samsung satura um pouco mais as cores e reforça o contraste, entregando aquele visual pronto para postar nas redes sociais. O Poco oferece tons mais naturais e excelente balanço de brancos.</p>
<p>À noite, o sensor de grandes dimensões do Poco combinado ao processamento de imagem do Dimensity 9500s surpreende, registrando fotos muito claras com ruído controlado. O S25 FE também brilha no modo noturno, com excelente retenção de sombras.</p>

<h3>A lente telefoto com zoom óptico 3x: O abismo</h3>
<p>Aqui está o maior ponto fraco do Poco e o maior trunfo do Galaxy S25 FE:</p>
<ul>
    <li><strong>Galaxy S25 FE:</strong> Conta com uma câmera <strong>telefoto dedicada de 8 MP com zoom óptico real de 3x</strong> e zoom digital que alcança até 30x. O zoom óptico 3x preserva todos os detalhes em objetos distantes e proporciona um efeito retrato com compressão ótica de fundo lindíssimo e natural.</li>
    <li><strong>Poco X8 Pro Max:</strong> <em>Não possui câmera telefoto dedicada</em>. Todo o zoom é digital via recorte central do sensor principal de 50 MP até 10x. A partir de 2x ou 3x, a perda de textura e a granulação tornam-se bastante evidentes.</li>
</ul>

<h3>Câmera ultrawide e câmera frontal</h3>
<p>Na grande-angular (ultrawide), a Samsung também leva a melhor: o sensor de <strong>12 MP</strong> do S25 FE entrega bordas muito mais nítidas e um campo de visão mais amplo do que o sensor modesto de <strong>8 MP</strong> do Poco.</p>
<p>Nas selfies, o Poco conta com 20 MP e a Samsung com 12 MP com foco automático. De dia, as selfies do S25 FE exibem maior riqueza de poros e fidelidade no tom de pele. À noite, o Poco consegue iluminar ligeiramente melhor o rosto.</p>

<h3>Gravação de vídeo: Vitória maiúscula da Samsung</h3>
<p>Se você produz conteúdo para o Instagram, TikTok ou YouTube, a Samsung é imbatível:</p>
<ul>
    <li><strong>Galaxy S25 FE:</strong> Grava em até <strong>8K a 30 fps</strong> ou <strong>4K a 60 fps</strong> na traseira com estabilização primorosa, e grava em <strong>4K a 60 fps na câmera frontal</strong>.</li>
    <li><strong>Poco X8 Pro Max:</strong> Grava em 4K a 60 fps na traseira, mas na câmera frontal fica <strong>limitado a 1080p a 60 fps</strong>.</li>
</ul>
<p>Para criadores de conteúdo e vloggers, a ausência de 4K na câmera frontal do Poco pode ser um fator decisivo contra ele.</p>

<h2>Construção, durabilidade e recursos exclusivos</h2>
<p>Os dois smartphones têm acabamento refinado com <strong>traseira em vidro e laterais em metal (alumínio)</strong>. Porém, trazem comodidades exclusivas bem distintas:</p>
<ul>
    <li><strong>Poco X8 Pro Max:</strong> Traz certificação dupla <strong>IP68 e IP69</strong> — suportando não apenas submersão em água doce como também jatos de água em alta pressão e alta temperatura. Além disso, conta com o tradicional <strong>sensor infravermelho</strong> para controlar TVs e aparelhos de ar-condicionado, e um chamativo <strong>anel de LED</strong> ao redor das câmeras para sinalizar notificações e recarga.</li>
    <li><strong>Galaxy S25 FE:</strong> Traz certificação <strong>IP68</strong>, suporte completo ao <strong>Samsung DeX</strong> (conecte a um monitor ou TV via cabo ou sem fio e use o celular como se fosse um computador desktop com janelas e teclado) e todo o ecossistema de inteligência artificial <strong>Galaxy AI</strong> integrado ao sistema.</li>
</ul>
<p>No quesito áudio, ambos possuem alto-falantes estéreo com som alto e nítido, mas o Galaxy S25 FE apresenta uma curva acústica com graves mais presentes e médios mais encorpados.</p>

<h2>Software e longevidade: 7 anos contra 4 anos</h2>
<p>No sistema operacional, temos a One UI 8.5/9 da Samsung contra a HyperOS da Xiaomi, ambas baseadas no <strong>Android 15</strong>. A política de atualizações é um diferencial que não pode ser ignorado:</p>
<ul>
    <li><strong>Samsung Galaxy S25 FE:</strong> Promessa oficial de <strong>7 anos de atualizações de versão do Android e 7 anos de pacotes de segurança</strong>. É um aparelho que vai receber novidades até 2033.</li>
    <li><strong>Poco X8 Pro Max:</strong> Promessa de <strong>4 anos de atualizações de Android e 6 anos de segurança</strong>. Uma ótima marca para a Xiaomi, mas ainda abaixo do compromisso da Samsung.</li>
</ul>
"""

CONCLUSION = """
<p><strong>Veredito Final: Qual vale mais a pena comprar?</strong></p>
<p>A resposta depende diretamente das suas prioridades de uso no dia a dia:</p>
<ul>
    <li><strong>Escolha o Poco X8 Pro Max se:</strong> Seu foco principal é <strong>bateria absurda (8.500 mAh)</strong> para passar dois dias sem carregar, recarga de 100 W na caixa, <strong>desempenho monstruoso para jogos pesados</strong> (Dimensity 9500s com câmara de vapor gigante), tela gigantesca de 3.500 nits e <strong>mais memória RAM e armazenamento (12GB/256GB)</strong> pelo seu dinheiro. É o melhor celular gamer e multimídia da categoria.</li>
    <li><strong>Escolha o Samsung Galaxy S25 FE se:</strong> Você prioriza um conjunto completo de <strong>câmeras profissionais com zoom óptico real de 3x</strong>, gravação de vídeo em 4K60 na frontal para redes sociais, <strong>carregamento sem fio</strong>, ecossistema Galaxy AI, modo computador com <strong>Samsung DeX</strong> e a segurança de <strong>7 anos de atualizações garantidas</strong>. É o smartphone mais equilibrado, elegante e duradouro.</li>
</ul>
<p>Ambos são aparelhos fantásticos que representam o ápice do custo-benefício intermediário premium em 2026. Para conferir os melhores preços com desconto e entrega rápida e segura, utilize os links verificados abaixo:</p>
"""

SPECS_S25_FE = {
    'Tela': '6.7" Dynamic AMOLED 2X, FHD+, 1-120Hz LTPO, 1.900 nits',
    'Processador': 'Samsung Exynos 2400 (4nm Octa-Core)',
    'Pontuação AnTuTu': '~2.182.000 pontos (v10)',
    'Memória RAM': '8 GB LPDDR5X',
    'Armazenamento': '128 GB ou 256 GB UFS',
    'Câmera Traseira Principal': '50 MP, f/1.8 com OIS (Dual Pixel)',
    'Câmera Telefoto (Zoom)': '8 MP, f/2.4 com Zoom Óptico 3x (até 30x digital)',
    'Câmera Ultrawide': '12 MP, f/2.2 (123º FoV)',
    'Câmera Frontal': '12 MP com foco automático (vídeo 4K 60 fps)',
    'Gravação de Vídeo': 'Traseira: até 8K a 30 fps / 4K a 60 fps; Frontal: até 4K a 60 fps',
    'Bateria': '4.900 mAh (autonomia média de 1 dia)',
    'Carregamento com Fio': 'Até 45W (carregador de 25W incluso na caixa)',
    'Carregamento Sem Fio': 'Sim, 15W Wireless + carregamento reverso sem fio',
    'Construção': 'Traseira em vidro Gorilla Glass, moldura em alumínio',
    'Resistência à Água': 'IP68 (submersão em água doce até 1,5m por 30 min)',
    'Sistema e Suporte': 'One UI (Android 15) com 7 anos de atualizações de SO e segurança',
    'Recursos Extras': 'Samsung DeX, Galaxy AI nativo, alto-falantes estéreo encorpados',
}

SPECS_POCO_X8 = {
    'Tela': '6.83" AMOLED, 1.5K (2712x1220), 120Hz, 3.500 nits de pico',
    'Processador': 'MediaTek Dimensity 9500s (4nm Octa-Core)',
    'Pontuação AnTuTu': '~2.732.000 pontos (v10)',
    'Memória RAM': '12 GB ou 16 GB LPDDR5X (+6 GB RAM Virtual)',
    'Armazenamento': '256 GB ou 512 GB UFS 4.0',
    'Câmera Traseira Principal': '50 MP, f/1.6 com OIS',
    'Câmera Telefoto (Zoom)': 'Sem telefoto dedicada (zoom digital por recorte até 10x)',
    'Câmera Ultrawide': '8 MP, f/2.2 (119º FoV)',
    'Câmera Frontal': '20 MP (vídeo até 1080p 60 fps)',
    'Gravação de Vídeo': 'Traseira: até 4K a 60 fps; Frontal: até 1080p a 60 fps',
    'Bateria': '8.500 mAh Silício-Carbono (até 2 dias de autonomia)',
    'Carregamento com Fio': '100W ultrarrápido (carregador de 100W incluso na caixa)',
    'Carregamento Sem Fio': 'Não possui suporte a carregamento por indução',
    'Construção': 'Traseira em vidro, moldura em alumínio reforçado',
    'Resistência à Água': 'IP68 e IP69 (proteção reforçada contra jatos de água em alta pressão)',
    'Sistema e Suporte': 'HyperOS (Android 15) com 4 anos de Android e 6 de segurança',
    'Recursos Extras': 'Sensor Infravermelho, LED de notificações nas câmeras, Câmara de vapor gigante',
}

PROS_S25_FE = """Câmera telefoto de 8 MP com zoom óptico real de 3x (e até 30x digital)
Gravação de vídeo profissional até 8K na traseira e 4K a 60 fps na câmera frontal
Câmera ultrawide superior de 12 MP com maior ângulo e nitidez nas bordas
Suporte a carregamento sem fio (15W wireless) e carregamento sem fio reverso
Suporte ao Samsung DeX (transforma o smartphone em computador) e suíte Galaxy AI
Compromisso de 7 anos de atualizações de sistema operacional Android e segurança
Tela Dynamic AMOLED 2X com taxa variável LTPO (1 a 120 Hz) para economia
Áudio estéreo mais encorpado e equilibrado com graves marcantes"""

CONS_S25_FE = """Bateria bem menor de 4.900 mAh (autonomia média de ~1 dia contra 2 dias do Poco)
Carregador de apenas 25W incluso na caixa (suporta 45W, mas precisa comprar à parte)
Desempenho no AnTuTu cerca de 550 mil pontos abaixo do Dimensity 9500s
Versão de entrada inicia com 8 GB de RAM e 128 GB de armazenamento
Brilho de pico menor (1.900 nits contra 3.500 nits do concorrente)"""

PROS_POCO_X8 = """Bateria colossal de 8.500 mAh de silício-carbono com autonomia de até 2 dias
Carregamento ultrarrápido de 100W com carregador de 100W incluso na embalagem (60%+ em 30 min)
Desempenho monstro com MediaTek Dimensity 9500s (mais de 2.732.000 pontos no AnTuTu)
Sistema de refrigeração líquida com câmara de vapor gigante para jogatinas sem quedas de FPS
Configuração base generosa: 12 GB de RAM (+6 GB virtual) e 256 GB de armazenamento UFS 4.0
Tela AMOLED de 6,83 polegadas 1.5K com brilho de pico de 3.500 nits e bordas ultrafinas
Certificação dupla de resistência à água e poeira: IP68 e IP69 (jatos de alta pressão)
Sensor infravermelho integrado e anel de LED de notificações nas câmeras
Excelente processamento noturno na câmera principal de 50 MP"""

CONS_POCO_X8 = """Sem câmera telefoto dedicada (zoom apenas digital recortado no sensor até 10x)
Câmera frontal limitada a gravação em Full HD 1080p a 60 fps (sem suporte a 4K)
Câmera ultrawide básica de 8 MP com menor definição nas bordas
Não possui suporte a carregamento sem fio (indução)
Menor tempo de suporte de software (4 anos de Android contra 7 anos da Samsung)
Sem modo desktop integrado equivalente ao Samsung DeX"""


def create_placeholder_image():
    main_dir = os.path.join(settings.MEDIA_ROOT, 'comparisons', 'main')
    os.makedirs(main_dir, exist_ok=True)
    path = os.path.join(main_dir, f'{SLUG}.webp')
    
    img = Image.new('RGB', (1280, 720), '#0a0a0a')
    draw = ImageDraw.Draw(img)
    
    # Fundo degradê sutil
    for y in range(720):
        shade = int(10 + (y / 720.0) * 22)
        draw.line([(0, y), (1280, y)], fill=(shade, shade, shade + 3))
    
    # Detalhe geométrico com verde NVIDIA (#76b900)
    draw.rectangle([(0, 0), (12, 720)], fill=(118, 185, 0))
    draw.rectangle([(0, 0), (1280, 10)], fill=(118, 185, 0))
    draw.rectangle([(40, 40), (70, 70)], fill=(118, 185, 0))
    
    try:
        font_eyebrow = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 24)
        font_title = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 54)
        font_vs = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 44)
        font_brand = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 28)
    except OSError:
        font_eyebrow = ImageFont.load_default()
        font_title = font_eyebrow
        font_vs = font_eyebrow
        font_brand = font_eyebrow
        
    eyebrow = 'COMPARATIVO ESPECIAL 2026 • ANDRÉ INDICA'
    p1_title = 'Galaxy S25 FE'
    vs_text = 'VS'
    p2_title = 'Poco X8 Pro Max'
    sub_text = '8.500 mAh vs 4.900 mAh • Dimensity 9500s vs Exynos 2400 • Zoom 3x'
    
    draw.text((90, 45), eyebrow, fill=(118, 185, 0), font=font_eyebrow)
    
    # Linha de destaque para os dois celulares
    draw.text((90, 240), p1_title, fill=(255, 255, 255), font=font_title)
    draw.text((90, 310), vs_text, fill=(118, 185, 0), font=font_vs)
    draw.text((90, 370), p2_title, fill=(255, 255, 255), font=font_title)
    
    draw.text((90, 490), sub_text, fill=(180, 180, 180), font=font_brand)
    
    img.save(path, format='WEBP', quality=85)
    return f'comparisons/main/{SLUG}.webp'


def main():
    category, _ = Category.objects.get_or_create(
        slug='mobile',
        defaults={'name': 'Mobile'}
    )
    
    prod_samsung, _ = Product.objects.get_or_create(
        brand='Samsung',
        name='Galaxy S25 FE',
        defaults={'category': category}
    )
    
    prod_poco, _ = Product.objects.get_or_create(
        brand='Poco',
        name='Poco X8 Pro Max',
        defaults={'category': category}
    )
    
    author = User.objects.filter(username='admin').first() or User.objects.first()
    
    image_rel_path = create_placeholder_image()
    print(f'Imagem criada em: {image_rel_path}')
    
    comp, created = Comparison.objects.update_or_create(
        slug=SLUG,
        defaults={
            'product_1': prod_samsung,
            'product_2': prod_poco,
            'title': TITLE,
            'author': author,
            'excerpt': EXCERPT,
            'content': CONTENT.strip(),
            'conclusion': CONCLUSION.strip(),
            'main_image': image_rel_path,
            'amazon_link_1': AMAZON_LINK,
            'shopee_link_1': SHOPEE_LINK,
            'amazon_link_2': AMAZON_LINK,
            'shopee_link_2': SHOPEE_LINK,
            'tags_input': 'samsung, galaxy s25 fe, poco x8 pro max, xiaomi, comparativo, smartphone, celular 2026, dimensity 9500s, bateria 8500mah',
            'pros_1': PROS_S25_FE.strip(),
            'cons_1': CONS_S25_FE.strip(),
            'rating_1': 8.7,
            'pros_2': PROS_POCO_X8.strip(),
            'cons_2': CONS_POCO_X8.strip(),
            'rating_2': 9.2,
            'specifications_1': SPECS_S25_FE,
            'specifications_2': SPECS_POCO_X8,
            'rating': 9.1,
            'is_published': True,
            'is_featured': True,
        }
    )
    
    status_str = "Criado" if created else "Atualizado"
    print(f'Comparativo {status_str} com sucesso! ID={comp.id}, Slug={comp.slug}')


if __name__ == '__main__':
    main()

