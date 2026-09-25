from django.http import HttpResponsePermanentRedirect

CANONICAL_HOST = 'andreindicatech.com.br'
WWW_HOST = f'www.{CANONICAL_HOST}'

# Nao redirecionar estes caminhos: EasyPanel/Let's Encrypt validam o
# certificado neste path e um 301 aqui quebraria a renovacao.
ACME_PREFIX = '/.well-known/acme-challenge/'


class CanonicalHostMiddleware:
    """Redireciona www.andreindicatech.com.br para o host canonico com 301.

    Sem isso as duas variantes respondiam 200 com o mesmo HTML, o que
    duplica o conteudo e divide os sinais de SEO. O canonical tag sozinho
    nao resolve: o Google ainda baixa as duas URLs.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(ACME_PREFIX):
            return self.get_response(request)

        host = request.get_host().partition(':')[0].lower()
        if host == WWW_HOST:
            scheme = 'https' if request.is_secure() else 'http'
            target = f'{scheme}://{CANONICAL_HOST}{request.get_full_path()}'
            return HttpResponsePermanentRedirect(target)

        return self.get_response(request)
