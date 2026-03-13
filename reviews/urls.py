from django.urls import path
from .views import ReviewListView, ReviewDetailView, CategoryListView, CategoryDetailView, AboutView, AllReviewsView, PrivacyView, TermsView, ContactView

app_name = 'reviews'

urlpatterns = [
    path('', ReviewListView.as_view(), name='index'),
    path('reviews/', AllReviewsView.as_view(), name='all_reviews'),
    path('review/<slug:slug>/', ReviewDetailView.as_view(), name='review_detail'),
    path('categorias/', CategoryListView.as_view(), name='all_categories'),
    path('categoria/<slug:slug>/', CategoryDetailView.as_view(), name='category_list'),
    path('sobre/', AboutView.as_view(), name='about'),
    path('privacidade/', PrivacyView.as_view(), name='privacy'),
    path('termos-de-uso/', TermsView.as_view(), name='terms'),
    path('contato/', ContactView.as_view(), name='contact'),
]
