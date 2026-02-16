import requests

pikachu = "https://pokeapi.co/api/v2/pokemon/pikachu"
charmander = "https://pokeapi.co/api/v2/pokemon/charmander"
rapidash = "https://pokeapi.co/api/v2/pokemon/rapidash"
graveler = "https://pokeapi.co/api/v2/pokemon/graveler"
vileplume = "https://pokeapi.co/api/v2/pokemon/vileplume"
wartortle = "https://pokeapi.co/api/v2/pokemon/wartortle"

print("""
[1] Pikachu
[2] Charmander
[3] Rapidash
[4] Graveler
[5] Vileplume
[6] Wartortle
""")

seleccionar = input("Selecciona un Pokémon (número del 1 al 6): ")

# Según la elección, se guarda la URL correspondiente
if seleccionar == "1":
    url = pikachu
elif seleccionar == "2":
    url = charmander
elif seleccionar == "3":
    url = rapidash
elif seleccionar == "4":
    url = graveler
elif seleccionar == "5":
    url = vileplume
elif seleccionar == "6":
    url = wartortle
else:
    print("Opción inválida. Opciones disponibles: 1-2-3-4-5-6")
    exit()

# Hacemos la solicitud a la API
response = requests.get(url)

# Si la respuesta es correcta (código 200)
if response.status_code == 200:
    data = response.json()

    print("Nombre:", data["name"].capitalize())
    print(" ")

    # Mostrar tipos
    for tipo in data["types"]:
        print("Tipo:", tipo["type"]["name"])
        print(" ")

    # Mostrar habilidades
    print("Habilidades:")
    for habilidad in data["abilities"]:
        print("-", habilidad["ability"]["name"])

    # Mostrar estadísticas
    print("Estadísticas:")
    for stat in data["stats"]:
        print("-", stat["stat"]["name"], ":", stat["base_stat"])

else:
    print("Error al obtener los data del Pokémon.")
