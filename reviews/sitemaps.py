from django.contrib.sitemaps import Sitemap
from .models import Review, Category, Comparison, Guide

class ReviewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Review.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Category.objects.all()

class ComparisonSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Comparison.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

class GuideSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Guide.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at
