# Practica03_001_Algoritmo_de_Dijkstra_Mundo
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

import heapq

def dijkstra(graph, start):
    # Inicializamos las distancias con infinito para todos los nodos
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # La distancia al nodo inicial es 0
    # Usaremos un heap para seleccionar el nodo con la distancia mínima
    priority_queue = [(0, start)]  # (distancia, nodo)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Si encontramos una distancia menor a la conocida, la actualizamos
        if current_distance > distances[current_node]:
            continue
        
        # Exploramos los vecinos del nodo actual
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Si encontramos un camino más corto hacia el vecino, lo actualizamos
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

if __name__ == "__main__":
    graph = {
        'Casa': {'Taller': 1, 'Hospital': 4},
        'Taller': {'Casa': 1, 'Hospital': 2, 'Mercado': 5},
        'Hospital': {'Casa': 4, 'Taller': 2, 'Mercado': 1},
        'Mercado': {'Taller': 5, 'Hospital': 1}
    }
    
    start_node = 'Taller'
    shortest_distances = dijkstra(graph, start_node)
    
    print("**************************GPS**************************") # Se imprime mensaje inicial 
    print("Las distancia más corta desde: ", start_node) # Se imprime cual es la distancia mas corta
    for node, distance in shortest_distances.items():
        print(f"Distancia hacia: {node} es de {distance} km") # Se imprimen todas las distancias
