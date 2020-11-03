from django.urls import path
from . import views  # . is current directory

# empty '' (path) for home page....need to be name specific
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('mydashboard/', views.mydashboard, name='blog-about'),
]
