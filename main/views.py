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
        result = catch_pokemon("kanto")
        if result[:5] == "shiny" :
            p = Pokemon.objects.get(name=result[6:])
        elif result: 
            p = Pokemon.objects.get(name=result)
        return render(request, "main/regions/kanto.html", {"r": r, "result": result, "p": p})
    
    return render(request, "main/regions/kanto.html", {"r": r})

def johto(request, region):
    r = Region.objects.get(name=region)
    
    if request.method == 'POST':
        result = catch_pokemon("johto")
        if result[:5] == "shiny" :
            p = Pokemon.objects.get(name=result[6:])
        elif result: 
            p = Pokemon.objects.get(name=result)
        return render(request, "main/regions/johto.html", {"r": r, "result": result, "p": p})
    
    return render(request, "main/regions/johto.html", {"r": r})

def hoenn(request, region):
    r = Region.objects.get(name=region)
    
    if request.method == 'POST':
        result = catch_pokemon("hoenn")
        if result[:5] == "shiny" :
            p = Pokemon.objects.get(name=result[6:])
        elif result: 
            p = Pokemon.objects.get(name=result)
        return render(request, "main/regions/hoenn.html", {"r": r, "result": result, "p": p})
    
    return render(request, "main/regions/hoenn.html", {"r": r})

def sinnoh(request, region):
    r = Region.objects.get(name=region)
    
    if request.method == 'POST':
        result = catch_pokemon("sinnoh")
        if result[:5] == "shiny" :
            p = Pokemon.objects.get(name=result[6:])
        elif result: 
            p = Pokemon.objects.get(name=result)
        return render(request, "main/regions/sinnoh.html", {"r": r, "result": result, "p": p})
    
    return render(request, "main/regions/sinnoh.html", {"r": r})

def unova(request, region):
    r = Region.objects.get(name=region)
    
    if request.method == 'POST':
        result = catch_pokemon("unova")
        if result[:5] == "shiny" :
            p = Pokemon.objects.get(name=result[6:])
        elif result: 
            p = Pokemon.objects.get(name=result)
        return render(request, "main/regions/unova.html", {"r": r, "result": result, "p": p})
    
    return render(request, "main/regions/unova.html", {"r": r})

def kalos(request, region):
    r = Region.objects.get(name=region)
    
    if request.method == 'POST':
        result = catch_pokemon("kalos")
        if result[:5] == "shiny" :
            p = Pokemon.objects.get(name=result[6:])
        elif result: 
            p = Pokemon.objects.get(name=result)
        return render(request, "main/regions/kalos.html", {"r": r, "result": result, "p": p})
    
    return render(request, "main/regions/kalos.html", {"r": r})

def alola(request, region):
    r = Region.objects.get(name=region)
    
    if request.method == 'POST':
        result = catch_pokemon("alola")
        if result[:5] == "shiny" :
            p = Pokemon.objects.get(name=result[6:])
        elif result: 
            p = Pokemon.objects.get(name=result)
        return render(request, "main/regions/alola.html", {"r": r, "result": result, "p": p})
    
    return render(request, "main/regions/alola.html", {"r": r})

def galar(request, region):
    r = Region.objects.get(name=region)
    
    if request.method == 'POST':
        result = catch_pokemon("galar")
        if result[:5] == "shiny" :
            p = Pokemon.objects.get(name=result[6:])
        elif result: 
            p = Pokemon.objects.get(name=result)
        return render(request, "main/regions/galar.html", {"r": r, "result": result, "p": p})

    return render(request, "main/regions/galar.html", {"r": r})

def paldea(request, region):
    r = Region.objects.get(name=region)
    
    if request.method == 'POST':
        result = catch_pokemon("paldea")
        if result[:5] == "shiny" :
            p = Pokemon.objects.get(name=result[6:])
        elif result: 
            p = Pokemon.objects.get(name=result)
        return render(request, "main/regions/paldea.html", {"r": r, "result": result, "p": p})
    
    return render(request, "main/regions/paldea.html", {"r": r})