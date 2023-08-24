import requests

#getting data from pokeapi
def fetchdata(id):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}/"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else :
        print("oops")

#putting data in txtfile
def get_pokemon(region, lower_bound, upper_bound):
    with open(f"{region}.txt", "w") as file:
        pokemon_id = list(range(lower_bound, upper_bound))
        for number in pokemon_id:
            pokemon = fetchdata(str(number))
            pokemon_id = pokemon['id']
            pokemon_name = pokemon['name']
            pokemon_type = pokemon['types'][0]['type']['name']
            file.write(f"{pokemon_id}, {pokemon_name}, {pokemon_type}\n")

#get_pokemon("kanto",1,152)
#get_pokemon("johto",152,252)
#get_pokemon("hoenn",252,387)
#get_pokemon("sinnoh",387,494)
#get_pokemon("unova",494,650)
#get_pokemon("kalos",650,722)
#get_pokemon("alola",722,810)
#get_pokemon("galar",810,906)
#get_pokemon("paldea",906,1011)
