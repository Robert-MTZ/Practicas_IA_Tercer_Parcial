# Practica04_002_Algoritmo_Árbol Parcial mínimo_de_Prim_Vida
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

import heapq
import matplotlib.pyplot as plt
import networkx as nx

def prim_mst(graph):
    start_node = list(graph.keys())[0]
    visited = {start_node}
    edges = [(cost, start_node, neighbor) for neighbor, cost in graph[start_node].items()]
    heapq.heapify(edges)
    mst = []

    while edges:
        cost, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, cost))

            for neighbor, cost in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (cost, v, neighbor))

        print(f"Visitando arista: {u} - {v}, Prioridad: {cost}")
        print(f"Tareas incluidas en el MST parcial: {mst}")
        print(f"Tareas visitadas: {visited}\n")

    return mst

def draw_graph(graph, mst_edges):
    G = nx.Graph()

    for node in graph:
        G.add_node(node)

    for u, v, cost in mst_edges:
        G.add_edge(u, v, weight=cost)

    pos = nx.spring_layout(G)
    edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}

    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=1.5, alpha=0.8, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    plt.title('Árbol de Mínimo Coste para Organización de Tareas Escolares')
    plt.axis('off')
    plt.show()

graph = {
    'Matemáticas': {'Física': 4, 'Control': 3, 'Ingles': 5},
    'Física': {'Matemáticas': 4, 'Control': 2},
    'Control': {'Matemáticas': 3, 'Física': 2, 'Ingles': 1},
    'Ingles': {'Matemáticas': 5, 'Control': 1}
}

# Calcular MST utilizando el algoritmo de Prim
mst_edges = prim_mst(graph)

# Mostrar gráficamente el MST
draw_graph(graph, mst_edges)
