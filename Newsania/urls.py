from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.News, name='news'),
    path('Title/', views.Title, name='Title'),
    path('Image/', views.Image, name='Image'),

]