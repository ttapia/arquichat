from django.urls import path

from . import views

app_name='chat'
urlpatterns = [
    path('', views.landing, name='landing'),
    path('login', views.login, name='login'),
    path('messages', views.index, name='index'),
    path('send', views.send, name='send'),
    path('sendRandomFact', views.sendRandomFact, name='sendRandomFact'),
    path('logout', views.logout, name='logout'),
]
