from django.contrib import admin
from .models import Category, Tag, Product, Review, ReviewImage, Comment, Comparison

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
    
    fieldsets = (
        (None, {
            'fields': ('product', 'title', 'slug', 'author', 'excerpt', 'content', 'conclusion', 'main_image', 'rating', 'is_featured', 'is_published')
        }),
        ('Afiliados (Deixe em branco se não houver link)', {
            'fields': ('amazon_link', 'mercadolivre_link', 'shopee_link', 'aliexpress_link', 'kabum_link')
        }),
        ('Tags', {
            'fields': ('tags_input', 'tags')
        }),
        ('Conteúdo Extra', {
            'fields': ('pros', 'cons', 'specifications')
        }),
    )
    readonly_fields = ('tags',)

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

@admin.register(Comparison)
class ComparisonAdmin(admin.ModelAdmin):
    list_display = ('title', 'product_1', 'product_2', 'rating', 'created_at', 'is_featured', 'is_published')
    list_filter = ('is_featured', 'is_published', 'created_at')
    search_fields = ('title', 'content', 'product_1__name', 'product_2__name')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('tags',)
    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'excerpt', 'main_image', 'rating', 'is_featured', 'is_published')
        }),
        ('Duelo', {
            'fields': ('product_1', 'product_2', 'content', 'verdict')
        }),
        ('Afiliados (Gerais do Duelo)', {
            'fields': ('amazon_link', 'mercadolivre_link', 'shopee_link', 'aliexpress_link', 'kabum_link')
        }),
        ('Tags', {
            'fields': ('tags_input', 'tags')
        }),
        ('Conteúdo Extra/Duelo', {
            'fields': ('pros', 'cons', 'specifications')
        }),
    )
