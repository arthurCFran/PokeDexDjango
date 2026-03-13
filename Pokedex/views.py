from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest

from .models import Pokemon
from .forms import PokemonForm

# Create your views here.
def Pokedex_index(request):
    context = {
        'pokemons': Pokemon.objects.all()
    }
    return render(request, 'pokedex/index.html', context)

def Pokedex_adcionar(request:HttpRequest):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    context = {
        'form': PokemonForm()
    }
    return render(request, 'pokedex/adicionar.html', context)

def Pokedex_remover(request:HttpRequest, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    pokemon.delete()
    return redirect('pokedex:index') 

def Pokedex_editar(request:HttpRequest, pokemon_id):
    pokemon = get_object_or_404(id=pokemon_id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')

    form = PokemonForm(instance=pokemon)
    context = {
        'form': form
    }
    return render(request, 'pokedex/editar.html', context)