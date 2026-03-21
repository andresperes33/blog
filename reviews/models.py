from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Slug", max_length=100, unique=True, blank=True)
    icon = models.CharField("Ícone (Emoji ou Classe de Ícone)", max_length=50, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def total_content_count(self):
        # Importação dentro do método para evitar erro de definição (pois Review/Comparison vêm depois)
        from .models import Review, Comparison
        from django.db.models import Q
        
        # Reviews vinculados a produtos desta categoria
        reviews_count = Review.objects.filter(product__category=self, is_published=True).count()
        
        # Comparativos envolvendo produtos desta categoria
        comparisons_count = Comparison.objects.filter(
            Q(product_1__category=self) | Q(product_2__category=self),
            is_published=True
        ).distinct().count()
        
        # Guias vinculados diretamente
        guides_count = self.guides.filter(is_published=True).count()
        
        return reviews_count + comparisons_count + guides_count

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reviews:category_list', kwargs={'slug': self.slug})

class Tag(models.Model):
    name = models.CharField("Nome", max_length=50, unique=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField("Nome do Produto", max_length=200)
    brand = models.CharField("Marca", max_length=100)
    model_name = models.CharField("Modelo", max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f"{self.brand} {self.name}"

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    title = models.CharField("Título do Review", max_length=255)
    slug = models.SlugField("Slug", max_length=255, unique=True, blank=True)
    excerpt = models.TextField("Resumo", help_text="Aparece nas listagens.")
    content = models.TextField("Conteúdo do Review (Markdown/HTML)")
    conclusion = models.TextField("Conclusão", blank=True, help_text="Formatação igual ao conteúdo.")
    main_image = models.ImageField("Imagem Principal", upload_to="reviews/main/")
    rating = models.DecimalField("Nota (0-10)", max_digits=3, decimal_places=1)
    pros = models.TextField("Pontos Positivos", help_text="Um por linha")
    cons = models.TextField("Pontos Negativos", help_text="Um por linha")
    specifications = models.JSONField("Especificações Técnicas", default=dict, blank=True)
    tags_input = models.CharField("Tags (separadas por vírgula)", max_length=255, blank=True, help_text="Ex: gamer, barato, potente")
    
    # Links de Afiliados
    amazon_link = models.URLField("Link Amazon", max_length=500, blank=True, null=True)
    mercadolivre_link = models.URLField("Link Mercado Livre", max_length=500, blank=True, null=True)
    shopee_link = models.URLField("Link Shopee", max_length=500, blank=True, null=True)
    aliexpress_link = models.URLField("Link AliExpress", max_length=500, blank=True, null=True)
    kabum_link = models.URLField("Link Kabum", max_length=500, blank=True, null=True)
    
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField("Destaque", default=False)
    is_published = models.BooleanField("Publicado", default=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('reviews:review_detail', kwargs={'slug': self.slug})

    @property
    def parsed_specs(self):
        if isinstance(self.specifications, dict):
            return [{"label": k, "value": v} for k, v in self.specifications.items()]
        return []

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        # Converte imagem principal para WebP se necessário
        if self.main_image:
            from PIL import Image
            from io import BytesIO
            from django.core.files.base import ContentFile
            import os

            img = Image.open(self.main_image)
            if img.format != 'WEBP':
                # Preserva a proporção
                output = BytesIO()
                img.save(output, format='WEBP', quality=80)
                output.seek(0)
                
                # Altera o nome do arquivo para .webp
                name = os.path.splitext(self.main_image.name)[0] + '.webp'
                self.main_image.save(name, ContentFile(output.read()), save=False)

        super().save(*args, **kwargs)
        
        # Process tags_input if present
        if self.tags_input:
            tag_names = [t.strip() for t in self.tags_input.split(',') if t.strip()]
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name)
                self.tags.add(tag)

class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="reviews/gallery/")
    alt_text = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if self.image:
            from PIL import Image
            from io import BytesIO
            from django.core.files.base import ContentFile
            import os

            img = Image.open(self.image)
            if img.format != 'WEBP':
                output = BytesIO()
                img.save(output, format='WEBP', quality=80)
                output.seek(0)
                
                name = os.path.splitext(self.image.name)[0] + '.webp'
                self.image.save(name, ContentFile(output.read()), save=False)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Imagem da Galeria"
        verbose_name_plural = "Imagens da Galeria"

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Comentário")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"

class Comparison(models.Model):
    product_1 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comparisons_as_first")
    product_2 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comparisons_as_second")
    title = models.CharField("Título do Comparativo", max_length=255)
    slug = models.SlugField("Slug", max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    excerpt = models.TextField("Resumo", help_text="Aparece nas listagens.")
    content = models.TextField("Conteúdo do Comparativo (Markdown/HTML)")
    conclusion = models.TextField("Conclusão", blank=True, help_text="Formatação igual ao conteúdo.")
    main_image = models.ImageField("Imagem Principal", upload_to="comparisons/main/")
    
    # Links de Afiliados - Produto 1
    amazon_link_1 = models.URLField("Link Amazon (Produto 1)", max_length=500, blank=True, null=True)
    mercadolivre_link_1 = models.URLField("Link Mercado Livre (Produto 1)", max_length=500, blank=True, null=True)
    shopee_link_1 = models.URLField("Link Shopee (Produto 1)", max_length=500, blank=True, null=True)
    aliexpress_link_1 = models.URLField("Link AliExpress (Produto 1)", max_length=500, blank=True, null=True)
    kabum_link_1 = models.URLField("Link Kabum (Produto 1)", max_length=500, blank=True, null=True)

    # Links de Afiliados - Produto 2
    amazon_link_2 = models.URLField("Link Amazon (Produto 2)", max_length=500, blank=True, null=True)
    mercadolivre_link_2 = models.URLField("Link Mercado Livre (Produto 2)", max_length=500, blank=True, null=True)
    shopee_link_2 = models.URLField("Link Shopee (Produto 2)", max_length=500, blank=True, null=True)
    aliexpress_link_2 = models.URLField("Link AliExpress (Produto 2)", max_length=500, blank=True, null=True)
    kabum_link_2 = models.URLField("Link Kabum (Produto 2)", max_length=500, blank=True, null=True)

    # Tags
    tags_input = models.CharField("Tags (separadas por vírgula)", max_length=255, blank=True, help_text="Ex: gamer, barato, potente")
    tags = models.ManyToManyField(Tag, blank=True)
    
    # Conteúdo Extra Produto 1
    pros_1 = models.TextField("Pontos Positivos (Produto 1)", help_text="Um por linha", blank=True)
    cons_1 = models.TextField("Pontos Negativos (Produto 1)", help_text="Um por linha", blank=True)
    rating_1 = models.DecimalField("Nota Produto 1 (0-10)", max_digits=3, decimal_places=1, default=0.0)

    # Conteúdo Extra Produto 2
    pros_2 = models.TextField("Pontos Positivos (Produto 2)", help_text="Um por linha", blank=True)
    cons_2 = models.TextField("Pontos Negativos (Produto 2)", help_text="Um por linha", blank=True)
    rating_2 = models.DecimalField("Nota Produto 2 (0-10)", max_digits=3, decimal_places=1, default=0.0)
    
    # Especificações Técnicas Individuais (Opcional, se quiser sobrescrever o produto)
    specifications_1 = models.JSONField("Especificações Técnicas Produto 1", default=dict, blank=True)
    specifications_2 = models.JSONField("Especificações Técnicas Produto 2", default=dict, blank=True)
    
    # Nota Geral do Duelo (Opcional, se quiser manter uma média ou nota de quem ganha)
    rating = models.DecimalField("Nota Geral do Duelo (0-10)", max_digits=3, decimal_places=1, default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField("Publicado", default=True)
    is_featured = models.BooleanField("Destaque na Home", default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        if self.main_image:
            from PIL import Image
            from io import BytesIO
            from django.core.files.base import ContentFile
            import os

            img = Image.open(self.main_image)
            if img.format != 'WEBP':
                output = BytesIO()
                img.save(output, format='WEBP', quality=80)
                output.seek(0)
                name = os.path.splitext(self.main_image.name)[0] + '.webp'
                self.main_image.save(name, ContentFile(output.read()), save=False)

        super().save(*args, **kwargs)
        
        # Process tags_input if present
        if self.tags_input:
            tag_names = [t.strip() for t in self.tags_input.split(',') if t.strip()]
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name)
                self.tags.add(tag)

    class Meta:
        verbose_name = "Comparativo"
        verbose_name_plural = "Comparativos"
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('reviews:comparison_detail', kwargs={'slug': self.slug})

    @property
    def parsed_specs_1(self):
        if isinstance(self.specifications_1, dict):
            return [{"label": k, "value": v} for k, v in self.specifications_1.items()]
        return []

    @property
    def parsed_specs_2(self):
        if isinstance(self.specifications_2, dict):
            return [{"label": k, "value": v} for k, v in self.specifications_2.items()]
        return []

class Guide(models.Model):
    title = models.CharField("Título do Guia", max_length=255)
    slug = models.SlugField("Slug", max_length=255, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="guides")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    excerpt = models.TextField("Resumo", help_text="Aparece nas listagens.")
    content = models.TextField("Conteúdo/Introdução do Guia")
    conclusion = models.TextField("Conclusão/Veredito Final", blank=True)
    main_image = models.ImageField("Imagem Principal", upload_to="guides/main/")
    is_published = models.BooleanField("Publicado", default=True)
    is_featured = models.BooleanField("Destaque na Home", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Guia de Compra"
        verbose_name_plural = "Guias de Compra"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('reviews:guide_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class GuideItem(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, help_text="Opcional: Vincule a um produto existente")
    position = models.PositiveIntegerField("Posição no Rank (1, 2, 3...)")
    name = models.CharField("Nome de Exibição do Produto", max_length=255)
    description = models.TextField("Descrição/Análise Curta")
    image = models.ImageField("Imagem do Produto", upload_to="guides/items/", blank=True, null=True)
    
    # Links de Afiliados Manual (Caso não queira usar campos do Produto)
    amazon_link = models.URLField("Link Amazon", max_length=500, blank=True, null=True)
    mercadolivre_link = models.URLField("Link Mercado Livre", max_length=500, blank=True, null=True)
    shopee_link = models.URLField("Link Shopee", max_length=500, blank=True, null=True)
    aliexpress_link = models.URLField("Link AliExpress", max_length=500, blank=True, null=True)
    kabum_link = models.URLField("Link Kabum", max_length=500, blank=True, null=True)
    
    # Prós e Contras
    pros = models.TextField("Pontos Positivos", help_text="Um por linha", blank=True)
    cons = models.TextField("Pontos Negativos", help_text="Um por linha", blank=True)
    
    @property
    def pros_list(self):
        if self.pros:
            return [line.strip() for line in self.pros.splitlines() if line.strip()]
        return []

    @property
    def cons_list(self):
        if self.cons:
            return [line.strip() for line in self.cons.splitlines() if line.strip()]
        return []

    class Meta:
        verbose_name = "Item do Guia"
        verbose_name_plural = "Itens do Guia"
        ordering = ['position']

    def __str__(self):
        return f"{self.position}º - {self.name}"
