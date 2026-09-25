"""Cria o guia de compra "Melhores placas de video para comprar em 2026"
(Guide + 13 GuideItems) na categoria Placas de Video.

Uso:
    $env:SECRET_KEY="test"; $env:DEBUG="True"; python create_guia_placas_video_2026.py
    $env:SECRET_KEY="test"; $env:DEBUG="True"; python export_content.py

O conteudo e escrito para SEO + GEO (Generative Engine Optimization):
resposta direta no primeiro paragrafo, tabelas comparativas, secoes em
formato de pergunta e bloco de FAQ (renderizado do campo `faq` do model
e exposto como schema.org/FAQPage).
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

SLUG = 'melhores-placas-de-video-2026'
TITLE = 'Melhores placas de vídeo para comprar em 2026: guia de custo-benefício'
EXCERPT = (
    'Qual placa de vídeo comprar em 2026? Comparamos 13 modelos por preço, VRAM '
    'e desempenho real em Full HD, 2K e 4K, com o veredito de cada uma.'
)

# Os precos citados abaixo foram levantados em setembro de 2026 e oscilam
# bastante: o guia sempre recomenda conferir o historico antes de fechar a compra.
CONTENT = """
<p><strong>Resposta curta:</strong> se você quer gastar o mínimo e não ter dor de cabeça, a <strong>Radeon RX 7600 8GB</strong> é a melhor placa de custo-benefício de 2026. Se quer o melhor desempenho pelo preço, a <strong>Radeon RX 9060 XT 16GB</strong> entrega mais quadros por real do que qualquer modelo da NVIDIA na mesma faixa. E se o seu orçamento é curto de verdade, a <strong>RX 580 8GB</strong> ainda roda uma boa lista de jogos por menos de R$ 600.</p>

<p>O problema de comprar placa de vídeo em 2026 é outro: <strong>os preços subiram, e muito</strong>. A RTX 5060, que antes aparecia facilmente por R$ 1.900, hoje tem preço de base na casa dos R$ 2.500. A RTX 5060 Ti de 16 GB saltou de R$ 3.600 para quase R$ 4.000 em poucos dias, e a RTX 5070 que muita gente comprou por R$ 3.846 já está a R$ 5.000. Comprar no impulso, sem comparar histórico, é exatamente como se perde dinheiro.</p>

<p>Por isso este guia é organizado <strong>da mais barata para a mais potente</strong>, com 13 placas que ainda valem a pena em 2026. Para cada uma você encontra o preço real de mercado, o perfil de uso, o que ela entrega de verdade e, principalmente, <strong>quando ela não vale a pena</strong> — porque a placa errada na faixa errada é dinheiro jogado fora.</p>

<h2>Resposta rápida: qual placa de vídeo comprar em 2026?</h2>
<p>Se você quer pular direto para a decisão, esta é a nossa recomendação por faixa de orçamento, com base nos preços que levantamos:</p>

<div class="overflow-x-auto my-6">
    <table class="w-full text-left border-collapse border border-hairline">
        <thead>
            <tr class="bg-soft text-[12px] uppercase font-bold text-mute">
                <th class="p-3 border-b border-hairline">Placa de Vídeo</th>
                <th class="p-3 border-b border-hairline text-right">Preço de Mercado</th>
                <th class="p-3 border-b border-hairline">Perfil</th>
                <th class="p-3 border-b border-hairline">Resolução Ideal</th>
            </tr>
        </thead>
        <tbody class="divide-y divide-hairline text-[14px] text-body">
            <tr>
                <td class="p-3 font-semibold">RX 580 8GB</td>
                <td class="p-3 text-right">~R$ 600</td>
                <td class="p-3">Entrada / semjgames novos</td>
                <td class="p-3">Full HD (Baixo)</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">RX 7600 8GB</td>
                <td class="p-3 text-right text-primary font-bold">R$ 1.700 – 2.000</td>
                <td class="p-3"><strong>Melhor custo-benefício</strong></td>
                <td class="p-3">Full HD (Alto/Ultra)</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">Intel Arc B580 12GB</td>
                <td class="p-3 text-right">Ver oferta</td>
                <td class="p-3">12 GB no orçamento</td>
                <td class="p-3">Full HD (Alto)</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">RTX 5050 8GB</td>
                <td class="p-3 text-right text-primary font-bold">R$ 1.700 – 1.950</td>
                <td class="p-3">Nvidia barata</td>
                <td class="p-3">Full HD (Alto)</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">RTX 5060 8GB</td>
                <td class="p-3 text-right">R$ 2.400 – 2.500</td>
                <td class="p-3">Full HD no Ultra</td>
                <td class="p-3">Full HD (Ultra)</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">RTX 5060 Ti 8GB</td>
                <td class="p-3 text-right">~R$ 2.700</td>
                <td class="p-3">2K com 8 GB</td>
                <td class="p-3">2K (Alto)</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">RX 9060 XT 16GB</td>
                <td class="p-3 text-right text-primary font-bold">R$ 3.100 – 3.300</td>
                <td class="p-3"><strong>Melhor preço por quadro</strong></td>
                <td class="p-3">2K (Ultra)</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">RTX 5070 12GB</td>
                <td class="p-3 text-right">R$ 5.000 – 5.300</td>
                <td class="p-3">4K com DLSS 5</td>
                <td class="p-3">2K/4K (Alto)</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">RTX 5070 Ti 16GB</td>
                <td class="p-3 text-right">R$ 6.700 – 9.000</td>
                <td class="p-3">Elite 4K</td>
                <td class="p-3">4K (Ultra)</td>
            </tr>
        </tbody>
    </table>
</div>

<div class="card p-6 my-8 border-l-4 border-l-primary">
    <span class="corner-square"></span>
    <h3 class="text-lg font-bold text-ink mb-2">Veredito em uma frase</h3>
    <p class="text-body text-[14px] leading-relaxed mb-0">
        Quer a melhor placa que dá para comprar? <strong>Radeon RX 7600 8GB</strong>. Quer o máximo de quadros por real? <strong>Radeon RX 9060 XT 16GB</strong>. Só quer uma NVIDIA com DLSS 5? <strong>RTX 5070 12GB</strong> — mas espere o preço cair. E tem orçamento apertado? <strong>RX 580 8GB</strong>, sabendo das limitações.
    </p>
</div>

<h2>Antes de comprar: os 3 erros que custam mais caro que a placa</h2>
<p>Um guia de placas de vídeo é inútil se você não levar em conta o resto do PC. Estes são os três erros mais comuns que a gente vê toda semana:</p>
<ul>
    <li><strong>Ignorar a fonte de alimentação.</strong> Placas de 16 GB e topo de linha puxam mais energia do que aparentam. Nunca use fonte de marca branca sem selo: uma fonte ruim é o que queima sua placa nova. Para as placas deste guia, a <strong>faixa segura é de 650W a 750W</strong>, com certificação real.</li>
    <li><strong>Achar que 8 GB ainda basta para tudo.</strong> Roda Full HD, sim. Mas em 2K e 4K a memória de vídeo vira o gargalo: texturas ficam sem nitidez, texturas estouram a VRAM e aparecem engasgos (stuttering). A partir de 2K, <strong>16 GB é o mínimo confortável</strong>.</li>
    <li><strong>Comprar placa para um gabinete pequeno demais.</strong> Com o mercado apertado, muita gente cai na tentação da placa de <strong>uma única ventoinha</strong> para economizar uns centimeters. A RTX 5050 de uma fã é o exemplo perfeito: só compensa se o seu gabinete for realmente compacto.</li>
