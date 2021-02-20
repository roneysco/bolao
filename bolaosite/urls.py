from django.urls import path
from . import views

urlpatterns = [
    path('', views.jogos_list, name='jogos_list'),
]