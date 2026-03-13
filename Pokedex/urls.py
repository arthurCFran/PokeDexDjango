from  django.urls import path
from . import views

app_name = 'pokedex'

urlpatterns = [
    path('', views.Pokedex_index, name='index'),
    path('adicionar/', views.Pokedex_adcionar, name='adicionar'),
    path('remover/<int:pokemon_id>/', views.Pokedex_remover, name='remover'),
    path('editar/<int:pokemon_id>/', views.Pokedex_editar, name='editar')
] 