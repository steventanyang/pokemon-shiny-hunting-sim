from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import random

from .models import Region, Pokemon

def regions(response):
	return render(response, "main/regions.html", {})

def home(response):
	return render(response, "main/home.html", {})

def test(response, pokemon):
	p = Pokemon.objects.get(name=pokemon)
	return render(response, "main/test.html", {"p":p})

def pokedex(response, region):
	r = Region.objects.get(name=region)
	return render(response, "main/pokedex.html", {"r":r})

def choosedex(response):
	return render(response, "main/choosedex.html", {})



def catch_pokemon(region):
    r = Region.objects.get(name=region)
    pokemon_list = []
    for pokemon in r.pokemon_set.all():
        pokemon_list.append(pokemon)
    
    catch = random.choice(pokemon_list)
    shiny = random.randint(1, 2)
    
    if shiny == 1:
        return "shiny " + catch.name
    else:
        return catch.name



def kanto(request, region):
    r = Region.objects.get(name=region)
    
    if request.method == 'POST':
        result = catch_pokemon("kanto")  # Call the encounter logic
        return render(request, "main/regions/kanto.html", {"r": r, "result": result})
    
    return render(request, "main/regions/kanto.html", {"r": r})

def johto(response, region):
    r = Region.objects.get(name=region)
    
    if response.method == 'POST':
        result = catch_pokemon(region)
        return render(response, "main/regions/johto.html", {"r": r, "result": result})
    
    return render(response, "main/regions/johto.html", {"r": r})

def hoenn(response, region):
    r = Region.objects.get(name=region)
    
    if response.method == 'POST':
        result = catch_pokemon(region)
        return render(response, "main/regions/hoenn.html", {"r": r, "result": result})
    
    return render(response, "main/regions/hoenn.html", {"r": r})

def sinnoh(response, region):
    r = Region.objects.get(name=region)
    
    if response.method == 'POST':
        result = catch_pokemon(region)
        return render(response, "main/regions/sinnoh.html", {"r": r, "result": result})
    
    return render(response, "main/regions/sinnoh.html", {"r": r})

def unova(response, region):
    r = Region.objects.get(name=region)
    
    if response.method == 'POST':
        result = catch_pokemon(region)
        return render(response, "main/regions/unova.html", {"r": r, "result": result})
    
    return render(response, "main/regions/unova.html", {"r": r})

def kalos(response, region):
    r = Region.objects.get(name=region)
    
    if response.method == 'POST':
        result = catch_pokemon(region)
        return render(response, "main/regions/kalos.html", {"r": r, "result": result})
    
    return render(response, "main/regions/kalos.html", {"r": r})

def alola(response, region):
    r = Region.objects.get(name=region)
    
    if response.method == 'POST':
        result = catch_pokemon(region)
        return render(response, "main/regions/alola.html", {"r": r, "result": result})
    
    return render(response, "main/regions/alola.html", {"r": r})

def galar(response, region):
    r = Region.objects.get(name=region)
    
    if response.method == 'POST':
        result = catch_pokemon(region)
        return render(response, "main/regions/galar.html", {"r": r, "result": result})
    
    return render(response, "main/regions/galar.html", {"r": r})

def paldea(response, region):
    r = Region.objects.get(name=region)
    
    if response.method == 'POST':
        result = catch_pokemon(region)
        return render(response, "main/regions/paldea.html", {"r": r, "result": result})
    
    return render(response, "main/regions/paldea.html", {"r": r})
