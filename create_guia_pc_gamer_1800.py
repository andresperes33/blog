"""Cria o guia de compra "Como Montar um PC Gamer Barato de R$ 1.800 em 2026"
(Guide + 7 GuideItems + Categoria PC Gamer) no banco local.

Uso:
    $env:SECRET_KEY="test"; $env:DEBUG="True"; python create_guia_pc_gamer_1800.py
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
from reviews.models import Category, Guide, GuideItem

SLUG = 'como-montar-pc-gamer-barato-1800-2026'
TITLE = 'Como Montar um PC Gamer Barato de R$ 1.800 em 2026: Guia Completo Peça por Peça'
EXCERPT = (
    'Guia definitivo para montar um PC Gamer custo-benefício de R$ 1.700 a R$ 1.800 em 2026. '
    'Lista completa de peças recomendadas no AliExpress e Shopee, testes reais em jogos '
    '(Battlefield, Forza Horizon e Elden Ring em Full HD) e como extrair o máximo gastando pouco.'
)

CONTENT = """
<p>Montar um computador gamer em 2026 tornou-se um desafio real para o bolso do brasileiro: os lançamentos mais recentes de processadores e placas de vídeo empurraram os orçamentos de entrada para a casa dos R$ 4.000 a R$ 5.000. Mas será que você realmente precisa gastar tudo isso para se divertir com gráficos bonitos e alta taxa de quadros?</p>
<p>A resposta é <strong>não</strong>. Fomos atrás de cada componente no mercado, garimpando as peças com a melhor relação entre custo e entrega real de desempenho, e montamos um <strong>PC Gamer completo na faixa de R$ 1.700 a R$ 1.800</strong> capaz de rodar títulos modernos em Full HD com folga, aproveitando tecnologias como <strong>FSR 3</strong> e <strong>Frame Generation</strong>.</p>
<p>Neste guia, você confere a lista completa peça por peça com links de compra confiáveis, testes de bancada em jogos pesados e o passo a passo para não passar aperto na montagem.</p>

<h2>Orçamento Estimado: O que dá para comprar com R$ 1.800?</h2>
<p>A distribuição do investimento foi planejada para priorizar onde realmente importa para jogos: <strong>processador com muitos threads</strong>, <strong>placa de vídeo com 8 GB de VRAM</strong> e <strong>SSD NVMe veloz</strong>.</p>

<div class="overflow-x-auto my-6">
    <table class="w-full text-left border-collapse border border-hairline">
        <thead>
            <tr class="bg-soft text-[12px] uppercase font-bold text-mute">
                <th class="p-3 border-b border-hairline">Componente</th>
                <th class="p-3 border-b border-hairline">Modelo Escolhido</th>
                <th class="p-3 border-b border-hairline text-right">Preço Médio (R$)</th>
            </tr>
        </thead>
        <tbody class="divide-y divide-hairline text-[14px] text-body">
            <tr>
                <td class="p-3 font-semibold">Kit Placa-Mãe + Processador</td>
                <td class="p-3">Soyo X99 + Intel Xeon E5-2676 V3 (12C / 24T)</td>
                <td class="p-3 text-right text-primary font-bold">R$ 550,00</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">Placa de Vídeo</td>
                <td class="p-3">AMD Radeon RX 580 8GB GDDR5 (2048SP)</td>
                <td class="p-3 text-right text-primary font-bold">R$ 650,00</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">Memória RAM</td>
                <td class="p-3">16 GB (2x 8GB) DDR3 1600 MHz Dual Channel</td>
                <td class="p-3 text-right text-primary font-bold">Incluso no Kit / R$ 100</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">Armazenamento</td>
                <td class="p-3">SSD M.2 NVMe Netac 256GB / 500GB PCIe 3.0</td>
                <td class="p-3 text-right text-primary font-bold">R$ 130,00</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">Fonte de Alimentação</td>
                <td class="p-3">500W com PFC Ativo e Selo 80 Plus / Cybenetics</td>
                <td class="p-3 text-right text-primary font-bold">R$ 180,00</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">Gabinete</td>
                <td class="p-3">Rise Mode Gamer Estilo Aquário Branco</td>
                <td class="p-3 text-right text-primary font-bold">R$ 110,00</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">Refrigeração</td>
                <td class="p-3">Air Cooler Perfil Baixo LGA 2011-3</td>
                <td class="p-3 text-right text-primary font-bold">R$ 60,00</td>
            </tr>
            <tr class="bg-soft font-bold text-ink">
                <td class="p-3" colspan="2">TOTAL DO INVESTIMENTO</td>
                <td class="p-3 text-right text-primary text-base">~ R$ 1.730,00 a R$ 1.830,00</td>
            </tr>
        </tbody>
    </table>
