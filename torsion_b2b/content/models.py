from django.db import models
from datetime import datetime
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=300)
    comment = models.CharField(max_length=500, null=True, blank=True)
    url = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Content(models.Model):
    alias = models.SlugField(max_length=300, unique=True)
    created_date = models.DateTimeField(default=datetime.today)
    updated_date = models.DateTimeField(default=datetime.today)
    published = models.BooleanField(default=0)
    main_image = models.ImageField(upload_to="content/main_image/", blank=True, null=True)
    category_id = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name="content_category", null=True, blank=True)
    title = models.CharField(max_length=500, null=True)
    intro_text = models.CharField(max_length=1000, null=True)
    full_text = models.TextField(null=True)
    meta_tag_title = models.CharField(max_length=500, null=True, blank=True)
    meta_tag_description = models.CharField(max_length=500, null=True, blank=True)
    meta_tag_keyword = models.CharField(max_length=500, null=True, blank=True)
    geo = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.alias

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={"slug": self.alias})

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Contents"


class ContentImage(models.Model):
    name = models.CharField(max_length=250, default='ContentImage')
    description = models.TextField(null=True, blank=True)
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="content/content_image/", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ContentImage"
        verbose_name_plural = "ContentImages"
