from django.db import models
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

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

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
    title = models.CharField("Título do Comparativo", max_length=255)
    slug = models.SlugField("Slug", max_length=255, unique=True, blank=True)
    product_1 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comparisons_as_first")
    product_2 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comparisons_as_second")
    main_image = models.ImageField("Imagem do Duelo", upload_to="comparisons/main/")
    content = models.TextField("Conteúdo do Comparativo (Markdown/HTML)")
    verdict = models.TextField("O Veredito do André", help_text="Explique quem ganha e por que.")
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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

    class Meta:
        verbose_name = "Comparativo"
        verbose_name_plural = "Comparativos"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
