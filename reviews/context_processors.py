from .models import Category

def categories_processor(request):
    """Disponibiliza as categorias globalmente para navegação e menus."""
    try:
        categories = list(Category.objects.all().order_by('name'))
        return {'nav_categories': categories}
    except Exception:
        return {'nav_categories': []}

