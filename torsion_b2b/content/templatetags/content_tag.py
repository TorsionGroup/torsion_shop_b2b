from django import template
from content.models import *
register = template.Library()


@register.simple_tag()
def get_catalogcategories():
    return CatalogCategory.objects.all()


@register.inclusion_tag('torsion_shop/tags/last_news.html')
def get_last_news(count=5):
    news = Content.objects.filter(category_id=2).order_by("id")[:count]
    return {'last_news': news}
