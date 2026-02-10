import requests

pikachu = "https://pokeapi.co/api/v2/pokemon/pikachu"
charmander = "https://pokeapi.co/api/v2/pokemon/charmander"
rapidash = "https://pokeapi.co/api/v2/pokemon/rapidash"
graveler = "https://pokeapi.co/api/v2/pokemon/graveler"
vileplume = "https://pokeapi.co/api/v2/pokemon/vileplume"

print("""
[1] Pikachu
[2] Charmander
[3] Rapidash
[4] Graveler
[5] Vileplume
""")

seleccionar = input("Selecciona un Pokémon (número del 1 al 5): ")

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
else:
    print("Solo puedes seleccionar de 1 a 5.")
    exit()

# Hacemos la solicitud a la API
response = requests.get(url)

# Si la respuesta es correcta (código 200)
if response.status_code == 200:
    datos = response.json()

    print("Nombre:", datos["name"].capitalize())

    # Mostrar tipos
    for tipo in datos["types"]:
        print("Tipo:", tipo["type"]["name"])

    # Mostrar habilidades
    print("Habilidades:")
    for habilidad in datos["abilities"]:
        print("-", habilidad["ability"]["name"])

    # Mostrar estadísticas
    print("Estadísticas:")
    for stat in datos["stats"]:
        print("-", stat["stat"]["name"], ":", stat["base_stat"])

else:
    print("Error al obtener los datos del Pokémon.")
