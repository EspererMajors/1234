import requests 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '05def516386e82d1e9cc6963f45828d2'
HEADER = {'Content_Type' : 'application/json', 'trainer_token' : TOKEN}
body_creating_pokemon = {
    "name": "Картошка",
    "photo_id": 12
    }


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json=body_creating_pokemon)
print(response_create.json())

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_change = {
    "pokemon_id": pokemon_id,
    "name": "Булавка",
    "photo_id": 2
}

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.json())

body_pokebol = {
    "pokemon_id": pokemon_id
}

response_pokebol = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokebol)
print(response_pokebol.json())
