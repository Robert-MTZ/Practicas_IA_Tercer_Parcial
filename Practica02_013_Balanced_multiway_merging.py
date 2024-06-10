# Practica02_013_Balanced_multiway_merging
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

"""

El "Balanced Multiway Merging" es un algoritmo de ordenación que se utiliza para ordenar grandes cantidades de datos almacenados en múltiples archivos. Es una extensión del algoritmo
de "Multiway Merging" que permite manejar un número variable de archivos de entrada de manera más eficiente.

Funcionamiento:

División inicial: Se divide el conjunto de datos en múltiples archivos más pequeños que puedan caber en la memoria principal de la computadora. Estos archivos pequeños se denominan "runs" o "tramos".
Ordenación interna: Cada uno de estos archivos pequeños se ordena internamente utilizando un algoritmo de ordenación eficiente, como QuickSort o MergeSort. Esto garantiza que cada "run" esté ordenado individualmente.
Fusión múltiple balanceada: A diferencia del algoritmo de "Multiway Merging" tradicional, en el que se fusionan todos los "runs" a la vez, el "Balanced Multiway Merging" utiliza una estrategia de fusión múltiple balanceada. En lugar de fusionar todos los "runs" a la vez, se fusionan en grupos más pequeños de manera iterativa y equilibrada. Esto significa que, en cada iteración, se fusionan solo un número limitado de "runs", lo que ayuda a evitar la sobrecarga de memoria y mejora la eficiencia del proceso de fusión.
Iteración: Este proceso de fusión múltiple balanceada se repite hasta que todos los "runs" se fusionen en un solo archivo ordenado.

"""

import heapq # Esta libreria proporciona funciones para implementar estructuras de datos basadas en montículos (heaps). Un montículo, también conocido como cola de prioridad, es una estructura de datos en forma de árbol binario en la que todos los nodos de un nivel dado (excepto posiblemente el último, que se llena de izquierda a derecha) están completamente llenos, y todos los nodos están ordenados de acuerdo con una relación de orden específica.

def balanced_multiway_merging(adj_lists):
    # Inicializamos un heap con el primer nodo de cada lista de adyacencia
    heap = [(neighbors[0], node, 0) for node, neighbors in adj_lists.items() if neighbors]

    # Inicializamos el resultado como un diccionario vacío para almacenar el resultado de la fusión
    merged_adj_list = {}

    # Iteramos hasta que el heap esté vacío
    while heap:
        # Extraemos el nodo con el menor valor de adyacencia del heap
        min_neighbor, node, idx = heapq.heappop(heap)

        # Agregamos el nodo extraído al resultado fusionado
        if node not in merged_adj_list:
            merged_adj_list[node] = []

        merged_adj_list[node].append(min_neighbor)

        # Si aún hay vecinos en la lista de adyacencia del nodo extraído, los agregamos al heap
        if idx + 1 < len(adj_lists[node]):
            next_neighbor = adj_lists[node][idx + 1]
            heapq.heappush(heap, (next_neighbor, node, idx + 1))

    return merged_adj_list

# Listas de adyacencia de un grafo no dirigido
adj_lists = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'C'],
    'E': ['B', 'F'],
    'F': ['E']
}

# Aplicamos el Balanced Multiway Merging a las listas de adyacencia del grafo
merged_adj_list = balanced_multiway_merging(adj_lists)
print("Lista de adyacencia fusionada:", merged_adj_list)




