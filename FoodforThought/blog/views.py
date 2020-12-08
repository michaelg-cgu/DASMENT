from django.shortcuts import render
from .models import Post
import folium
from django.contrib.auth.models import User
from folium import plugins
import pandas as pd
import numpy as np
import matplotlib as mpl
import sqlite3
from surveys.models import FoodAllergy, Environmental
from myusers.models import UserRegDemographics
from django.contrib.auth.decorators import login_required

df_incidents = pd.read_csv(
    '/Users/michaelgarcia/Documents/PythonProjects/IST303/projects/DASMENT/FoodforThought/blog/restaurants.csv')


def home(request):
    # Create Map
    m = folium.Map(location=[34.09812147677658, -117.71827532972465], zoom_start=15)

    # the featuregroup is for generic bubbles
    incidents = folium.map.FeatureGroup()
    # the cluster feature is for clusters
    # incidents = plugins.MarkerCluster(add_to(m))
    # loop through the 100 crimes and add each to the incidents feature group
    for lat, lng, in zip(df_incidents.Y, df_incidents.X):
        incidents.add_child(
            folium.CircleMarker(
                [lat, lng],
                radius=5,  # define how big you want the circle markers to be
                color='yellow',
                fill=True,
                fill_color='blue',
                fill_opacity=0.6
            )
        )
    # add popup text to each marker on the map:
    latitudes = list(df_incidents.Y)
    longitudes = list(df_incidents.X)
    posscore = list(df_incidents.Good)  # category is the csv column name
    negscore = list(df_incidents.Bad)
    resname = list(df_incidents.RestaurantName)
    rescore = list(df_incidents.Score)

    for lat, lng, pscore, nscore, rname, rscore in zip(latitudes, longitudes, posscore, negscore, resname, rescore):
        folium.Marker([lat, lng], popup=(rname + '<br><br>' +
                                         ' ' + 'good reviews: ' + str(pscore) +
                                         '<br><br>' + 'bad reviews: ' + str(nscore) + '<br><br>' + 'Overall Score: ' + str(rscore))).add_to(m)

    m.add_child(incidents)
    # end testing
    # Get html representation ofs map
    m = m._repr_html_()

    context = {
        'posts': Post.objects.all(),  # this queries the data base using the local commas
        'm': m
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


@login_required()
def mydashboard(request):
    pk = request.user.pk
    print(pk)
    user = User.objects.get(pk=pk)
    c = UserRegDemographics.objects.all()
    d = FoodAllergy.objects.all()
    e = Environmental.objects.all()
    context = dict(testing=c)
    context2 = dict(testing2=d)
    context2_1 = dict(testing3=e)
    context3 = {**context, **context2, **context2_1}
    print('context1', context)
    print('hello', context2)
    print('hello', context2_1)
    print('helep', context3)
    return render(request, 'blog/mydashboard.html', context3)
