import requests

# URLs de los Pokémon
pikachu = "https://pokeapi.co/api/v2/pokemon/pikachu"
charmander = "https://pokeapi.co/api/v2/pokemon/charmander"
rapidash = "https://pokeapi.co/api/v2/pokemon/rapidash"
graveler = "https://pokeapi.co/api/v2/pokemon/graveler"
vileplume = "https://pokeapi.co/api/v2/pokemon/vileplume"
wartortle = "https://pokeapi.co/api/v2/pokemon/wartortle"

# Menú
print("""
[1] Pikachu
[2] Charmander
[3] Rapidash
[4] Graveler
[5] Vileplume
[6] Wartortle
""")

# --- Selección del primer Pokémon ---
pokemon1 = input("Selecciona el primer Pokémon (número del 1 al 6): ")

if pokemon1 == "1":
    url1 = pikachu
elif pokemon1 == "2":
    url1 = charmander
elif pokemon1 == "3":
    url1 = rapidash
elif pokemon1 == "4":
    url1 = graveler
elif pokemon1 == "5":
    url1 = vileplume
elif pokemon1 == "6":
    url1 = wartortle
else:
    print("Solo puedes seleccionar de 1 a 6.")
    exit()

# --- Selección del segundo Pokémon ---
pokemon2 = input("Selecciona el segundo Pokémon (número del 1 al 6): ")

if pokemon2 == "1":
    url2 = pikachu
elif pokemon2 == "2":
    url2 = charmander
elif pokemon2 == "3":
    url2 = rapidash
elif pokemon2 == "4":
    url2 = graveler
elif pokemon2 == "5":
    url2 = vileplume
elif pokemon2 == "6":
    url2 = wartortle
else:
    print("Solo puedes seleccionar de 1 a 6.")
    exit()

# --- Obtener los datos de ambos ---
respuesta1 = requests.get(url1)
respuesta2 = requests.get(url2)

if respuesta1.status_code == 200 and respuesta2.status_code == 200:
    datos1 = respuesta1.json()
    datos2 = respuesta2.json()

    # Obtener nombre y ataque de cada Pokémon
    nombre1 = datos1["name"].capitalize()
    nombre2 = datos2["name"].capitalize()

    ataque1 = 0
    ataque2 = 0

    for stat in datos1["stats"]:
        if stat["stat"]["name"] == "attack":
            ataque1 = stat["base_stat"]

    for stat in datos2["stats"]:
        if stat["stat"]["name"] == "attack":
            ataque2 = stat["base_stat"]

    # Mostrar resultados
    print("\nATAQUE DE AMBOS")
    print(f"{nombre1}: Ataque = {ataque1}")
    print(f"{nombre2}: Ataque = {ataque2}")

    # Determinar ganador
    print("\n--- RESULTADO DE LA BATALLA ---")
    if ataque1 > ataque2:
        print(f"{nombre1} GANA POR SU ATAQUE DE {ataque1}!")
    elif ataque2 > ataque1:
        print(f"{nombre2} GANA POR SU ATAQUE DE {ataque2}!")
    else:
        print("ES UN EMPATE")

else:
    print("Error al obtener los datos del pokemon.")