</ul>

<h2>AMD ou NVIDIA em 2026: a grande decisão</h2>
<p>Essa é a dúvida que mais aparece, e a resposta curta mudou: <strong>a AMD subiu menos de preço que a NVIDIA</strong> e entrega desempenho equivalente ou melhor na maioria dos jogos. O argumento classic de "Nvidia é melhor por causa do DLSS" continua valendo em 2026 — o <strong>DLSS 5</strong> é uma tecnologia revolucionária e exclusiva das RTX 50 — mas pagar <strong>R$ 1.000 a mais por isso já não compensa</strong> em quase nenhuma das placas deste guia.</p>

<div class="overflow-x-auto my-6">
    <table class="w-full text-left border-collapse border border-hairline">
        <thead>
            <tr class="bg-soft text-[12px] uppercase font-bold text-mute">
                <th class="p-3 border-b border-hairline">Critério</th>
                <th class="p-3 border-b border-hairline">AMD (Radeon)</th>
                <th class="p-3 border-b border-hairline">NVIDIA (GeForce)</th>
            </tr>
        </thead>
        <tbody class="divide-y divide-hairline text-[14px] text-body">
            <tr>
                <td class="p-3 font-semibold">Preço em 2026</td>
                <td class="p-3 text-success font-bold">Subiu menos</td>
                <td class="p-3 text-error">Subiu mais (RTX 5060 e 5060 Ti)</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">Upscaling</td>
                <td class="p-3">FSR 4.1 (melhorou muito a RX 7600)</td>
                <td class="p-3">DLSS 5 (exclusivo RTX 50)</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">VRAM por real</td>
                <td class="p-3 text-success font-bold">Ganha (16 GB mais baratos)</td>
                <td class="p-3 text-error">Custa caro para subir de 8 GB</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">Desempenho bruto</td>
                <td class="p-3">Muito bom (RX 9060 XT e 9070 XT)</td>
                <td class="p-3">Bom (RTX 5070 perto da RX 9070)</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">Para quem é</td>
                <td class="p-3">Quem quer mais FPS por real</td>
                <td class="p-3">Quem quer DLSS 5 e desvalorizar menos</td>
            </tr>
        </tbody>
    </table>
</div>

<h2>Até R$ 1.000: Radeon RX 580 8GB — a única opção que ainda faz sentido</h2>
<p>Vamos ser honestos: <strong>abaixo da RX 7600 não existe placa de vídeo moderna que valha a pena</strong>. A única que ainda se sustenta é a antiga <strong>Radeon RX 580 8GB</strong>, que aparece em promoção na faixa dos <strong>R$ 600</strong> (com estoque nacional, em até 10x sem juros).</p>
<p>Ela roda uma lista razoável de jogos, e os 8 GB de VRAM ainda salvam em Full HD. Mas seja claro com você mesmo: <strong>é um produto antigo, com limitações reais</strong>. Jogos atuais de blockbuster podem não rodar, e a placa não tem as tecnologias de upscaling modernas. Compre sabendo disso.</p>

<h2>A melhor custo-benefício de 2026: Radeon RX 7600 8GB</h2>
<p>Se você só puder guardar uma única recomendação deste guia, guarde esta. A <strong>RX 7600 8GB</strong> é a placa que entrega <strong>o melhor desempenho por real gasto</strong> e não faz você pensar duas vezes na compra.</p>
<p>O grande ganho recente veio com o <strong>FSR 4.1</strong>, que deu um upgrade real de performance na RX 7600: com ele ligado, você tem <strong>ótimo desempenho em praticamente qualquer jogo que abrir</strong> em Full HD. É uma placa feita para quem quer <strong>solução gastando ainda pouco</strong> — não é uma placa de painho, e é justamente por isso que é a queridinha.</p>
<p>Um dado que ajuda a dimensionar: um <strong>PC completo com RX 7600</strong> (Ryzen 5 5500, fonte, SSD e tudo mais) apareceu por <strong>cerca de R$ 4.000</strong>. É praticamente o valor de uma placa 5060 ou 5060 Ti sozinha — e vem com o computador inteiro.</p>
<p>O preço de mercado atual está na <strong>faixa de R$ 1.700 a R$ 2.000</strong>, e ela frequentemente aparece abaixo disso em promoção (a melhor que encontramos foi R$ 1.697).</p>

<h2>Intel Arc B580 12GB: a surpresa do orçamento</h2>
<p>Se você tem orçamento apertado e quer <strong>mais VRAM que a concorrência</strong>, a <strong>Intel Arc B580 12GB</strong> merece atenção. Ter 12 GB numa placa de entrada é raro, e isso evita os engasgos de textura que atingem as concorrentes de 8 GB.</p>
<p>Na prática, ela é concorrente direta da RX 7600 e da RTX 5050 em Full HD. Só leve em conta que a <strong>Intel ainda pede drivers mais recentes</strong> para tirar o máximo de proveito, e o ecossistema de jogos é menor que o das duas grandes. Vale testar antes, se puder.</p>

<h2>NVIDIA: RTX 5050, RTX 5060 e RTX 5060 Ti</h2>
<h3>RTX 5050 8GB — a Nvidia de entrada, e só isso</h3>
<p>A <strong>RTX 5050</strong> entrega <strong>desempenho praticamente igual ao da RX 7600</strong>: os dois rodam os mesmos jogos com FPS bem parecidos, e cada uma ganha em títulos específicos. A AMD ganha alguns jogos, a NVIDIA ganha em outros.</p>
<p>O problema é o preço. A RTX 5050 apareceu historicamente na <strong>faixa de R$ 1.700 a R$ 1.900</strong> (e já foi vista mais barato), mas em várias lojas ela está sendo vendida a <strong>R$ 2.300 ou mais</strong> — e aí não compensa. <strong>Compre só na faixa de R$ 1.900, no máximo R$ 2.000</strong>. E atenção à versão de <strong>uma única ventoinha</strong>: ela só faz sentido se o seu gabinete for muito pequeno.</p>

<h3>RTX 5060 8GB — Full HD no Ultra, mas o preço mudou</h3>
<p>A <strong>RTX 5060 8GB</strong> continua sendo uma das placas mais procuradas da NVIDIA e entrega <strong>desempenho de sobra para rodar jogos em Full HD no Ultra</strong>. Se você já usa aplicações que pedem mais poder (edição, criação, streaming), é o degrau certo acima da RX 7600.</p>
<p>A má notícia é o preço: a nova realidade é <strong>R$ 2.500</strong>. Antes ela aparecia a R$ 1.900-2.000, depois subiu para R$ 2.200, e hoje o preço base já é R$ 2.500 (com lojas mostrando até R$ 2.700-2.800). <strong>Não espere mais vê-la por R$ 2.000 como antes.</strong> Nessa faixa, a <strong>RX 9060 XT 16GB</strong> é uma opção melhor por desempenho e por preço.</p>

