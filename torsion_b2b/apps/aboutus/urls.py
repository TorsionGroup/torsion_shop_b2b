from django.urls import path
from . import views

urlpatterns = [
    path('aboutus/', views.AboutusView.as_view(), name='aboutus'),
]