</div>

<h2>Por que a combinação Xeon X99 + RX 580 ainda reina em 2026?</h2>
<p>O segredo desse computador econômico está em equilibrar força bruta multitarefa com o preço imbatível de plataformas maduras:</p>
<ul>
    <li><strong>Intel Xeon E5-2676 V3:</strong> São <strong>12 núcleos físicos e 24 threads</strong>. No benchmark do CPU-Z, sua pontuação multi-thread alcança mais de <strong>4.500 pontos</strong>, um resultado muito semelhante ao de um <em>Ryzen 5 5500</em> novo que sozinho custa quase o valor do kit inteiro. Por ter muitos núcleos, ele segura folgadamente o Windows 11, Discord, navegador com abas abertas e jogos sem engasgos.</li>
    <li><strong>Memórias DDR3 no X99:</strong> A placa-mãe Soyo possui a peculiaridade de trabalhar com memórias DDR3 de servidor, que são extremamente mais baratas do que kits DDR4 e DDR5, reduzindo drasticamente o custo final do kit sem comprometer os jogos.</li>
    <li><strong>Radeon RX 580 8GB:</strong> Continua sendo a placa com 8 GB de VRAM mais barata do planeta. Em 2026, jogos modernos exigem mais de 4 GB ou 6 GB de memória de vídeo só para carregar texturas limpas em Full HD. Placas de entrada com 4 GB travam e apresentam gagueira constante (stuttering), enquanto a RX 580 respira aliviada com seus 8 GB.</li>
</ul>

<h2>Desempenho Real em Jogos: Nossos Testes em Full HD</h2>
<p>Ligamos a máquina na bancada, instalamos os drivers mais recentes da AMD e rodamos três dos jogos mais exigentes e populares da atualidade com medição em tempo real de FPS, consumo de VRAM e estabilidade:</p>

<div class="overflow-x-auto my-6">
    <table class="w-full text-left border-collapse border border-hairline">
        <thead>
            <tr class="bg-soft text-[12px] uppercase font-bold text-mute">
                <th class="p-3 border-b border-hairline">Jogo Testado</th>
                <th class="p-3 border-b border-hairline">Resolução / Preset</th>
                <th class="p-3 border-b border-hairline">Recursos Ativos</th>
                <th class="p-3 border-b border-hairline text-center">Média FPS</th>
                <th class="p-3 border-b border-hairline text-center">1% Low</th>
                <th class="p-3 border-b border-hairline">Uso VRAM / RAM</th>
            </tr>
        </thead>
        <tbody class="divide-y divide-hairline text-[14px] text-body">
            <tr>
                <td class="p-3 font-semibold">Battlefield (BF)</td>
                <td class="p-3">1080p (Full HD) • Preset Baixo</td>
                <td class="p-3">FSR Qualidade + Frame Generation</td>
                <td class="p-3 text-center text-primary font-bold text-base">97 - 98 FPS</td>
                <td class="p-3 text-center font-semibold">68 FPS</td>
                <td class="p-3">5.8 GB VRAM / 10.2 GB RAM</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">Forza Horizon</td>
                <td class="p-3">1080p (Full HD) • Preset Médio</td>
                <td class="p-3">FSR 3.1.5 Modo Qualidade</td>
                <td class="p-3 text-center text-primary font-bold text-base">56 - 58 FPS</td>
                <td class="p-3 text-center font-semibold">41 FPS</td>
                <td class="p-3">6.6 GB VRAM / 12.0 GB RAM</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">Elden Ring</td>
                <td class="p-3">1080p (Full HD) • Preset Alto</td>
                <td class="p-3">Nativo (Sem FSR / Upscaling)</td>
                <td class="p-3 text-center text-primary font-bold text-base">50 - 52 FPS</td>
                <td class="p-3 text-center font-semibold">44 FPS</td>
                <td class="p-3">3.8 GB VRAM / 11.6 GB RAM</td>
            </tr>
        </tbody>
    </table>
</div>

