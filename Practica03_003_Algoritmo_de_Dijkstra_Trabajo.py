# Practica03_003_Algoritmo_de_Dijkstra_Trabajo
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

import heapq

class Warehouse:
    def __init__(self):
        self.graph = {}

    def add_location(self, location):
        if location not in self.graph:
            self.graph[location] = {}

    def add_connection(self, location1, location2, distance):
        if location1 in self.graph and location2 in self.graph:
            self.graph[location1][location2] = distance
            self.graph[location2][location1] = distance  # Assuming bidirectional

    def dijkstra(self, start):
        distances = {location: float('inf') for location in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]  # (distance, location)
        visited = set()

        while priority_queue:
            current_distance, current_location = heapq.heappop(priority_queue)

            if current_location in visited:
                continue

            visited.add(current_location)

            for neighbor, weight in self.graph[current_location].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

warehouse = Warehouse()

# Se agregan ubicaciones
warehouse.add_location('AreaTB')
warehouse.add_location('Almacen')
warehouse.add_location('Oficina')
warehouse.add_location('Herramientas')

# Se definen conexiones y distancias
warehouse.add_connection('AreaTB', 'Almacen', 3)
warehouse.add_connection('AreaTB', 'Oficina', 5)
warehouse.add_connection('Almacen', 'Oficina', 2)
warehouse.add_connection('Almacen', 'Herramientas', 7)
warehouse.add_connection('Oficina', 'Herramientas', 4)

# Se Calculan las distancias más cortas desde un punto de inicio
start_location = 'AreaTB'
distances = warehouse.dijkstra(start_location)

# Se muestran resultados
print("**********************Taller de afinaciones******************")
print(f"Distancias más cortas desde '{start_location}' a cada punto:")
for location, distance in distances.items():
    print(f"Ubicación: {location}, Distancia: {distance} m")


