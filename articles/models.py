from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save, pre_save
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from .utils import slugify_instance_title


class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()  # []
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Articles(models.Model):
    user = models.ForeignKey("auth.user", null=True, blank=True, on_delete=models.SET_NULL)
    author_name = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    published = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now, null=True, blank=True)

    object=ArticleManager()
    @property
    def name(self):
        return self.title

    def get_absolute_url(self):
        # return f'/articles/{self.slug}/'
        return reverse("articles:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        super(Articles, self).save(*args, **kwargs)


def article_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    print(args, kwargs)
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(article_pre_save, sender=Articles)


def article_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    print(args, kwargs)
    if created:
       slugify_instance_title(instance, save=True)


post_save.connect(article_post_save, sender=Articles)