<div class="card p-6 my-8 border-l-4 border-l-primary">
    <span class="corner-square"></span>
    <h3 class="text-lg font-bold text-ink mb-2">Dica de Ouro: Como Corrigir o Erro FH205 / FH215 no Forza Horizon</h3>
    <p class="text-body text-[14px] leading-relaxed mb-3">
        Ao abrir o Forza Horizon na RX 580 pela primeira vez, o jogo pode exibir a mensagem: <em>"Sua placa de vídeo não é compatível (Código FH205 / FH215)"</em>. Para solucionar em menos de 5 minutos:
    </p>
    <ol class="list-decimal list-inside space-y-2 text-[14px] text-body">
        <li>Baixe o mod de contorno de compatibilidade no GitHub (pesquise por <code>Forza Horizon RX 580 FH215 Fix</code>).</li>
        <li>Extraia a pasta e copie o arquivo <code>.dll</code> diretamente para a pasta principal onde o jogo está instalado (onde fica o executável <code>.exe</code> do Forza).</li>
        <li>Se ainda solicitar atualização de driver, instale o pacote <strong>AMD Agility SDK Work Graphs</strong> oficial e reinicie o PC.</li>
        <li>Pronto! O jogo iniciará normalmente, permitindo rodar em Full HD Médio a quase 60 FPS estáveis.</li>
    </ol>
</div>

<h2>Dicas Essenciais para a Montagem</h2>
<ul>
    <li><strong>Organização dos Cabos:</strong> O gabinete Rise Mode estilo aquário possui excelente espaço atrás da placa-mãe. Esconda os cabos sobressalentes da fonte para manter o interior limpo e maximizar o fluxo de ar para a GPU.</li>
    <li><strong>Drivers Corretos:</strong> Baixe o driver <em>AMD Software Adrenalin</em> para a RX 580 diretamente do site da AMD. Não deixe o Windows Update instalar drivers genéricos antigos.</li>
    <li><strong>Dual Channel Obrigatório:</strong> Certifique-se de instalar as duas memórias RAM de 8 GB nos slots corretos da placa X99 para ativar o Dual Channel. Isso dobra a largura de banda de memória do Xeon e previne quedas de quadros (1% low).</li>