<h3>RTX 5060 Ti 8GB e 16GB — a ponte para 2K, com um problema de VRAM</h3>
<p>A <strong>RTX 5060 Ti</strong> tem desempenho um pouco maior que o da 5060 e já <strong>roda jogos em 2K</strong>. Mas ela esbarra num limite: <strong>a versão de 8 GB fica "capada"</strong> porque o armazenamento de textura complica. Ela deveria ter 16 GB.</p>
<p>A versão de <strong>16 GB</strong> resolve isso, mas o preço já é quase <strong>R$ 4.000</strong> (e subiu de R$ 3.600-3.700 na última semana — <strong>ainda vai subir mais</strong>). Com esse valor, a <strong>RX 9060 XT 16GB entrega desempenho equivalente por menos dinheiro</strong>.</p>

<h2>AMD topo de linha: RX 9070 e RX 9070 XT 16GB</h2>
<p>As placas AMD de topo são, para muita gente, a melhor compra do mercado em 2026: <strong>mais desempenho por real do que a NVIDIA equivalente</strong>.</p>
<ul>
    <li><strong>RX 9070 16GB:</strong> já aparece em promoção na <strong>faixa de R$ 4.100</strong>. É o degrau intermediário para quem quer 2K e 4K sem entrar nas cinco mil.</li>
    <li><strong>RX 9070 XT 16GB:</strong> é a <strong>melhor opção de desempenho bruto se você quer 4K e pode pagar menos que uma RTX 5070</strong>. A RTX 5070 aparece em promoções por R$ 4.700-5.000, e a RX 9070 XT já foi vista por <strong>R$ 4.829</strong> com desempenho equivalente ou melhor. A diferença é o DLSS 5, que só existe na NVIDIA.</li>
</ul>
<p>Resumo honesto: <strong>a AMD aumentou menos de preço que a NVIDIA</strong>, e isso é notório. Você entrega placas tão boas quanto as da rival, só que sem o diferencial do DLSS 5 — e esse é um ponto que não dá para ignorar.</p>

<h2>NVIDIA topo: RTX 5070, RTX 5070 Ti e RTX 5080</h2>
<h3>RTX 5070 12GB — a placa do DLSS 5 que faz sentido</h3>
<p>A <strong>RTX 5070 12GB</strong> é a placa da NVIDIA que realmente vale a pena para quem quer <strong>4K com DLSS 5</strong>. E o DLSS 5 aqui <strong>funciona de verdade</strong>, diferente das placas mais fracas: como ela tem desempenho de sobra, dá para ativar o DLSS 5 em qualidade máxima, <strong>transformando completamente o visual do jogo</strong> (personagens, cinemáticas) e a placa aguenta o tranco.</p>
<p>Comparada a uma RTX 3090, a 5070 <strong> entrega desempenho parecido ou até superior</strong>. Só que o preço é o ponto fraco: está em <strong>R$ 5.000 a R$ 5.300</strong>, e quem comprou há dois meses e meio pagou <strong>R$ 3.846</strong>. <strong>Se aparecer abaixo de R$ 4.800, é a hora de comprar</strong> — acima disso, a RX 9070 XT entrega mais por menos.</p>

<h3>RTX 5070 Ti 16GB — a elite, se o caixa permitir</h3>
<p>A <strong>RTX 5070 Ti 16GB</strong> é <strong>performance insana para rodar jogos em 4K no Ultra usando DLSS 5</strong>. Roda qualquer jogo atual sem esforço, com a tecnologia de upscaling mais avançada do mercado. É a escolha de quem não quer pensar duas vezes e tem orçamento para o topo de linha. O preço, como esperado, é o mais alto: já apareceu em <strong>R$ 6.699</strong> em promoção e circula perto de <strong>R$ 9.000</strong> nas lojas.</p>

<h3>RTX 5080 16GB — o topo absoluto</h3>
<p>A <strong>RTX 5080 16GB</strong> é a <strong>elite</strong>: desempenho ultra para rodar qualquer jogo sem esforço, com DLSS 5. Se você está nessa faixa de preço, o argumento é o mesmo da 5070 Ti — performance de topo com a melhor tecnologia disponível. <strong>Confira o preço do dia nos links abaixo</strong>: como em todo o resto deste guia, ela sofre forte variação e só vale a pena em promoção forte.</p>

<h2>RTX 5070 ou RX 9070 XT: qual das duas escolher?</h2>
<p>Esse é o duelo que mais aparece na faixa de 4 mil reais, e a resposta depende de uma única pergunta: <strong>você valoriza o DLSS 5?</strong></p>
<div class="overflow-x-auto my-6">
    <table class="w-full text-left border-collapse border border-hairline">
        <thead>
            <tr class="bg-soft text-[12px] uppercase font-bold text-mute">
                <th class="p-3 border-b border-hairline">Critério</th>
                <th class="p-3 border-b border-hairline">RTX 5070 12GB</th>
                <th class="p-3 border-b border-hairline">RX 9070 XT 16GB</th>
            </tr>
        </thead>
        <tbody class="divide-y divide-hairline text-[14px] text-body">
            <tr>
                <td class="p-3 font-semibold">Preço de mercado</td>
                <td class="p-3">R$ 5.000 – 5.300</td>
                <td class="p-3 text-success font-bold">~R$ 4.800 (em promoção)</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">Desempenho bruto</td>
                <td class="p-3">Muito bom</td>
                <td class="p-3 text-success font-bold">Ligeiramente melhor</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">Tecnologia de upscaling</td>
                <td class="p-3 text-success font-bold">DLSS 5 (topo)</td>
                <td class="p-3">FSR 4.1</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">VRAM</td>
                <td class="p-3">12 GB</td>
                <td class="p-3 text-success font-bold">16 GB</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">Veredito</td>
                <td class="p-3">Se quer a tecnologia da Nvidia</td>
                <td class="p-3">Se quer mais quadros por real</td>
            </tr>
        </tbody>
    </table>
</div>
<p><strong>Resposta:</strong> se você quer <strong>desempenho bruto e economizar</strong>, compre a <strong>RX 9070 XT</strong>. Se você quer <strong>o DLSS 5 para rodar os jogos de forma insana e aproveitar o máximo da tecnologia da NVIDIA</strong> (e não se preocupa com a desvalorização, que na NVIDIA costuma ser menor), vá de <strong>RTX 5070 ou 5070 Ti</strong>.</p>

