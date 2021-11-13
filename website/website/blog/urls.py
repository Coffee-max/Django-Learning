from django.urls import path
from .  import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.abt, name='blog-abt'),
]