</ul>
"""

CONCLUSION = """
<p><strong>Veredito do André Indica: Vale a pena montar esse PC em 2026?</strong></p>
<p>Com certeza. Por menos de <strong>R$ 1.800</strong>, é praticamente impossível encontrar qualquer computador pré-montado no varejo nacional ou notebook que chegue perto desse desempenho. Você leva para casa uma máquina com <strong>12 núcleos, 16 GB de RAM, 8 GB de VRAM e SSD NVMe</strong>, capaz de rodar títulos como <em>Battlefield, Forza Horizon, GTA V, CS2, Valorant e Elden Ring</em> em Full HD com ótima fluidez.</p>
<p>Para quem está com o orçamento curto e quer sair do videogame antigo ou do PC fraco sem se endividar, essa é a montagem definitiva de custo-benefício. Utilize os links verificados abaixo para garantir as melhores peças e preços com frete seguro:</p>
"""

ITEMS = [
    {
        'position': 1,
        'name': 'Kit Soyo X99 + Intel Xeon E5-2676 V3 (12C / 24T)',
        'description': (
            '<p>O coração do nosso PC econômico. Este kit da <strong>Soyo</strong> combina uma placa-mãe X99 com o potente processador <strong>Intel Xeon E5-2676 V3</strong>, que entrega nada menos que <strong>12 núcleos físicos e 24 threads</strong> com clock base de 2.4 GHz.</p>'
            '<p>No teste de benchmark do CPU-Z, sua pontuação multi-thread bate expressivos <strong>4.500 pontos</strong> — desempenho comparável ao de um AMD Ryzen 5 5500. A placa conta com slot M.2 NVMe nativo, portas USB 3.0 e boa construção. Uma das melhores partes é que você encontra esse kit já com <strong>estoque nacional no Brasil</strong> no AliExpress por volta de R$ 550, eliminando a espera e o risco de taxas extras de importação.</p>'
        ),
        'pros': (
            '12 núcleos físicos e 24 threads (excelente para jogos e multitarefa)\n'
            'Pontuação multi-thread similar ao Ryzen 5 5500 por uma fração do preço\n'
            'Slot M.2 NVMe PCIe integrado para SSDs rápidos\n'
            'Opção com estoque já no Brasil sem imposto surpresa de 60%\n'
            'Custo-benefício imbatível na faixa dos R$ 550'
        ),
        'cons': (
            'Clock por núcleo moderado (2.4 GHz base), com menor desempenho single-thread\n'
            'Placa-mãe simples sem suporte a overclock avançado'
        ),
        'aliexpress': 'https://pt.aliexpress.com/item/1005010490994831.html?aff_fcid=947a3a2d0f234bbb97618f2b8fafb48f-1789996761219-03578-_mL84t3V&tt=CPS_NORMAL&aff_fsk=_mL84t3V&aff_platform=influencer-program-register-campaign&sk=_mL84t3V&aff_trace_key=947a3a2d0f234bbb97618f2b8fafb48f-1789996761219-03578-_mL84t3V&terminal_id=c49e47a8944e447aae1f6c05887608c9&afSmartRedirect=y',
    },
    {
        'position': 2,
        'name': 'Placa de Vídeo AMD Radeon RX 580 8GB GDDR5 (2048SP)',
        'description': (
            '<p>A clássica e indispensável <strong>Radeon RX 580 8GB</strong>. Não existe hoje no mercado de hardware nenhuma placa de vídeo abaixo de R$ 700 que encare e entregue o nível de desempenho e estabilidade desse modelo.</p>'
            '<p>Os <strong>8 GB de memória de vídeo (VRAM)</strong> são o divisor de águas: enquanto placas de 4 GB enfrentam engasgos severos em jogos de 2026, a RX 580 carrega texturas em Full HD com tranquilidade. Além disso, o suporte ao <strong>AMD FSR 3 com Frame Generation</strong> permite destravar taxas de quase 100 FPS em títulos pesados como Battlefield. Um verdadeiro tanque de guerra por cerca de R$ 600 a R$ 650 em promoção.</p>'
        ),
        'pros': (
            '8 GB de VRAM GDDR5: essencial para rodar jogos modernos sem engasgos de textura\n'
            'Suporte a tecnologias modernas de upscaling: AMD FSR 3 e Frame Gen\n'
            'Entrega 60+ FPS estáveis em Full HD na maioria dos jogos competitivos e AAA\n'
            'Visual moderno em branco que combina com gabinetes aquário\n'
            'Melhor relação custo por frame na faixa de R$ 600 a R$ 700'
        ),
        'cons': (
            'Consumo de energia na casa dos 150W (exige fonte com conector PCIe de 8 pinos)\n'
            'Alguns jogos recentes exigem fix de compatibilidade ou drivers específicos'
        ),
        'aliexpress': 'https://s.click.aliexpress.com/e/_c3dkaEvF',
    },
    {
        'position': 3,
        'name': 'Memória RAM 16 GB (2x 8GB) DDR3 1600 MHz Dual Channel',
        'description': (
            '<p>A memória RAM é fundamental para evitar travamentos e quedas bruscas de frametime. Neste kit, optamos por <strong>16 GB de RAM</strong> divididos em dois pentes de 8 GB operando a 1600 MHz em <strong>Dual Channel</strong>.</p>'
            '<p>O grande trunfo desta placa Soyo X99 é aceitar módulos DDR3: isso reduz drasticamente o custo em comparação a kits DDR4 ou DDR5, mantendo 16 GB de espaço que é o padrão ouro para rodar jogos modernos (onde Battlefield consumiu 10.2 GB e Forza Horizon bateu 12 GB durante os nossos testes).</p>'
        ),
        'pros': (
            '16 GB em Dual Channel (2x 8GB) para dobrar a largura de banda do processador\n'
            'Preço muito inferior às memórias DDR4/DDR5 de mesma capacidade\n'
            'Dissipador metálico que auxilia no controle térmico e no visual\n'
            'Capacidade suficiente para rodar qualquer jogo atual sem gargalo de RAM'
        ),
        'cons': (
            'Frequência de 1600 MHz limitada pelo padrão DDR3\n'
            'Não é compatível com placas-mãe de gerações mais recentes (DDR4/DDR5)'
        ),
        'aliexpress': 'https://s.click.aliexpress.com/e/_c4o1aEy1',
    },
    {
        'position': 4,
        'name': 'Armazenamento SSD NVMe M.2 Netac PCIe 3.0 (256 GB ou 500 GB)',
        'description': (
            '<p>Esqueça HDs mecânicos ou SSDs SATA lentos. O <strong>SSD M.2 NVMe Netac</strong> entrega velocidades de leitura e escrita várias vezes superiores, garantindo que o Windows 11 inicialize em poucos segundos e os jogos carreguem quase instantaneamente.</p>'
            '<p>Com as novas regras tributárias de importação abaixo de 50 dólares, esse modelo ficou ainda mais atraente, pois está isento do imposto de importação federal de 60%, recolhendo apenas o ICMS. Você pode escolher a versão de <strong>256 GB</strong> para economizar ao máximo ou a de <strong>500 GB</strong> para instalar mais jogos simultaneamente.</p>'
        ),
        'pros': (
            'Velocidades NVMe PCIe de alta performance (boot em segundos)\n'
            'Instalação direta no slot M.2 da placa-mãe, sem necessidade de cabos SATA ou de força\n'
            'Preço extremamente competitivo no AliExpress com isenção de imposto de 60%\n'
            'Excelente durabilidade e controle térmico com LED indicador de atividade'
        ),
        'cons': (
            'Versão de 256 GB pode lotar rápido com mais de 2 ou 3 jogos pesados instalados'
        ),
        'aliexpress': 'https://s.click.aliexpress.com/e/_c3kKBXOZ',
    },
    {
        'position': 5,
        'name': 'Fonte de Alimentação 500W com PFC Ativo e Selo 80 Plus / Cybenetics',
        'description': (
            '<p>A fonte de alimentação é o coração elétrico de qualquer setup gamer e a peça onde você nunca deve economizar de forma irresponsável. Para a nossa configuração de Xeon E5-2676 V3 e RX 580, uma fonte de <strong>400W a 500W de boa qualidade</strong> é mais do que suficiente para segurar tudo com muita folga.</p>'
            '<p>O consumo total desse computador em carga máxima durante jogos fica entre 250W e 300W. Por isso, uma fonte de 500W com <strong>PFC Ativo</strong> e certificação de eficiência (como 80 Plus Bronze ou Cybenetics) garante que a fonte trabalhará na sua faixa de maior eficiência, economizando na conta de luz e protegendo suas peças contra variações de tensão.</p>'
        ),
        'pros': (
            'Potência de 500W com ampla folga para a RX 580 e o Xeon\n'
            'PFC Ativo para estabilidade de tensão e proteção contra surtos\n'
            'Cabos com conectores PCIe de 6+2 pinos para alimentar placas dedicadas\n'
            'Preço acessível no mercado nacional com entrega rápida pela Shopee (~R$ 180)'
        ),
        'cons': (
            'Cabos não modulares (exigem um pouco mais de cuidado na organização atrás do gabinete)'
        ),
        'shopee': 'https://s.shopee.com.br/LnPCraQA8',
    },
    {
        'position': 6,
        'name': 'Gabinete Gamer Rise Mode Aquário Branco (Vidro Temperado)',
        'description': (
            '<p>O gabinete é a cara do seu setup. Em vez de escolher um gabinete genérico feio e fechado, você pode encontrar modelos espetaculares na faixa de <strong>R$ 80 a R$ 119</strong>. Escolhemos o <strong>Rise Mode estilo Aquário</strong> na cor branca, que virou febre no mercado.</p>'
            '<p>Ele conta com painel lateral e frontal em <strong>vidro temperado</strong> transparente, permitindo visualizar todos os componentes internos. Ele tem ótimo espaço traseiro para gerenciamento de cabos, suporte a múltiplos coolers de 120 mm e combinou com perfeição com o tom branco da placa de vídeo.</p>'
        ),
        'pros': (
            'Design moderno estilo aquário com visão panorâmica em vidro temperado\n'
            'Excelente apelo estético para quem quer um setup bonito e clean\n'
            'Espaço dedicado para esconder a fonte e os cabos traseiros\n'
            'Preço surpreendentemente baixo no mercado nacional (R$ 80 a R$ 119 na Shopee)'
        ),
        'cons': (
            'Não acompanha ventoinhas (fans) na versão mais barata (podem ser adicionadas depois)'
        ),
        'shopee': 'https://s.shopee.com.br/7AdjLIVJ38',
    },
    {
        'position': 7,
        'name': 'Air Cooler Perfil Baixo para Socket Intel LGA 2011-3',
        'description': (
            '<p>Para manter o Xeon E5-2676 V3 trabalhando em temperaturas amenas, você não precisa de um water cooler caro de R$ 300. Um <strong>Air Cooler de perfil baixo</strong> dedicado para o socket LGA 2011-3 cumpre o papel com louvor.</p>'
            '<p>Durante os nossos testes mais intensos em jogos pesados, o processador operou sempre na faixa dos <strong>55 °C a 62 °C</strong>, com rotação silenciosa e sem thermal throttling. Custa na faixa dos R$ 50 a R$ 60 no AliExpress e já vem com a presilha de fixação padrão para o socket X99.</p>'
        ),
        'pros': (
            'Excelente capacidade de dissipação térmica para processadores Xeon LGA 2011-3\n'
            'Perfil baixo que não bloqueia os slots de memória RAM nem bate no vidro do gabinete\n'
            'Operação silenciosa mesmo durante longas sessões de jogatina\n'
            'Preço muito baixo (cerca de R$ 60 no AliExpress)'
        ),
        'cons': (
            'Não possui iluminação ARGB sincronizável na versão mais básica'
        ),
        'aliexpress': 'https://s.click.aliexpress.com/e/_c430i4Iz',
    },
]


def create_placeholder_image(rel_path, title, subtitle='André Indica'):
    abs_path = os.path.join(settings.MEDIA_ROOT, rel_path)
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    if os.path.exists(abs_path):
        return rel_path

    img = Image.new('RGB', (1280, 720), '#0a0a0a')
    draw = ImageDraw.Draw(img)

    for y in range(720):
        shade = int(12 + (y / 720.0) * 20)
        draw.line([(0, y), (1280, y)], fill=(shade, shade, shade + 2))

    # Detalhes NVIDIA green
    draw.rectangle([(0, 0), (12, 720)], fill=(118, 185, 0))
    draw.rectangle([(0, 0), (1280, 8)], fill=(118, 185, 0))
    draw.rectangle([(40, 40), (68, 68)], fill=(118, 185, 0))

    try:
        font_eyebrow = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 24)
        font_title = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 50)
        font_sub = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 28)
    except OSError:
        font_eyebrow = ImageFont.load_default()
        font_title = font_eyebrow
        font_sub = font_eyebrow

    draw.text((85, 45), 'GUIA DE MONTAGEM • PC GAMER 2026', fill=(118, 185, 0), font=font_eyebrow)
    draw.text((85, 280), title, fill=(255, 255, 255), font=font_title)
    draw.text((85, 360), subtitle, fill=(180, 180, 180), font=font_sub)

    img.save(abs_path, format='WEBP', quality=85)
    return rel_path


def main():
    category, _ = Category.objects.get_or_create(
        slug='pc-gamer',
        defaults={
            'name': 'PC Gamer',
            'icon': 'icon-pc'
        }
    )
    if category.icon != 'icon-pc':
        category.icon = 'icon-pc'
        category.save()

    author = User.objects.filter(username='admin').first() or User.objects.first()

    main_img = create_placeholder_image(
        'guides/main/como-montar-pc-gamer-barato-1800-2026.webp',
        'PC Gamer Barato R$ 1.800',
        'Xeon X99 12C/24T • Radeon RX 580 8GB • Full HD 60+ FPS'
    )

    guide, created = Guide.objects.update_or_create(
        slug=SLUG,
        defaults={
            'title': TITLE,
            'category': category,
            'author': author,
            'excerpt': EXCERPT,
            'content': CONTENT.strip(),
            'conclusion': CONCLUSION.strip(),
            'main_image': main_img,
            'is_published': True,
            'is_featured': True,
        }
    )

    status_str = "Criado" if created else "Atualizado"
    print(f'Guia {status_str}! ID={guide.id}, Slug={guide.slug}')

    # Criação dos Itens
    for item_data in ITEMS:
        item_img_rel = f"guides/items/{item_data['position']}-peca-{item_data['name'][:20].lower().replace(' ', '-')}.webp"
        item_img = create_placeholder_image(
            item_img_rel,
            f"Peça #{item_data['position']}",
            item_data['name'][:35]
        )

        gi, gi_created = GuideItem.objects.update_or_create(
            guide=guide,
            position=item_data['position'],
            defaults={
                'name': item_data['name'],
                'description': item_data['description'],
                'pros': item_data.get('pros', ''),
                'cons': item_data.get('cons', ''),
                'image': item_img,
                'aliexpress_link': item_data.get('aliexpress'),
                'shopee_link': item_data.get('shopee'),
                'amazon_link': item_data.get('amazon'),
                'mercadolivre_link': item_data.get('ml'),
            }
        )
        gi_status = "Criado" if gi_created else "Atualizado"
        print(f"   -> Item {item_data['position']} ({item_data['name'][:25]}...) {gi_status}")

    print('Todos os itens foram processados com sucesso!')


if __name__ == '__main__':
    main()

