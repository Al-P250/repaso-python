import random
from pprint import pprint

import requests


weather_url="https://www.eltiempo.es/"
api_url="https://pokeapi.co/api/v2/pokemon/"

poke=input("Dime un pokemon => ")

response=requests.get(api_url+poke)
pokemon=response.json()

tipos_response=pokemon["types"]

tipos=[]
for i in range(len(tipos_response)):
    tipos.append(tipos_response[i]["type"]["name"])


descripcion_url=pokemon["species"]["url"]
descripcion_info=requests.get(descripcion_url).json()
descripcion=""
for i in range(len(descripcion_info["flavor_text_entries"])-1):
    if descripcion_info["flavor_text_entries"][i]["language"]["name"]=="es":
        descripcion=descripcion_info["flavor_text_entries"][i]["flavor_text"]

print(descripcion)


movimientos_response=pokemon["moves"]

movimientos=[]

for i in range(4):
    movimiento_r=movimientos_response.pop(random.randint(0,len(movimientos_response)))
    movimiento_url=movimiento_r["move"]["url"]
    movimiento_info=requests.get(movimiento_url).json()
    movimientos.append({"move_name": movimiento_info["names"][5]["name"], "move_power":movimiento_info["power"], "move_pp":movimiento_info["pp"]})
pprint(movimientos)


stats_response=pokemon["stats"]

stats=[]
for i in range(len(stats_response)):
    stats.append({stats_response[i]["stat"]["name"]:stats_response[i]["base_stat"]})


pprint(stats)
'''for el in pokemon:
    pprint(f"datos[el]: {pokemon[el]}")
    print(f"el: {el}")'''