from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.db.models import Q
from .models import Review, Category, Comparison, Guide

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return [
            'index', 'all_reviews', 'all_categories', 'comparison_list',
            'guide_list', 'about', 'contact', 'privacy', 'terms',
            'cookie_policy', 'disclaimer', 'transparency',
        ]

    def location(self, item):
        return reverse(f'reviews:{item}')

    def priority(self, item):
        return 1.0 if item == 'index' else 0.5

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
        return Category.objects.filter(
            Q(products__reviews__is_published=True) |
            Q(products__comparisons_as_first__is_published=True) |
            Q(products__comparisons_as_second__is_published=True) |
            Q(guides__is_published=True)
        ).distinct().order_by('name')

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
        return Guide.objects.filter(is_published=True).order_by('-created_at')

    def lastmod(self, obj):
        return obj.updated_at
