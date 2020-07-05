from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/<slug:slug>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('about-us/', views.AboutUsView.as_view(), name='about-us'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
]