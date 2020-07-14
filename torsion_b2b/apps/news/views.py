from django.views.generic import ListView, DetailView
from .models import *

class NewsView(ListView):
    model = News
    queryset = News.objects.all()
    context_object_name = 'news_list'
    paginate_by = 10
    template_name = 'torsion_shop/news/news_list.html'


class NewsDetailView(DetailView):
    model = News
    slug_field = 'alias'
    context_object_name = 'news_detail'
    template_name = 'torsion_shop/news/news_detail.html'