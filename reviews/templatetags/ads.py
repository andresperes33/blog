from django import template
from django.conf import settings
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def ad_slot(position, wrapper_class='ad-slot my-8'):
    """Renderiza uma unidade de anuncio do AdSense.

    Uso:  {% load ads %}{% ad_slot "top" %}

    Se a unidade correspondente nao estiver configurada em settings
    (ADSENSE_SLOT_<POSITION>), nada e renderizado.
    """
    slot = getattr(settings, f'ADSENSE_SLOT_{position.upper()}', '').strip()
    client = getattr(settings, 'ADSENSE_CLIENT', '').strip()

    if not slot or not client:
        return ''

    html = (
        f'<aside class="{escape(wrapper_class)}" aria-label="Publicidade">'
        f'<ins class="adsbygoogle" style="display:block"'
        f' data-ad-client="{escape(client)}"'
        f' data-ad-slot="{escape(slot)}"'
        f' data-ad-format="auto"'
        f' data-full-width-responsive="true"></ins>'
        f'<script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>'
        f'</aside>'
    )
    return mark_safe(html)
