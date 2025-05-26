import requests
import pytest 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '05def516386e82d1e9cc6963f45828d2'
HEADER = {'Content_Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '33463'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID} )
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID} )
    assert response_get.json()['data'][0]['trainer_id']== TRAINER_ID
     
