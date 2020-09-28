from django.views.generic import ListView, DetailView
from django.urls import reverse
from .models import *


class HomeView(ListView):
    template_name = 'oscar_promotions/home.html'

