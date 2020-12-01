from django.shortcuts import render
from .models import Post
import folium
from folium import plugins
import pandas as pd
import numpy as np

#below is not needed
#from django.http import HttpResponse

# no longer dummy datas
df_incidents = pd.read_csv(
    '/Users/michaelgarcia/Documents/PythonProjects/IST303/projects/DASMENT/FoodforThought/blog/restaurants.csv')


def home(request):
    # Create Map
    m = folium.Map(location=[34.09812147677658, -117.71827532972465], zoom_start=15)

    #folium.Marker(location=[34.05, -118.24]).add_to(m)
    # testing

    # the featuregroup is for generic bubbles
    incidents = folium.map.FeatureGroup()
    # the cluster feature is for clusters
    #incidents = plugins.MarkerCluster(add_to(m))
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


def mydashboard(request):
    return render(request, 'blog/mydashboard.html', {'title': 'My-Dashboard'})

# def map(request):
#     m = folium.Map()
#     return render(request, m)
