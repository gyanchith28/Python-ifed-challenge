import json, requests
from os import name

def ability(x):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/%s/' %(x))
    poke = json.loads(response.text)
    lst1 = []

    for i in range(len(poke['abilities'])):
        lst1.append(poke['abilities'][i]['ability']['name'])
    
    return lst1