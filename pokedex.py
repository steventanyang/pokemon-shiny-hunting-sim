import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")  
django.setup()


from main.models import Pokedex, Region, Pokemon
import requests


national_pokedex = Pokedex.objects.get(name="National")

def create_region(region_name): 
    Region.objects.create(Pokedex=national_pokedex, name=region_name)

#all_regions = Region.objects.all()
#for region in all_regions:
#    print(region.name)
#create_region("kanto")
#create_region("johto")
#create_region("hoenn")
#create_region("sinnoh")
#create_region("unova")
#create_region("kalos")
#create_region("alola")
#create_region("galar")
#create_region("paldea")
        
def add_pokemon_to_database(region):
    with open(f"main/pokemon_data/{region}.txt", "r") as file:
        database_region = Region.objects.get(name=region)
        for line in file:
            data = line.strip().split(", ")
            Pokemon.objects.create(
                Region = database_region,
                pokemon_id = data[0],
                name = data[1],
                pokemon_type = data[2],
                caught = False,
                shiny_caught = False
            )

#add_pokemon_to_database("kanto")
#add_pokemon_to_database("johto")
#add_pokemon_to_database("hoenn")
#add_pokemon_to_database("sinnoh")
#add_pokemon_to_database("unova")
#add_pokemon_to_database("kalos")
#add_pokemon_to_database("alola")
#add_pokemon_to_database("galar")
#add_pokemon_to_database("paldea")

def add_images_to_database():
    for id_number in range(1,1011):
        url = f"https://pokeapi.co/api/v2/pokemon/{id_number}/"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            pokemon_image = data['sprites']['front_default']

            try:
                pokemon = Pokemon.objects.get(pokemon_id=id_number)
                pokemon.image = pokemon_image
                pokemon.save()

            except Pokemon.DoesNotExist:
                print('oops')
        else :
            print("oops")

#add_images_to_database()