<h2>Qual placa de vídeo escolher para cada resolução?</h2>
<p>Essa é a pergunta mais importante do guia, porque <strong>a resolução que você joga define a placa</strong>. Jogue no tamanho certo e a placa errada é dinheiro jogado fora.</p>
<div class="overflow-x-auto my-6">
    <table class="w-full text-left border-collapse border border-hairline">
        <thead>
            <tr class="bg-soft text-[12px] uppercase font-bold text-mute">
                <th class="p-3 border-b border-hairline">Sua Resolução</th>
                <th class="p-3 border-b border-hairline">Placa Recomendada</th>
                <th class="p-3 border-b border-hairline">Observação</th>
            </tr>
        </thead>
        <tbody class="divide-y divide-hairline text-[14px] text-body">
            <tr>
                <td class="p-3 font-semibold">Full HD (1080p)</td>
                <td class="p-3">RX 580 8GB (orçamento mínimo) ou RX 7600 8GB (recomendada)</td>
                <td class="p-3">A RX 7600 é a melhor compra aqui</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">Full HD no Ultra</td>
                <td class="p-3">RTX 5060 8GB ou RX 9060 XT 16GB</td>
                <td class="p-3">A 9060 XT entrega mais por menos</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">2K (1440p)</td>
                <td class="p-3"><strong>RX 9060 XT 16GB</strong> (a melhor da categoria)</td>
                <td class="p-3">VRAM de 16 GB faz toda a diferença</td>
            </tr>
            <tr>
                <td class="p-3 font-semibold">4K (2160p)</td>
                <td class="p-3">RX 9070 XT 16GB (custo-benefício) ou RTX 5070/5070 Ti (com DLSS 5)</td>
                <td class="p-3">Aqui o DLSS 5 muda o jogo</td>
            </tr>
        </tbody>
    </table>
</div>

<h2>Como saber se a oferta é boa de verdade: use o histórico de preços</h2>
<p>Com o mercado tão volátil, <strong>o preço de hoje não diz se a oferta é boa</strong> — o histórico diz. Uma placa a R$ 5.000 não é sinal de que a RTX 5070 "valorizou": é sinal de que ela <strong>subiu de preço</strong> e que o dia da compra ainda não chegou.</p>
<p>Antes de fechar a compra, confira o histórico de preço do produto. Ele mostra tanto o <strong>pago médio real</strong> quanto o <strong>menor preço já registrado</strong>. Se a oferta atual está próxima do menor histórico, é sinal bom. Se está muito acima, <strong>espere a próxima promoção</strong> — e essa é a principal razão pela qual vale a pena acompanhar os grupos de oferta: as melhores oportunidades aparecem primeiro neles.</p>
<p>Um alerta importante sobre <strong>versões de uma e duas ventoinhas</strong> e sobre placas com <strong>nomes parecidos</strong> (a 5060 de 8 GB, a 5060 Ti de 8 GB e a de 16 GB têm preços muito diferentes): confira sempre a <strong>quantidade de VRAM</strong> e o modelo exato antes de comprar.</p>

<h2>As placas que a gente não recomenda comprar agora</h2>
<p>Um guia honesto também precisa dizer o que <strong>não</strong> comprar. Nestas condições:</p>
<ul>
    <li><strong>RTX 5060 8GB a R$ 2.700+:</strong> neste preço, a RX 9060 XT 16GB entrega mais desempenho por menos dinheiro.</li>
    <li><strong>RTX 5060 Ti 16GB a R$ 4.000:</strong> o desempenho não se justifica nesse valor. Espere a queda ou vá de RX 9060 XT.</li>
    <li><strong>RTX 5070 12GB a R$ 5.300:</strong> é cara demais. O preço justo de promoção fica abaixo de R$ 4.800 — e ainda pode cair.</li>
    <li><strong>Qualquer placa de 4 GB de VRAM:</strong> em 2026, 4 GB não é mais suficiente para jogos atuais. Não vale a pena, nem barato.</li>
    <li><strong>RTX 5050 de uma ventoinha:</strong> só se o gabinete for realmente pequeno. Não é uma economia, é uma limitação.</li>
</ul>
"""

CONCLUSION = """
<p><strong>Qual placa de vídeo comprar em 2026, o veredito final:</strong></p>
<ul>
    <li><strong>Melhor custo-benefício geral:</strong> Radeon RX 7600 8GB — a melhor placa para Full HD, com FSR 4.1 e sem dor de cabeça.</li>
    <li><strong>Melhor preço por quadro:</strong> Radeon RX 9060 XT 16GB — a rainha do guia. Desempenho de RTX 5060 Ti 16GB por menos que a versão de 8 GB.</li>
    <li><strong>Melhor para 4K com custo-benefício:</strong> Radeon RX 9070 XT 16GB — mais desempenho bruto que a RTX 5070, por menos.</li>
    <li><strong>Melhor com DLSS 5:</strong> RTX 5070 12GB — só compensa abaixo de R$ 4.800.</li>
    <li><strong>Melhor topo de linha:</strong> RTX 5070 Ti 16GB — 4K no Ultra com a melhor tecnologia do mercado.</li>
    <li><strong>Melhor para orçamento apertado:</strong> RX 580 8GB por ~R$ 600 — sabendo que é uma placa antiga, com limitações.</li>
    <li><strong>Melhor Nvidia de entrada:</strong> RTX 5050 8GB — na faixa de R$ 1.900, e só nessa faixa.</li>
