from django.db.models import Q
from .models import Category

def categories_processor(request):
    """Disponibiliza no menu apenas categorias que possuam conteúdo publicado."""
    try:
        categories = Category.objects.filter(
            Q(products__reviews__is_published=True) |
            Q(products__comparisons_as_first__is_published=True) |
            Q(products__comparisons_as_second__is_published=True) |
            Q(guides__is_published=True)
        ).distinct().order_by('name')
        return {'nav_categories': list(categories)}
    except Exception:
        return {'nav_categories': []}

