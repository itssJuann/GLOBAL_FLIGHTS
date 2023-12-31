# -*- coding: utf-8 -*-
"""LAB_2_EDII_ND_BA_DM_JR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XNuz6KqJjfFbHOtQGoYsZUSZ_NZOQ9jC

> LABORATORIO 2

 - --Integrantes de Laboratorio--

- Nelson Diaz Pizarro - 20018943 - NRC 2445
- Bernardo Alvarez Ciro - NRC 2446
- Dieb Maloof Ramirez - 200183841 - NRC 2446
- Juan de la Rosa Palacio - 200180072 - NRC 2446
"""

import pandas as pd
df = pd.read_csv("/content/flights_final.csv")

df

## Mapa con la geolocalizaciòn

import csv
import folium

# Crear un mapa centrado en una ubicación específica
mapa = folium.Map(location=[0, 0], zoom_start=2)  # El zoom_start determina el nivel de acercamiento inicial

# Contador para limitar a los primeros 100 vuelos
contador = 0

# Leer el archivo CSV y agregar marcadores al mapa para los primeros 100 vuelos
with open('flights_final.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Obtener la latitud y longitud del aeropuerto de salida y llegada desde el archivo CSV
        lat_salida, lon_salida, lat_llegada, lon_llegada = float(row['Source Airport Latitude']), float(row['Source Airport Longitude']), float(row['Destination Airport Latitude']), float(row['Destination Airport Longitude'])

        # Agregar marcadores para el aeropuerto de salida y llegada
        folium.Marker([lat_salida, lon_salida], popup='Aeropuerto de Salida').add_to(mapa)
        folium.Marker([lat_llegada, lon_llegada], popup='Aeropuerto de Llegada').add_to(mapa)

        # Conectar los aeropuertos con una línea
        folium.PolyLine([(lat_salida, lon_salida), (lat_llegada, lon_llegada)], color="blue", weight=2.5, opacity=1).add_to(mapa)

        # Incrementar el contador
        contador += 1

        # Salir del bucle después de 100 vuelos (Con mas de 100 el tiempo de carga es mayor)
        if contador >= 100:
            break

# Mostrar el mapa
mapa

## Dado un primer vértice por el código del aeropuerto o seleccionado mediante la interfaz gráfica:
# - Mostrar la información correspondiente al aeropuerto (código, nombre, ciudad, país, latitud y longitud)
# - Mostrar la información (código, nombre, ciudad, país, latitud y longitud)de los 10 aeropuertos cuyos caminos mínimos desde el vértice dado sean los más largos. Adicionalmente, se debe mostrar la distancia de loscaminos.


## Muestra el peso de las Aristas (Distancia)
## Distancia entre dos coordenadas geográficas (Formula de Haversine)

import csv
import folium
from math import radians, sin, cos, sqrt, atan2

# Función para calcular la distancia entre dos puntos usando la fórmula de Haversine
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radio de la Tierra en kilómetros
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

# Crear un mapa centrado en una ubicación específica
mapa = folium.Map(location=[0, 0], zoom_start=2)  # El zoom_start determina el nivel de acercamiento inicial

# Leer el archivo CSV y agregar marcadores al mapa para los primeros 100 vuelos
with open('flights_final.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    contador = 0
    for row in reader:
        lat_salida, lon_salida, lat_llegada, lon_llegada = float(row['Source Airport Latitude']), float(row['Source Airport Longitude']), float(row['Destination Airport Latitude']), float(row['Destination Airport Longitude'])

        # Calcular la distancia entre las terminales de salida y llegada
        distancia = haversine(lat_salida, lon_salida, lat_llegada, lon_llegada)

        # Agregar marcadores para el aeropuerto de salida y llegada, con la distancia como etiqueta
        folium.Marker([lat_salida, lon_salida], popup=f'Aeropuerto de Salida\nDistancia: {distancia:.2f} km').add_to(mapa)
        folium.Marker([lat_llegada, lon_llegada], popup=f'Aeropuerto de Llegada\nDistancia: {distancia:.2f} km').add_to(mapa)

        # Conectar los aeropuertos con una línea, también mostrando la distancia como etiqueta
        folium.PolyLine([(lat_salida, lon_salida), (lat_llegada, lon_llegada)],
                        color="blue", weight=2.5, opacity=1,
                        popup=f'Distancia: {distancia:.2f} km').add_to(mapa)

        # Incrementar el contador
        contador += 1

        # Salir del bucle después de 100 vuelos  (Con mas DE 100 Vuelos, el tiempo de carga es mayor)
        if contador >= 100:
            break

# Mostrar el mapa
mapa

# Continuacion del Vertice 1
## Dado un primer vértice por el código del aeropuerto o seleccionado mediante la interfaz gráfica:
# - Mostrar la información correspondiente al aeropuerto (código, nombre, ciudad, país, latitud y longitud)
# - Mostrar la información (código, nombre, ciudad, país, latitud y longitud)de los 10 aeropuertos cuyos caminos mínimos desde el vértice dado sean los más largos. Adicionalmente, se debe mostrar la distancia de loscaminos.

import csv

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radio de la Tierra en kilómetros
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance
# Leer el archivo CSV y construir una lista de vuelos para los primeros 100 vuelos
flights = []
with open('flights_final.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    flight_count = 0
    for row in reader:
        source_code = row['Source Airport Code']
        dest_code = row['Destination Airport Code']
        source_lat, source_lon, dest_lat, dest_lon = float(row['Source Airport Latitude']), float(row['Source Airport Longitude']), float(row['Destination Airport Latitude']), float(row['Destination Airport Longitude'])
        distance = haversine(source_lat, source_lon, dest_lat, dest_lon)
        flights.append((source_code, dest_code, distance))

        flight_count += 1
        if flight_count >= 100:
            break

# Obtener el código del aeropuerto de salida del usuario
user_input = input("Ingrese el código del aeropuerto de salida (por ejemplo, 'JFK'): ")

# Construir un grafo no dirigido basado en los vuelos
graph = {}
for source, dest, distance in flights:
    if source not in graph:
        graph[source] = []
    if dest not in graph:
        graph[dest] = []
    graph[source].append((dest, distance))
    graph[dest].append((source, distance))

# Función de Búsqueda en Profundidad (DFS) para encontrar todos los caminos desde un nodo dado
def dfs(current, visited, path, all_paths):
    visited.add(current)
    for neighbor, distance in graph[current]:
        if neighbor not in visited:
            dfs(neighbor, visited.copy(), path + [(neighbor, distance)], all_paths)
    all_paths.append(path)

# Encontrar todos los caminos desde el aeropuerto de partida
all_paths = []
dfs(user_input, set(), [(user_input, 0)], all_paths)

# Seleccionar el camino más largo
longest_path = max(all_paths, key=lambda x: sum([distance for _, distance in x]))

# Mostrar la información del aeropuerto de salida
print(f"Información del aeropuerto de salida ({user_input}):")
with open('flights_final.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Source Airport Code'] == user_input:
            print(f"Nombre: {row['Source Airport Name']}")
            print(f"Ciudad: {row['Source Airport City']}")
            print(f"Latitud: {row['Source Airport Latitude']}")
            print(f"Longitud: {row['Source Airport Longitude']}")
            break

# Mostrar la información del aeropuerto de llegada en el camino más largo
destination_airport_longest = longest_path[-1][0]
print(f"\nInformación del aeropuerto de llegada en el camino más largo ({destination_airport_longest}):")
with open('flights_final.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Destination Airport Code'] == destination_airport_longest:
            print(f"Nombre: {row['Destination Airport Name']}")
            print(f"Ciudad: {row['Destination Airport City']}")
            print(f"Latitud: {row['Destination Airport Latitude']}")
            print(f"Longitud: {row['Destination Airport Longitude']}")
            break

# Seleccionar los 10 caminos más largos
sorted_paths = sorted(all_paths, key=lambda x: sum([distance for _, distance in x]), reverse=True)[:10]

# Mostrar la información de los 10 caminos más largos (Apropia correctamente en consola todos los vuelos finales registrados)
for i, path in enumerate(sorted_paths, start=1):
    total_distance = sum([distance for _, distance in path])
    airports = [node for node, _ in path]
    destination_airport = airports[-1]
    print(f"\nCamino #{i}:")
    print(" -> ".join(airports))
    print(f"Distancia total: {total_distance:.2f} km")
    print(f"Información del aeropuerto de llegada: ")
    with open('flights_final.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Destination Airport Code'] == destination_airport:
                print(f"Nombre: {row['Destination Airport Name']}")
                print(f"Ciudad: {row['Destination Airport City']}")
                print(f"Latitud: {row['Destination Airport Latitude']}")
                print(f"Longitud: {row['Destination Airport Longitude']}")
                break



"""- Dado un segundo vértice por el código del aeropuerto o seleccionado
mediante la interfaz gráfica:

-- Mostrar el camino mínimo entre el primer y el segundo vértice sobre el
mapa de la interfaz gráfica, pasando por cada uno de los vértices
intermedios del camino. Para cada vértice intermedio se debe mostrar la
información del aeropuerto (código, nombre, ciudad, país, latitud y
longitud).

"""

### Dado un segundo vértice por el código del aeropuerto o seleccionado mediante la interfaz gráfica:
## - Mostrar el camino mínimo entre el primer y el segundo vértice sobre el mapa de la interfaz gráfica, pasando por cada uno de los vértices intermedios del camino.
# Para cada vértice intermedio se debe mostrar la  información del aeropuerto (código, nombre, ciudad, país, latitud y longitud).

## Muestra la informacion de los vuelos y camino por el que pasa

import csv
import networkx as nx
from math import radians, sin, cos, sqrt, atan2

# Función para calcular la distancia entre dos puntos usando la fórmula de Haversine
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radio de la Tierra en kilómetros
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

# Leer el archivo CSV y construir una lista de vuelos para los primeros 100 vuelos
flights = []
with open('flights_final.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    flight_count = 0
    for row in reader:
        source_code = row['Source Airport Code']
        dest_code = row['Destination Airport Code']
        source_lat, source_lon = float(row['Source Airport Latitude']), float(row['Source Airport Longitude'])
        dest_lat, dest_lon = float(row['Destination Airport Latitude']), float(row['Destination Airport Longitude'])
        distance = haversine(source_lat, source_lon, dest_lat, dest_lon)
        flights.append((source_code, dest_code, distance))

        flight_count += 1
        if flight_count >= 66929:  ## Apropia con todos los registros finales registrados
            break

# Continúa con el resto del código (Dijkstra y mostrar información de aeropuertos)...

# (Código Dijkstra y mostrar información de aeropuertos)


# Obtener el código del aeropuerto de salida del usuario
user_input_start = input("Ingrese el código del aeropuerto de salida (por ejemplo, 'JFK'): ")

# Obtener el código del aeropuerto de llegada del usuario
user_input_end = input("Ingrese el código del aeropuerto de llegada (por ejemplo, 'LAX'): ")

# Construir un grafo dirigido basado en los vuelos
G = nx.DiGraph()
for source, dest, distance in flights:
    G.add_edge(source, dest, weight=distance)

# Encontrar el camino mínimo entre el aeropuerto de salida y el aeropuerto de llegada utilizando Dijkstra
try:
    shortest_path = nx.shortest_path(G, source=user_input_start, target=user_input_end, weight='weight')
except nx.NetworkXNoPath:
    print("No se encontró un camino entre los aeropuertos seleccionados.")
    shortest_path = []

# Función para obtener información de un aeropuerto
def get_airport_info(code):
    with open('flights_final.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Source Airport Code'] == code:
                return {
                    'Código': row['Source Airport Code'],
                    'Nombre': row['Source Airport Name'],
                    'Ciudad': row['Source Airport City'],
                    'País': row['Source Airport Country'],
                    'Latitud': row['Source Airport Latitude'],
                    'Longitud': row['Source Airport Longitude']
                }
            elif row['Destination Airport Code'] == code:
                return {
                    'Código': row['Destination Airport Code'],
                    'Nombre': row['Destination Airport Name'],
                    'Ciudad': row['Destination Airport City'],
                    'País': row['Destination Airport Country'],
                    'Latitud': row['Destination Airport Latitude'],
                    'Longitud': row['Destination Airport Longitude']
                }
    return None

# Mostrar información de aeropuerto de salida
airport_start_info = get_airport_info(user_input_start)
if airport_start_info:
    print()
    print("Información del aeropuerto de salida:")
    for key, value in airport_start_info.items():
        print(f"{key}: {value}")

# Mostrar información de aeropuerto de llegada
airport_end_info = get_airport_info(user_input_end)
if airport_end_info:
    print("\nInformación del aeropuerto de llegada:")
    for key, value in airport_end_info.items():
        print(f"{key}: {value}")

# Mostrar información de aeropuertos intermedios en el camino mínimo
if shortest_path:
    print("\nAeropuertos intermedios en el camino:")
    for airport_code in shortest_path[1:-1]:  # Excluyendo el de salida y llegada
        airport_info = get_airport_info(airport_code)
        if airport_info:
            print(f"\nInformación del aeropuerto {airport_code}:")
            for key, value in airport_info.items():
                print(f"{key}: {value}")

## Grafica el recorrido de los vuelos

import csv
import folium
from math import radians, sin, cos, sqrt, atan2
import networkx as nx

# Código para calcular la distancia entre dos puntos usando la fórmula de Haversine
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radio de la Tierra en kilómetros
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

# Crear un mapa centrado en una ubicación específica
mapa = folium.Map(location=[0, 0], zoom_start=2)  # El zoom_start determina el nivel de acercamiento inicial

# Leer el archivo CSV y construir una lista de vuelos para los primeros 100 vuelos
flights = []
with open('flights_final.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    flight_count = 0
    for row in reader:
        source_code = row['Source Airport Code']
        dest_code = row['Destination Airport Code']
        source_lat, source_lon, dest_lat, dest_lon = float(row['Source Airport Latitude']), float(row['Source Airport Longitude']), float(row['Destination Airport Latitude']), float(row['Destination Airport Longitude'])
        distance = haversine(source_lat, source_lon, dest_lat, dest_lon)
        flights.append((source_code, dest_code, distance))

        flight_count += 1
        if flight_count >= 66929:  ## Apropia con todos los registros finales registrados
            break

# Obtener el código del aeropuerto de salida del usuario
user_input_start = input("Ingrese el código del aeropuerto de salida (por ejemplo, 'JFK, EN MAYUSCULAS'): ")

# Obtener el código del aeropuerto de llegada del usuario
user_input_end = input("Ingrese el código del aeropuerto de llegada (por ejemplo, 'LAX, EN MAYUSCULAS'): ")

# Construir un grafo dirigido basado en los vuelos
G = nx.DiGraph()
for source, dest, distance in flights:
    G.add_edge(source, dest, weight=distance)

# Encontrar el camino mínimo entre el aeropuerto de salida y el aeropuerto de llegada utilizando Dijkstra
try:
    shortest_path = nx.shortest_path(G, source=user_input_start, target=user_input_end, weight='weight')
except nx.NetworkXNoPath:
    print("No se encontró un camino entre los aeropuertos seleccionados.")
    shortest_path = []

# Función para agregar un marcador para un aeropuerto con información
def add_airport_marker(code):
    with open('flights_final.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Source Airport Code'] == code:
                folium.Marker([float(row['Source Airport Latitude']), float(row['Source Airport Longitude'])],
                              popup=f"Código: {row['Source Airport Code']}<br>Nombre: {row['Source Airport Name']}<br>Ciudad: {row['Source Airport City']}<br>País: {row['Source Airport Country']}<br>Latitud: {row['Source Airport Latitude']}<br>Longitud: {row['Source Airport Longitude']}",
                              icon=folium.Icon(color='green')).add_to(mapa)
            elif row['Destination Airport Code'] == code:
                folium.Marker([float(row['Destination Airport Latitude']), float(row['Destination Airport Longitude'])],
                              popup=f"Código: {row['Destination Airport Code']}<br>Nombre: {row['Destination Airport Name']}<br>Ciudad: {row['Destination Airport City']}<br>País: {row['Destination Airport Country']}<br>Latitud: {row['Destination Airport Latitude']}<br>Longitud: {row['Destination Airport Longitude']}",
                              icon=folium.Icon(color='red')).add_to(mapa)

# Función para agregar líneas que conectan los aeropuertos
def add_airport_lines(airports):
    for i in range(len(airports) - 1):
        source = airports[i]
        dest = airports[i + 1]
        source_row = next((row for row in csv.DictReader(open('flights_final.csv')) if row['Source Airport Code'] == source))
        source_lat, source_lon = float(source_row['Source Airport Latitude']), float(source_row['Source Airport Longitude'])

        dest_row = next((row for row in csv.DictReader(open('flights_final.csv')) if row['Source Airport Code'] == dest))
        dest_lat, dest_lon = float(dest_row['Source Airport Latitude']), float(dest_row['Source Airport Longitude'])

        folium.PolyLine([(source_lat, source_lon), (dest_lat, dest_lon)], color="blue", weight=2.5).add_to(mapa)

# Agregar marcadores y líneas para los aeropuertos en el camino mínimo
if shortest_path:
    add_airport_marker(shortest_path[0])  # Marcador del aeropuerto de salida
    add_airport_marker(shortest_path[-1])  # Marcador del aeropuerto de llegada
    add_airport_lines(shortest_path)  # Líneas que conectan los aeropuertos

# Mostrar el mapa
mapa