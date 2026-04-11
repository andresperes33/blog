from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.urls import reverse
from .models import Review, Category, Product, Comparison, Guide, GuideItem
from itertools import chain
from operator import attrgetter

class ReviewListView(ListView):
    template_name = 'reviews/index.html'
    context_object_name = 'combined_content'
    
    def get_queryset(self):
        reviews = list(Review.objects.filter(is_published=True))
        comparisons = list(Comparison.objects.filter(is_published=True))
        guides = list(Guide.objects.filter(is_published=True))
        
        # Atribuir metadados para facilitar no template
        for r in reviews:
            r.type_name = "review"
            r.display_category = r.product.category.name
            r.url = reverse('reviews:review_detail', kwargs={'slug': r.slug})
            
        for c in comparisons:
            c.type_name = "comparison"
            c.display_category = c.product_1.category.name
            c.url = reverse('reviews:comparison_detail', kwargs={'slug': c.slug})
            
        for g in guides:
            g.type_name = "guide"
            g.display_category = g.category.name
            g.url = reverse('reviews:guide_detail', kwargs={'slug': g.slug})

        combined = sorted(
            chain(reviews, comparisons, guides),
            key=attrgetter('created_at'),
            reverse=True
        )[:9]
        return combined

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_reviews'] = Review.objects.filter(is_featured=True, is_published=True).order_by('-created_at')[:3]
        context['categories'] = Category.objects.all()
        return context

class AllReviewsView(ListView):
    model = Review
    template_name = 'reviews/all_reviews.html'
    context_object_name = 'reviews'
    paginate_by = 12
    queryset = Review.objects.filter(is_published=True).order_by('-created_at')

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_reviews'] = Review.objects.filter(
            product__category=self.object.product.category
        ).exclude(id=self.object.id)[:3]
        # Versões curtas para evitar quebra de linha no template
        context['category'] = self.object.product.category.name
        context['rating'] = self.object.rating
        return context

class CategoryListView(ListView):
    model = Category
    template_name = 'reviews/all_categories.html'
    context_object_name = 'categories'

class CategoryDetailView(ListView):
    model = Review
    template_name = 'reviews/category_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Review.objects.filter(product__category=self.category, is_published=True).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from django.db.models import Q
        context['category'] = self.category
        context['comparisons'] = Comparison.objects.filter(
            Q(product_1__category=self.category) | Q(product_2__category=self.category),
            is_published=True
        ).distinct().order_by('-created_at')
        context['guides'] = Guide.objects.filter(category=self.category, is_published=True).order_by('-created_at')
        return context

class ComparisonListView(ListView):
    model = Comparison
    template_name = 'reviews/comparison_list.html'
    context_object_name = 'comparisons'
    paginate_by = 9

    def get_queryset(self):
        return Comparison.objects.filter(is_published=True).order_by('-created_at')

class ComparisonDetailView(DetailView):
    model = Comparison
    template_name = 'reviews/comparison_detail.html'
    context_object_name = 'comparison'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['p1'] = self.object.product_1
        context['p2'] = self.object.product_2
        context['review_1'] = Review.objects.filter(product=self.object.product_1).first()
        context['review_2'] = Review.objects.filter(product=self.object.product_2).first()
        context['related_comparisons'] = Comparison.objects.filter(
            is_published=True
        ).exclude(id=self.object.id)[:3]
        return context

from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'reviews/about.html'

class PrivacyView(TemplateView):
    template_name = 'reviews/privacy.html'

class TermsView(TemplateView):
    template_name = 'reviews/terms.html'

class ContactView(TemplateView):
    template_name = 'reviews/contact.html'

class GuideListView(ListView):
    model = Guide
    template_name = 'reviews/guide_list.html'
    context_object_name = 'guides'
    paginate_by = 9

    def get_queryset(self):
        return Guide.objects.filter(is_published=True).order_by('-created_at')

class GuideDetailView(DetailView):
    model = Guide
    template_name = 'reviews/guide_detail.html'
    context_object_name = 'guide'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.object.items.all().order_by('position')
        context['latest_guides'] = Guide.objects.filter(is_published=True).exclude(id=self.object.id)[:3]
        return context
