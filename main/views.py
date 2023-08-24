from django.shortcuts import render
from django.http import HttpResponse

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


def kanto(response, region):
	r = Region.objects.get(name=region)
	return render(response, "main/regions/kanto.html", {"r":r})

def johto(response):
	return render(response, "main/regions/johto.html", {})

def hoenn(response):
	return render(response, "main/regions/hoenn.html", {})

def sinnoh(response):
	return render(response, "main/regions/sinnoh.html", {})

def unova(response):
	return render(response, "main/regions/unova.html", {})

def kalos(response):
	return render(response, "main/regions/kalos.html", {})

def alola(response):
	return render(response, "main/regions/alola.html", {})

def galar(response):
	return render(response, "main/regions/galar.html", {})

def paldea(response):
	return render(response, "main/regions/paldea.html", {})