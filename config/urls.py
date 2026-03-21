from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import TemplateView

from django.contrib.sitemaps.views import sitemap
from reviews.sitemaps import ReviewSitemap, CategorySitemap, ComparisonSitemap, GuideSitemap

sitemaps = {
    'reviews': ReviewSitemap,
    'categories': CategorySitemap,
    'comparisons': ComparisonSitemap,
    'guides': GuideSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('ads.txt', TemplateView.as_view(template_name="ads.txt", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
