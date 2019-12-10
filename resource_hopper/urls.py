from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.teams, name='resource_hopper-teams'),
    path('resource/', views.resource, name='resource_hopper-resource'),
    path('buildteam/', views.buildteam, name='resource_hopper-buildteam'),
    path('', views.teams, name='resource_hopper-home')
]
