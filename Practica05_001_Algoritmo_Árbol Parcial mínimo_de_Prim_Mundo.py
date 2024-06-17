# Practica05_001_Algoritmo_Árbol Parcial mínimo_de_Prim_Mundo
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

import matplotlib.pyplot as plt
import networkx as nx

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, root1, root2):
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

def kruskal_mst(graph, is_max_cost=False):
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            edges.append((weight, u, v))

    # Sort edges by weight
    edges.sort(reverse=is_max_cost)

    vertices = list(graph.keys())
    ds = DisjointSet(vertices)
    mst = []
    total_cost = 0

    for weight, u, v in edges:
        root1 = ds.find(u)
        root2 = ds.find(v)

        if root1 != root2:
            ds.union(root1, root2)
            mst.append((u, v, weight))
            total_cost += weight

            if not is_max_cost:
                print(f"Added edge: ({u}-{v}), Cost: {weight}")
                print(f"Current MST: {mst}")
                print(f"Total Cost: {total_cost}\n")
            else:
                print(f"Added edge: ({u}-{v}), Cost: {weight} (Maximized)")
                print(f"Current Maximum Cost MST: {mst}")
                print(f"Total Maximum Cost: {total_cost}\n")

    return mst

def draw_graph(graph, mst_edges):
    G = nx.Graph()

    for u in graph:
        G.add_node(u)

    for u, v, weight in mst_edges:
        G.add_edge(u, v, weight=weight)

    pos = nx.spring_layout(G)
    edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}

    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=1.5, alpha=0.8, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    plt.title('Minimum/Maximum Cost Spanning Tree')
    plt.axis('off')
    plt.show()

graph = {
    'Casa': {'Mercado': 2, 'Hospital': 3},
    'Mercado': {'Casa': 2, 'Taller': 5, 'Hospital': 1},
    'Taller': {'Mercado': 5, 'Hospital': 4},
    'Hospital': {'Casa': 3, 'Mercado': 1, 'Taller': 4}
}

# Calcular MST utilizando Kruskal (Mínimo Coste)
print("Calculating Minimum Cost Spanning Tree (Kruskal)")
mst_edges = kruskal_mst(graph)
draw_graph(graph, mst_edges)

# Calcular MST utilizando Kruskal (Máximo Coste)
print("\nCalculating Maximum Cost Spanning Tree (Kruskal)")
mst_edges_max = kruskal_mst(graph, is_max_cost=True)
draw_graph(graph, mst_edges_max)
