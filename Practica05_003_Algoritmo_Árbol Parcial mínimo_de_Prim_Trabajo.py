# Practica05_003_Algoritmo_Árbol Parcial mínimo_de_Prim_Trabajo
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

import matplotlib.pyplot as plt
import networkx as nx

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

def kruskal_mst_max_min(graph):
    edges = []
    for u in graph:
        for v, cost in graph[u].items():
            edges.append((cost, u, v))
    
    edges.sort()  # Ordenar aristas por costo (de menor a mayor)

    parent = {}
    rank = {}
    mst_min = []
    mst_max = []

    for node in graph:
        parent[node] = node
        rank[node] = 0

    for cost, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_min.append((u, v, cost))
            mst_max.append((u, v, cost))  # Para el máximo coste, simplemente se agregan todas las aristas
            print(f"Conexión establecida en MST Mínimo: {u} - {v}, Costo: {cost}")
            print(f"Secuencia de conexiones parcial en MST Mínimo: {mst_min}\n")

    return mst_min, mst_max

def draw_graph(graph, mst_edges_min, mst_edges_max):
    G = nx.Graph()

    for u in graph:
        G.add_node(u)

    for u, v, cost in mst_edges_min:
        G.add_edge(u, v, weight=cost)

    pos = nx.spring_layout(G)
    labels_min = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_min)

    plt.title('Árbol de Mínimo Coste para Organización de un Taller Mecánico')
    plt.show()

    G = nx.Graph()  # Nuevo grafo para el máximo coste

    for u in graph:
        G.add_node(u)

    for u, v, cost in mst_edges_max:
        G.add_edge(u, v, weight=cost)

    labels_max = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_max)

    plt.title('Árbol de Máximo Coste para Organización de un Taller Mecánico')
    plt.show()

# Ejemplo de grafo ponderado para organizar un taller mecánico
graph = {
    'AreaTB': {'Almacen': 6, 'Oficina': 5, 'Herramientas': 10},
    'Almacen': {'AreaTB': 6, 'Oficina': 4, 'Herramientas': 7},
    'Oficina': {'AreaTB': 5, 'Almacen': 4, 'Herramientas': 3},
    'Herramientas': {'AreaTB': 10, 'Almacen': 7, 'Oficina': 3}
}

# Calcular MST mínimo y máximo utilizando Kruskal para organizar un taller mecánico
mst_edges_min, mst_edges_max = kruskal_mst_max_min(graph)

# Mostrar gráficamente los MST mínimo y máximo
draw_graph(graph, mst_edges_min, mst_edges_max)

