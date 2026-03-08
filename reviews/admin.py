from django.contrib import admin
from .models import Category, Tag, Product, Review, ReviewImage, Comment

class ReviewImageInline(admin.TabularInline):
    model = ReviewImage
    extra = 1

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'rating', 'created_at', 'is_featured', 'is_published')
    list_filter = ('is_featured', 'is_published', 'created_at', 'product__category')
    search_fields = ('title', 'content', 'product__name')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ReviewImageInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category')
    list_filter = ('category', 'brand')
    search_fields = ('name', 'brand')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'review', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('text', 'user__username', 'review__title')
