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
def get_pokemon(file, lower_bound, upper_bound):
    with open(f"{file}.txt", "w") as file:
        pokemon_id = list(range(lower_bound, upper_bound))
        for number in pokemon_id:
            pokemon = fetchdata(str(number))
            pokemon_image = pokemon['sprites']['front_default']
            if pokemon_image:
                file.write(f"{pokemon_image}\n")
            else: 
                file.write("no image \n")

get_pokemon("imagetest",1,1011)



###you need to find old version of this file and replace it because the github doesn't carry your database changes. 