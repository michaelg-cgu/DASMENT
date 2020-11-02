from django.urls import path
from . import views  # . is current directory
from django.conf.urls import include, url

# empty '' (path) for home page....need to be name specific
urlpatterns = [
    path('', views.surveys, name='surveys'),
    path('snippet/', views.snippet_detail, name='snippet'),
    path('enviromental/', views.enviromental_detail, name='enviromental')
]
