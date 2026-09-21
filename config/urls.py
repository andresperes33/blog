from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import TemplateView, RedirectView

from django.contrib.sitemaps.views import sitemap
from reviews.sitemaps import ReviewSitemap, CategorySitemap, ComparisonSitemap, GuideSitemap, StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'reviews': ReviewSitemap,
    'categories': CategorySitemap,
    'comparisons': ComparisonSitemap,
    'guides': GuideSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', serve, {'document_root': settings.STATIC_ROOT, 'path': 'img/favicon.ico'}),
    # Redirecionamentos 301 de URLs alternativas frequentes para evitar 404 no Googlebot
    path('politica-de-privacidade/', RedirectView.as_view(url='/privacidade/', permanent=True)),
    path('politica-cookies/', RedirectView.as_view(url='/politica-de-cookies/', permanent=True)),
    path('termos/', RedirectView.as_view(url='/termos-de-uso/', permanent=True)),
    path('termo-de-uso/', RedirectView.as_view(url='/termos-de-uso/', permanent=True)),
    path('politica-de-privacidade-e-cookies/', RedirectView.as_view(url='/privacidade/', permanent=True)),
    path('', include('reviews.urls')),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('ads.txt', TemplateView.as_view(template_name="ads.txt", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
        *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    ]
