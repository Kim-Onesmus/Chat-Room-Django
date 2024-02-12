from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('logout', views.Logout, name='logout'),
    path('<str:room>/', views.RooM, name='room'),
    path('checkview', views.Checkview, name='checkview'),
    path('send', views.Send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('room1', views.Room1, name='room1')
]