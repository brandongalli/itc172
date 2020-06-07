from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getResources/', views.getResources, name='resources'),
    path('getMeetings/', views.getMeetings, name='meetings'),
    path('meetingsDetail/<int:id>', views.meetingsDetail, name='meetingsdetail'),
    path('newProduct/', views.newProduct, name='newclub'),
    path('newResource/', views.newResource, name='newresource')

]