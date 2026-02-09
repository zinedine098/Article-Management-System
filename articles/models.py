from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Article(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'

    title = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True
    )

    content = models.TextField()

    thumbnail = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT
    )

    author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='articles',
    limit_choices_to={'role': 'author'}
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles'
    )

    view_count = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'articles'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    def __str__(self):
        return self.title
    

class ArticleTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE,
        related_name='article_tags'
    )
    tag = models.ForeignKey(
        'Tag',
        on_delete=models.CASCADE,
        related_name='tag_articles'
    )

    class Meta:
        db_table = 'article_tags'
        constraints = [
            models.UniqueConstraint(fields=['article', 'tag'], name='unique_article_tag')
        ]

    def __str__(self):
        return f"{self.article_id} - {self.tag_id}"

