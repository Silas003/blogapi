from django.db import models
from django.conf import settings
from django.db.models.query import QuerySet  
from django.utils import timezone
from django.utils.text import slugify
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='published')
    
    objects = models.Manager()
    postObjects = PostObjects()

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate a slug from the title and the published date
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering=['published']

    def __str__(self):
        return self.title