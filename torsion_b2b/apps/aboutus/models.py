from django.db import models
from datetime import datetime


class Aboutus(models.Model):
    alias = models.SlugField(max_length=300, unique=True)
    created_date = models.DateTimeField(default=datetime.today)
    updated_date = models.DateTimeField(default=datetime.today)
    published = models.BooleanField(default=0)
    main_image = models.ImageField(upload_to="content/main_image/", blank=True, null=True)
    title = models.CharField(max_length=500, null=True)
    intro_text = models.CharField(max_length=1000, null=True)
    full_text = models.TextField(null=True)
    meta_tag_title = models.CharField(max_length=500, null=True, blank=True)
    meta_tag_description = models.CharField(max_length=500, null=True, blank=True)
    meta_tag_keyword = models.CharField(max_length=500, null=True, blank=True)
    geo = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name = "Aboutus"
        verbose_name_plural = "Aboutus"