from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Review, Category, Product

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/index.html'
    context_object_name = 'reviews'
    paginate_by = 9
    queryset = Review.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_reviews'] = Review.objects.filter(is_featured=True, is_published=True)[:3]
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
        return Review.objects.filter(product__category=self.category, is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'reviews/about.html'

class PrivacyView(TemplateView):
    template_name = 'reviews/privacy.html'

class TermsView(TemplateView):
    template_name = 'reviews/terms.html'