</ul>
<p>O conselho mais importante deste guia é simples: <strong>não compre no impulso e não pague o preço de hoje sem comparar o histórico</strong>. As placas continuam subindo, e a próxima promoção é sempre uma questão de dias. Escolha uma das opções acima, acompanhe o histórico de preço e compre na hora certa.</p>
<p>Comprando pelos links deste guia você ajuda o André Indica a continuar trazendo análises honestas, sem custo adicional para você.</p>
"""

# FAQ: alimenta o bloco visivel "Perguntas Frequentes" e o schema.org/FAQPage (GEO)
FAQ = [
    {
        'question': 'Qual é a melhor placa de vídeo custo-benefício em 2026?',
        'answer': 'A Radeon RX 7600 8GB é a melhor placa de custo-benefício de 2026. Ela entrega desempenho de sobra para rodar qualquer jogo atual em Full HD, tem 8 GB de VRAM e se beneficia do FSR 4.1, e aparece na faixa de R$ 1.700 a R$ 2.000. Se você quer ainda mais quadros por real, a Radeon RX 9060 XT 16GB é a melhor compra do guia, com desempenho equivalente a uma RTX 5060 Ti 16GB por menos dinheiro.',
    },
    {
        'question': 'RX 7600 ou RTX 5060: qual comprar?',
        'answer': 'As duas têm desempenho muito parecido em Full HD — a AMD ganha em alguns jogos e a NVIDIA em outros. A RX 7600 é a escolha certa se você quer economizar, porque aparece na faixa de R$ 1.700 a R$ 2.000. A RTX 5060 faz sentido se você quer rodar em Full HD no preset Ultra ou usa aplicações que pedem mais poder, mas prepare para pagar mais: o preço de mercado dela é de R$ 2.500. Para a maioria das pessoas, a RX 7600 sai mais barato e entrega praticamente o mesmo.',
    },
    {
        'question': '8 GB de VRAM ainda bastam em 2026?',
        'answer': 'Bastam para jogar em Full HD, sim — por isso a RX 7600 8GB é uma ótima compra. A partir de 2K, a história muda: 8 GB começa a apertar, as texturas perdem nitidez e aparecem engasgos (stuttering) nos jogos mais pesados. Se você joga em 2K ou 4K, o ideal é 16 GB de VRAM, e é por isso que a RX 9060 XT 16GB e a RX 9070 XT 16GB são as recomendaciones para essas resoluções. Evite qualquer placa de 4 GB.',
    },
    {
        'question': 'AMD ou NVIDIA: qual é melhor em 2026?',
        'answer': 'Depende do seu orçamento e da sua resolução. Em termos de preço por desempenho, a AMD está ganhando: em 2026 as placas Radeon subiram menos de preço e entregam desempenho equivalente ou melhor, com mais VRAM pelo mesmo valor. A NVIDIA tem o diferencial do DLSS 5, exclusivo das RTX 50, que é uma tecnologia revolucionária de upscaling. A regra prática é esta: quer o máximo de quadros por real? AMD. Quer aproveitar o DLSS 5 e uma possível desvalorização menor no futuro? NVIDIA.',
    },
    {
        'question': 'Qual é a melhor placa de vídeo para jogar em 4K?',
        'answer': 'Para 4K com custo-benefício, a Radeon RX 9070 XT 16GB é a melhor opção: entrega mais desempenho bruto que a RTX 5070 12GB e aparece por menos. Se você quer aproveitar o DLSS 5 para transformar o visual dos jogos e rodar 4K no Ultra com folga, a RTX 5070 12GB (abaixo de R$ 4.800) ou a RTX 5070 Ti 16GB são as escolhas certas. Com uma RTX 5060 ou inferior, 4K é possível, mas você vai depender muito de upscaling para ficar confortável.',
    },
    {
        'question': 'RTX 5070 ou RX 9070 XT: qual vale mais a pena?',
        'answer': 'Se você valoriza desempenho bruto e quer economizar, compre a RX 9070 XT 16GB: ela entrega desempenho equivalente ou superior à RTX 5070 e costuma aparecer mais barata. Se você quer aproveitar o DLSS 5, a tecnologia de upscaling mais avançada do mercado, e não se preocupa em pagar um pouco mais, vá de RTX 5070 12GB. A RTX 5070 tem o ponto fraco do preço: está na faixa de R$ 5.000, e o preço justo de promoção fica abaixo de R$ 4.800.',
    },
    {
        'question': 'Quanto devo gastar em uma placa de vídeo em 2026?',
        'answer': 'Depende da sua resolução. Para Full HD, a faixa de R$ 1.700 a R$ 2.000 (RX 7600) é o ponto ideal. Para rodar em Full HD no Ultra ou em 2K, a faixa de R$ 3.100 a R$ 3.300 (RX 9060 XT 16GB) entrega o melhor resultado. Para 4K, a partir de R$ 4.800 (RX 9070 XT ou RTX 5070). Abaixo de R$ 1.000, a única opção que faz sentido é a antiga RX 580 8GB, com as limitações que isso traz.',
    },
    {
        'question': 'A placa RX 580 8GB ainda vale a pena?',
        'answer': 'Vale se — e somente se — o seu orçamento for muito apertado. A RX 580 8GB ainda roda uma boa lista de jogos em Full HD e aparece por cerca de R$ 600 em promoção. Mas é um produto antigo: jogos atuais de grande porte podem não rodar, e ela não tem as tecnologias de upscaling modernas. Com os 8 GB de VRAM, ela ainda é uma boa porta de entrada. Se o seu orçamento chegar a R$ 1.700, migre para a RX 7600.',
    },
    {
        'question': 'O que significa DLSS 5 e FSR 4.1 nas placas de 2026?',
        'answer': 'São tecnologias de upscaling: elas aumentam a resolução interna do jogo e reconstroem a imagem final, entregando mais quadros por menos poder de processamento. O DLSS 5, exclusivo das placas NVIDIA RTX 50, é o mais avançado, mas exige uma placa forte — em GPUs fracas ele derruba muito a taxa de quadros. O FSR 4.1, da AMD, é aberto e roda em qualquer placa, e foi justamente ele que melhorou bastante o desempenho da RX 7600.',
    },
]

ITEMS = [
    {
        'position': 1,
        'name': 'AMD Radeon RX 580 8GB (2048SP)',
        'slug': 'rx-580-8gb',
        'description': (
            '<p>A <strong>Radeon RX 580 8GB</strong> é a única placa de vídeo abaixo de R$ 1.000 que ainda faz sentido em 2026. Com 8 GB de VRAM e desempenho suficiente para Full HD, ela aparece em promoção na <strong>faixa dos R$ 600</strong> — com estoque nacional e parcelamento em até 10x sem juros.</p>'
            '<p>Ela roda uma lista razoável de jogos e os 8 GB de VRAM ainda evitam engasgos em Full HD. Mas seja honesto com você mesmo: <strong>é um produto antigo</strong>, com limitações reais. Jogos atuais de grande porte podem não rodar, e não há upscaling moderno. Compre sabendo disso — é uma placa para gastar pouco e se divertir, não para buscar desempenho de topo.</p>'
        ),
        'pros': (
            'Menor preço de placa de vídeo que ainda roda jogos\n'
            '8 GB de VRAM, suficiente para Full HD\n'
            'Estoque nacional, com frete rápido e 10x sem juros\n'
            'Consome pouca energia (boa para fontes modestas)'
        ),
        'cons': (
            'Produto antigo, sem suporte a DLSS/FSR modernos\n'
            'Jogos atuais de grande porte podem não rodar\n'
            'Desempenho bem abaixo das concorrentes atuais'
        ),
        'aliexpress': 'https://s.click.aliexpress.com/e/_c3dkaEvF',
    },
    {
        'position': 2,
        'name': 'AMD Radeon RX 7600 8GB',
        'slug': 'rx-7600-8gb',
        'description': (
            '<p>A <strong>RX 7600 8GB</strong> é a <strong>melhor placa de vídeo custo-benefício de 2026</strong>. É a placa que entrega o melhor desempenho por real gasto e não faz você pensar duas vezes na compra: <strong>solução gastando ainda pouco</strong>.</p>'
            '<p>O grande ganho veio com o <strong>FSR 4.1</strong>, que deu um upgrade real de performance na RX 7600. Com ele ligado, você tem ótimo desempenho em praticamente qualquer jogo que abrir, em Full HD. Para dimensionar: um <strong>PC completo com RX 7600</strong> (Ryzen 5 5500, fonte, SSD e tudo) apareceu por <strong>cerca de R$ 4.000</strong> — o valor de uma placa 5060 sozinha.</p>'
            '<p>O preço de mercado está na <strong>faixa de R$ 1.700 a R$ 2.000</strong>, e ela aparece com frequência abaixo disso em promoção.</p>'
        ),
        'pros': (
            'Melhor relação custo-benefício de todo o guia\n'
            '8 GB de VRAM e FSR 4.1 para Full HD sem engasgos\n'
            'Roda qualquer jogo atual em Full HD com folga\n'
            'Custa menos que uma placa Nvidia equivalente'
        ),
        'cons': (
            'Não tem o DLSS 5 exclusivo das RTX 50\n'
            '8 GB de VRAM começa a apertar se você for para 2K/4K'
        ),
        'amazon': 'https://www.amazon.com.br/ASRock-RX7600-CL-8GO-Challenger/dp/B0C626FFG2?tag=andre0cda-20',
        'ml': 'https://www.mercadolivre.com.br/placa-de-video-xfx-radeon-rx-7600-swft210-8gb-gddr6-128-bit/p/MLB28570288?matt_tool=83406274&matt_word=camilamartinstar',
    },
    {
        'position': 3,
        'name': 'Intel Arc B580 12GB',
        'slug': 'intel-arc-b580-12gb',
        'description': (
            '<p>A <strong>Intel Arc B580 12GB</strong> é a surpresa do orçamento. Ter <strong>12 GB de VRAM</strong> numa placa de entrada é raro, e isso evita os engasgos de textura que atingem as concorrentes de 8 GB — um problema real em 2026.</p>'
            '<p>Na prática ela é concorrente direta da RX 7600 e da RTX 5050 em Full HD. Leve em conta apenas que a Intel ainda pede <strong>drivers mais recentes</strong> para tirar o máximo de proveito, e que o catálogo de jogos otimizados é menor. Se o seu orçamento é curto e a prioridade é ter VRAM de sobra, vale muito a pena considerar.</p>'
        ),
        'pros': (
            '12 GB de VRAM, mais que as concorrentes de entrada\n'
            'Preço competitivo para a faixa de 8 GB\n'
            'Bom desempenho em Full HD\n'
            'Consumo baixo para uma placa com tanta VRAM'
        ),
        'cons': (
            'Exige drivers recentes da Intel para bom desempenho\n'
            'Menos jogos otimizados que AMD e NVIDIA\n'
            'Ecossistema ainda em amadurecimento'
        ),
        'shopee': 'https://s.shopee.com.br/7VGgHlSmo5',
    },
    {
        'position': 4,
        'name': 'NVIDIA GeForce RTX 5050 8GB',
        'slug': 'rtx-5050-8gb',
        'description': (
            '<p>A <strong>RTX 5050 8GB</strong> é a porta de entrada da NVIDIA e entrega <strong>desempenho praticamente igual ao da RX 7600</strong>: as duas rodam os mesmos jogos com FPS bem semelhantes, e cada uma ganha em títulos específicos.</p>'
            '<p>Ela apareceu historicamente na <strong>faixa de R$ 1.700 a R$ 1.900</strong> (e já foi vista mais barato ainda), mas em várias lojas está sendo vendida a <strong>R$ 2.300 ou mais</strong>. <strong>Compre só na faixa de R$ 1.900, no máximo R$ 2.000</strong> — acima disso a RX 7600 entrega mais pelo mesmo preço. E atenção à versão de <strong>uma única ventoinha</strong>: ela só faz sentido se o seu gabinete for muito pequeno.</p>'
        ),
        'pros': (
            'Desempenho equivalente ao da RX 7600\n'
            'Acesso ao DLSS 5 da Nvidia\n'
            'Preço competitivo quando aparece em promoção\n'
            'Boas opções de chipset e tamanho compacto'
        ),
        'cons': (
            'Preço inflado em muitas lojas (R$ 2.300+)\n'
            'Atenção à versão de ventoinha única\n'
            'Sem ganho de desempenho sobre a RX 7600 pelo preço'
        ),
        'shopee': 'https://s.shopee.com.br/70KPgqHYkA',
        'extra_link': '<p><a href="https://s.shopee.com.br/1qcJXLk62c" target="_blank" rel="nofollow">Ver oferta alternativa na Shopee</a></p>',
    },
    {
        'position': 5,
        'name': 'NVIDIA GeForce RTX 5060 8GB',
        'slug': 'rtx-5060-8gb',
        'description': (
            '<p>A <strong>RTX 5060 8GB</strong> é uma das placas mais procuradas da NVIDIA e entrega <strong>desempenho de sobra para rodar jogos em Full HD no preset Ultra</strong>. Se você já usa aplicações que pedem mais poder (edição, criação, streaming), é o degrau certo acima da RX 7600.</p>'
            '<p>A má notícia é o preço: a nova realidade é <strong>R$ 2.500</strong>. Antes aparecia a R$ 1.900-2.000, depois subiu para R$ 2.200, e hoje o preço base já é R$ 2.500 — com lojas mostrando até R$ 2.700-2.800. <strong>Não espere mais vê-la por R$ 2.000 como antes.</strong> Nessa faixa de preço, a RX 9060 XT 16GB é uma opção melhor por desempenho e por preço.</p>'
        ),
        'pros': (
            'Full HD no preset Ultra com sobra\n'
            'Acesso ao DLSS 5 da Nvidia\n'
            'Boa opção para além de jogos (edição e criação)\n'
            'Várias lojas com estoque e parcelamento'
        ),
        'cons': (
            'Preço subiu muito: R$ 2.500 a R$ 2.800\n'
            'A RX 9060 XT 16GB entrega mais por menos nesse valor\n'
            '8 GB de VRAM limita o uso em 2K/4K'
        ),
        'shopee': 'https://s.shopee.com.br/2gBQWsu3Qf',
        'aliexpress': 'https://s.click.aliexpress.com/e/_c3DcvfFJ',
        'extra_link': '<p><a href="https://s.shopee.com.br/7fa6U4fYaJ" target="_blank" rel="nofollow">Ver oferta alternativa na Shopee</a></p>',
    },
    {
        'position': 6,
        'name': 'NVIDIA GeForce RTX 5060 Ti 8GB',
        'slug': 'rtx-5060-ti-8gb',
        'description': (
            '<p>A <strong>RTX 5060 Ti 8GB</strong> tem desempenho um pouco maior que o da RTX 5060 e já <strong>roda jogos em 2K</strong>. Recentemente saiu por <strong>R$ 2.700</strong> em 12x sem juros, o que é um preço interessante.</p>'
            '<p>O porém é claro: <strong>os 8 GB de VRAM a limitam</strong>. Ela deveria ter 16 GB, e é justamente aí que o armazenamento de textura complica. A performance é muito boa e os jogos em 2K rodam bem, mas você vai sentir o teto da VRAM nos títulos mais pesados.</p>'
        ),
        'pros': (
            'Roda jogos em 2K com boa performance\n'
            'Preço interessante quando aparece em promoção\n'
            'Acesso ao DLSS 5\n'
            'Um degrau acima da RTX 5060'
        ),
        'cons': (
            'Limitada a 8 GB de VRAM\n'
            'A versão de 16 GB custa quase R$ 4.000\n'
            'Para 2K, a RX 9060 XT 16GB é melhor opção'
        ),
        'shopee': 'https://s.shopee.com.br/7KxG5Sl9mT',
        'extra_link': '<p><a href="https://s.shopee.com.br/5VVbu5wXHc" target="_blank" rel="nofollow">Ver oferta alternativa na Shopee</a></p>',
    },
    {
        'position': 7,
        'name': 'AMD Radeon RX 9060 XT 16GB',
        'slug': 'rx-9060-xt-16gb',
        'description': (
            '<p>A <strong>RX 9060 XT 16GB</strong> é, na nossa visão, <strong>a melhor placa de vídeo do guia</strong>: o melhor preço por quadro que existe hoje. Ela tem <strong>o mesmo desempenho de uma RTX 5060 Ti 16GB</strong>, sendo que está custando quase o preço da versão de <strong>8 GB</strong> da concorrente.</p>'
            '<p>É por isso que ela já tem muita procura: <strong>as placas estão subindo sem parar</strong>, e essa se destaca por ser muito boa pelo preço que está custando. <strong>Roda qualquer jogo da atualidade em 2K, praticamente no Ultra</strong> — não todos os jogos no Ultra, mas uma boa parte.</p>'
            '<p>Aparece por <strong>R$ 3.299 à vista</strong> e já foi vista por <strong>R$ 3.096</strong> em promoção recente. Se você quer o máximo de desempenho por real, é a compra certa.</p>'
        ),
        'pros': (
            'Melhor preço por quadro do guia\n'
            'Desempenho equivalente a uma RTX 5060 Ti 16GB\n'
            '16 GB de VRAM: roda 2K no Ultra com folga\n'
            'Custa quase o preço da RTX 5060 Ti de 8 GB'
        ),
        'cons': (
            'Não tem o DLSS 5 exclusivo da Nvidia\n'
            'Preço pode subir, como todas as placas de 16 GB'
        ),
        'shopee': 'https://s.shopee.com.br/7ptWgNs7ao',
        'extra_link': '<p><a href="https://s.shopee.com.br/2gBQWtFz4a" target="_blank" rel="nofollow">Ver oferta alternativa na Shopee</a></p>',
    },
    {
        'position': 8,
        'name': 'AMD Radeon RX 9070 16GB',
        'slug': 'rx-9070-16gb',
        'description': (
            '<p>A <strong>RX 9070 16GB</strong> é o degrau de entrada da linha topo da AMD, e aparece em <strong>promoções na faixa de R$ 4.100</strong>. Para quem quer jogar em 2K e 4K com 16 GB de VRAM sem precisar entrar nas cinco mil, ela é uma escolha sólida.</p>'
            '<p>É também a porta de entrada para a faixa de desempenho da RTX 5070, já que a 9070 XT entrega um degrau acima. Lembre-se que a <strong>AMD tem subido menos de preço que a Nvidia</strong>, o que torna essa linha especialmente interessante em 2026.</p>'
        ),
        'pros': (
            '16 GB de VRAM para 2K e 4K\n'
            'Promoções na faixa de R$ 4.100\n'
            'Subiu menos de preço que a concorrência Nvidia\n'
            'Boa porta de entrada para o topo de linha AMD'
        ),
        'cons': (
            'Sem DLSS 5\n'
            'A RX 9070 XT entrega mais pelo mesmo preço em promoção\n'
            'Ainda exige placa-mãe e fonte de qualidade'
        ),
        'shopee': 'https://s.shopee.com.br/BU5YIYIjI',
        'extra_link': '<p><a href="https://s.shopee.com.br/80Cwsh8sbc" target="_blank" rel="nofollow">Ver oferta alternativa na Shopee</a></p>',
    },
    {
        'position': 9,
        'name': 'NVIDIA GeForce RTX 5070 12GB',
        'slug': 'rtx-5070-12gb',
        'description': (
            '<p>A <strong>RTX 5070 12GB</strong> é a placa da NVIDIA que realmente faz sentido para quem quer <strong>4K com DLSS 5</strong> — e aqui o DLSS 5 funciona de verdade, diferente das placas mais fracas. Como ela tem desempenho de sobra, dá para ativar o DLSS 5 em qualidade máxima, <strong>transformando completamente o visual do jogo</strong> (personagens, cinemáticas) e a placa aguenta o tranco.</p>'
            '<p>Comparada a uma RTX 3090, ela <strong>entrega desempenho parecido ou até superior</strong>, e já roda jogos em 4K. O problema é o preço: está em <strong>R$ 5.000 a R$ 5.300</strong>, e quem comprou há dois meses e meio pagou <strong>R$ 3.846</strong>. <strong>Se aparecer abaixo de R$ 4.800, é a hora de comprar</strong> — acima disso, a RX 9070 XT entrega mais por menos.</p>'
        ),
        'pros': (
            'DLSS 5 funciona muito bem nesta placa\n'
            'Roda jogos em 4K com folga\n'
            'Desempenho parecido ou superior a uma RTX 3090\n'
            'Tecnologias mais recentes da Nvidia'
        ),
        'cons': (
            'Preço inflado: R$ 5.000 a R$ 5.300\n'
            'Só compensa abaixo de R$ 4.800 em promoção\n'
            'A RX 9070 XT entrega mais por menos'
        ),
        'shopee': 'https://s.shopee.com.br/6q0zUYHn1B',
        'extra_link': '<p><a href="https://s.shopee.com.br/9V1kfSBy8D" target="_blank" rel="nofollow">Ver oferta alternativa na Shopee</a></p>',
    },
    {
        'position': 10,
        'name': 'NVIDIA GeForce RTX 5060 Ti 16GB',
        'slug': 'rtx-5060-ti-16gb',
        'description': (
            '<p>A <strong>RTX 5060 Ti 16GB</strong> resolve o problema de VRAM da versão de 8 GB: com <strong>16 GB</strong>, os jogos em 2K rodam com folga e sem engasgos de textura. É o degrau de entrada da Nvidia para quem quer 2K com VRAM de sobra.</p>'
            '<p>Só que o preço já chegou a <strong>quase R$ 4.000</strong> (há cerca de dez dias estava na faixa de R$ 3.600-3.700) — e, pelo que o mercado está fazendo, <strong>ainda vai subir mais</strong>. Com esse valor, a <strong>RX 9060 XT 16GB entrega desempenho equivalente por menos dinheiro</strong>. Fique esperto se a planejar comprar.</p>'
        ),
        'pros': (
            '16 GB de VRAM para 2K sem engasgos\n'
            'Roda jogos em 2K com boa performance\n'
            'Acesso ao DLSS 5\n'
            'Resolução do problema de VRAM da versão de 8 GB'
        ),
        'cons': (
            'Preço alto, perto de R$ 4.000, e subindo\n'
            'A RX 9060 XT 16GB entrega mais por menos\n'
            'Não é a melhor opção para 4K nessa faixa'
        ),
        'shopee': 'https://s.shopee.com.br/4qFv6sCCij',
        'extra_link': '<p><a href="https://s.shopee.com.br/40go7LJqSG" target="_blank" rel="nofollow">Ver oferta alternativa na Shopee</a></p>',
    },
    {
        'position': 11,
        'name': 'AMD Radeon RX 9070 XT 16GB',
        'slug': 'rx-9070-xt-16gb',
        'description': (
            '<p>A <strong>RX 9070 XT 16GB</strong> é a <strong>melhor opção de desempenho bruto se você quer 4K e pode pagar menos que uma RTX 5070</strong>. Ela já apareceu em <strong>R$ 4.829</strong> em promoções recentes, e entrega desempenho equivalente ou superior à RTX 5070 pelo mesmo preço ou menos.</p>'
            '<p>É a alternativa mais inteligente para quem busca desempenho puro sem se prender ao DLSS 5. Em resumo: <strong>se você quer gastar menos e ter desempenho bruto, RX 9070 XT</strong>. A única coisa que você perde em relação à RTX 5070 é o DLSS 5 — o upscaling exclusivo da Nvidia. Tudo mais, você entrega mais quadros por real.</p>'
        ),
        'pros': (
            'Mais desempenho bruto que a RTX 5070 pelo mesmo preço\n'
            '16 GB de VRAM para 4K com folga\n'
            'Promoções vistas a partir de R$ 4.829\n'
            'Melhor custo-benefício da faixa de 4K'
        ),
        'cons': (
            'Não tem o DLSS 5 exclusivo da Nvidia\n'
            'A RX 9070 XT subiu menos que a Nvidia, mas ainda é cara'
        ),
        'shopee': 'https://s.shopee.com.br/4fwUuZYyX4',
        'extra_link': '<p><a href="https://s.shopee.com.br/8AWN50Q3Cq" target="_blank" rel="nofollow">Ver oferta alternativa na Shopee</a></p>',
    },
    {
        'position': 12,
        'name': 'NVIDIA GeForce RTX 5070 Ti 16GB',
        'slug': 'rtx-5070-ti-16gb',
        'description': (
            '<p>A <strong>RTX 5070 Ti 16GB</strong> é a <strong>elite</strong>: performance insana para rodar jogos em <strong>4K no Ultra usando DLSS 5</strong>. É uma placa diferenciada — roda qualquer jogo da atualidade sem esforço, com a tecnologia de upscaling mais avançada do mercado.</p>'
            '<p>Como esperado, o preço é o mais alto: já apareceu em <strong>R$ 6.699</strong> em promoção e circula perto de <strong>R$ 9.000</strong> nas lojas. É a escolha de quem quer o máximo da tecnologia Nvidia, não se preocupa com desvalorização e tem o orçamento para o topo de linha. Se for economizar, a <strong>RX 9070 XT</strong> entrega uma performance tão boa por menos.</p>'
        ),
        'pros': (
            '4K no Ultra com DLSS 5, sem esforço\n'
            '16 GB de VRAM para 4K com folga\n'
            'A melhor tecnologia de upscaling do mercado\n'
            'Desvaloriza menos que a concorrência (segundo a experiência do mercado)'
        ),
        'cons': (
            'Preço muito alto, de R$ 6.700 a R$ 9.000\n'
            'Performance bruta similar à RX 9070 XT\n'
            'Para desempenho puro, a AMD entrega mais por menos'
        ),
        'shopee': 'https://s.shopee.com.br/4Vd4iGiCcV',
        'extra_link': '<p><a href="https://s.shopee.com.br/5LCBhnjZES" target="_blank" rel="nofollow">Ver oferta alternativa na Shopee</a></p>',
    },
    {
        'position': 13,
        'name': 'NVIDIA GeForce RTX 5080 16GB',
        'slug': 'rtx-5080-16gb',
        'description': (
            '<p>A <strong>RTX 5080 16GB</strong> é o <strong>topo absoluto</strong>: performance ultra para rodar qualquer jogo sem esforço, com DLSS 5. Se você está na faixa de preço do topo de linha, o argumento é o mesmo da RTX 5070 Ti — o máximo de desempenho com a melhor tecnologia disponível.</p>'
            '<p>Como em todo o resto deste guia, ela sofre <strong>forte variação de preço</strong> e só vale a pena em promoção forte. <strong>Confira o preço do dia nos links abaixo</strong> e compare com o histórico antes de decidir. E lembre-se: se a sua prioridade for desempenho por real, a RX 9070 XT continua sendo uma opção mais inteligente.</p>'
        ),
        'pros': (
            'Topo de linha em desempenho bruto\n'
            'DLSS 5 para transformar o visual dos jogos\n'
            'Roda qualquer jogo da atualidade em 4K sem esforço\n'
            '16 GB de VRAM'
        ),
        'cons': (
            'Preço elevado, com forte variação\n'
            'Performance bruta similar à 5070 Ti\n'
            'Custo-benefício desfavorável frente às AMD'
        ),
        'shopee': 'https://s.shopee.com.br/7fa6U5f5HS',
        'extra_link': '<p><a href="https://s.shopee.com.br/5LCBhnsMpi" target="_blank" rel="nofollow">Ver oferta alternativa na Shopee</a></p>',
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
    draw.rectangle([(0, 0), (int(width * 0.03), height)], fill=(118, 185, 0))
    try:
        font_title = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', int(height * 0.07))
        font_sub = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', int(height * 0.035))
    except OSError:
        font_title = ImageFont.load_default()
        font_sub = font_title
    for i, line in enumerate(title.split('\n')[:2]):
        bbox = draw.textbbox((0, 0), line, font=font_title)
        tw = bbox[2] - bbox[0]
        draw.text(((width - tw) / 2, height * 0.36 + i * (height * 0.085)), line,
                  fill=(255, 255, 255), font=font_title)
    if subtitle:
        bbox = draw.textbbox((0, 0), subtitle, font=font_sub)
        tw = bbox[2] - bbox[0]
        draw.text(((width - tw) / 2, height * 0.66), subtitle, fill=(253, 186, 116), font=font_sub)
    _ = accent
    img.save(path, format='WEBP', quality=82)


def create_main_image():
    path = os.path.join(settings.MEDIA_ROOT, 'guides', 'main', f'{SLUG}.webp')
    _make_placeholder(
        path, 1280, 720,
        'Melhores Placas\nde Video 2026',
        'RX 7600 • RTX 5060 • RX 9060 XT • RTX 5070',
    )
    return f'guides/main/{SLUG}.webp'


def create_item_image(slug, name):
    path = os.path.join(settings.MEDIA_ROOT, 'guides', 'items', f'{slug}.webp')
    _make_placeholder(path, 800, 800, name, 'André Indica')
    return f'guides/items/{slug}.webp'


def main():
    category, _ = Category.objects.get_or_create(
        slug='placas-de-video',
        defaults={'name': 'Placas de Vídeo', 'icon': 'icon-gpu'},
    )
    author = User.objects.filter(username='admin').first() or User.objects.first()

    guide, created = Guide.objects.get_or_create(
        slug=SLUG,
        defaults={
            'title': TITLE,
            'category': category,
            'author': author,
            'excerpt': EXCERPT,
            'content': CONTENT.strip(),
            'conclusion': CONCLUSION.strip(),
            'faq': FAQ,
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
        guide.content = CONTENT.strip()
        guide.conclusion = CONCLUSION.strip()
        guide.faq = FAQ
        guide.main_image = create_main_image()
        guide.is_published = True
        guide.is_featured = True
        guide.save()

    GuideItem.objects.filter(guide=guide).delete()
    for item in ITEMS:
        description = item['description'] + item.get('extra_link', '')
        GuideItem.objects.create(
            guide=guide,
            product=None,
            position=item['position'],
            name=item['name'],
            description=description,
            image=create_item_image(item['slug'], item['name']),
            amazon_link=item.get('amazon'),
            mercadolivre_link=item.get('ml'),
            shopee_link=item.get('shopee'),
            aliexpress_link=item.get('aliexpress'),
            kabum_link=item.get('kabum'),
            pros=item['pros'],
            cons=item['cons'],
        )

    print('Guia criado/atualizado:')
    print(f'  URL (local): http://127.0.0.1:8000/guia/{guide.slug}/')
    print(f'  Itens: {guide.items.count()}')
    print(f'  FAQ: {len(guide.faq_items)} perguntas')
    print(f'  Imagem principal: {guide.main_image.name}')
    print('  (lembre: troque as imagens placeholder pelas fotos reais dos produtos)')


if __name__ == '__main__':
    main()
