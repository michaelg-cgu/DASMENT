from django.urls import path
from . import views  # . is current directory
from django.conf.urls import include, url

# empty '' (path) for home page....need to be name specific
urlpatterns = [
    path('', views.surveys, name='surveys'),
    path('environmental/', views.environmental_detail, name='environmental'),
    #path('allergy/', views.allergy_detail, name='allergy'),
    #ath('reaction/', views.reaction_detail, name='reaction')
]
