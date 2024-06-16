# Practica03_002_Algoritmo_de_Dijkstra_Vida
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

from collections import defaultdict, deque

def topological_sort(graph):
    # Función para realizar el orden topológico utilizando Kahn's Algorithm
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Cola de nodos con in-degree cero
    queue = deque([node for node in graph if in_degree[node] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) == len(graph):
        return topo_order
    else:
        # Si hay ciclos en el grafo, devolvemos None (esto no debería ocurrir en un DAG)
        return None

def organize_tasks(tasks):
    # Convertir lista de tareas en un grafo representado con diccionario
    graph = defaultdict(list)
    for task, dependencies in tasks.items():
        for dep in dependencies:
            graph[dep].append(task)  # Dependencia -> Tarea

    # Realizar orden topológico
    topo_order = topological_sort(graph)

    if topo_order:
        return topo_order
    else:
        return "Error: Existen ciclos en las dependencias de las tareas."

# Ejemplo de uso
if __name__ == "__main__":
    tasks = {
        'Tarea de control': [],
        'Tarea de IA': ['Tarea de control'],
        'Tarea de Vibraciones': ['Tarea de control'],
        'Tarea de Economia': ['Tarea de IA', 'Tarea de Vibraciones'],
        'Tarea de Vision': ['Tarea de Economia'],
        'Tarea de ingles': ['Tarea de Economia'],
        'Tarea de PLC': ['Tarea de Vision', 'Tarea de ingles']
    }

    # Organizar tareas basadas en dependencias
    ordered_tasks = organize_tasks(tasks)

    if isinstance(ordered_tasks, list):
        print("Orden óptimo de tareas:")
        for i, task in enumerate(ordered_tasks, start=1):
            print(f"{i}. {task}")
    else:
        print(ordered_tasks)

