from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('<str:room>/', views.RooM, name='room'),
    path('checkview', views.Checkview, name='checkview'),
    path('send', views.Send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]