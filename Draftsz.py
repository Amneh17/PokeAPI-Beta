import requests
import json
import os
import random

#this function each execution provide different ID for pokemon.
def random_id():
    random_id=random.randint(1,1025)
    return random_id

def retrieving_data(id):
    new_dictionary = {}
    pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}').json()
    # retrieve id , is_default parameters for the pokemon
    keys = ['id', 'is_default']
    for key in keys:
        new_dictionary[key] = pokemon[key]
    # retrieve the pokemon name
    new_dictionary['pokemon_name'] = pokemon['forms'][0]['name']
    #print(new_dictionary)
    return new_dictionary

# check if the data is exists in my file
def if_pokemon_exists(pokemon_data , filename='pokemon_data.json' ):
    if os.path.exists(filename):
        with open(filename, 'r') as json_file:
            try:
                data = json.load(json_file)

            except:
            # Handle the case where the file is empty or corrupted
                data = []
    else:
        # If file doesn't exist, initialize empty list
        data=[]

    # Check if the Pokémon with the same ID exists
    for i in data:
        if i['id'] == pokemon_data['id']:
             print(f'the pokemon exists , can"t be added')
             return True
    # If Pokémon doesn't exist, append it to the list and save it back
    data.append(pokemon_data)
    #Adding the Data of the Pokemon
    with open(filename , 'w') as json_file:
        json.dump(data , json_file , indent=4)
    print(f'The Pokémon with ID {pokemon_data["id"]} has been added')
    return False



def main():
    # Input the Pokémon ID you want to retrieve
    provided_id=random_id()


    # Call the first function to retrieve the data
    pokemon_data = retrieving_data(provided_id)

    # Call the second function to check if the Pokémon exists
    if not if_pokemon_exists(pokemon_data):
        print(f'Pokémon with ID {pokemon_data["id"]} can be added.')
        print(pokemon_data)
    else:
        print(f'Pokémon with ID {pokemon_data["id"]} already exists.')
        print(pokemon_data)

# This ensures that the main function is called when the script is executed
if __name__ == "__main__":
    main()
