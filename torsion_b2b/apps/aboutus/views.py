from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class AboutusView(ListView):
    model = Aboutus
    queryset = Aboutus.objects.all()
    context_object_name = 'aboutus_list'
    template_name = 'oscar/aboutus/aboutus.html'