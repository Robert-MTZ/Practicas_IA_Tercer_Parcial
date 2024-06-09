# Practica02_008_Ordenamiento_de_arbol
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

"""

El ordenamiento de árbol, también conocido como "Tree Sort", es un algoritmo de ordenamiento que utiliza un árbol binario de búsqueda para ordenar una lista de elementos.
En lugar de comparar directamente los elementos y realizar intercambios como en otros algoritmos de ordenamiento, el ordenamiento de árbol aprovecha las propiedades de un árbol binario
de búsqueda para ordenar los elementos de manera eficiente.

Funcionamiento:

Construcción del árbol: Se construye un árbol binario de búsqueda insertando cada elemento de la lista en el árbol. Cada elemento se inserta en el árbol de manera que cumpla con las reglas de orden del árbol binario de búsqueda: los elementos menores se colocan a la izquierda de un nodo y los elementos mayores se colocan a la derecha.
Recorrido en orden: Una vez que todos los elementos se han insertado en el árbol, se realiza un recorrido en orden del árbol. Este recorrido visita todos los nodos del árbol en orden ascendente (o descendente, dependiendo del orden deseado) de sus valores. Durante el recorrido en orden, los elementos se recopilan en una lista en el orden deseado.
Lista ordenada: Al finalizar el recorrido en orden, se obtiene una lista ordenada que contiene todos los elementos de la lista original, pero en el orden deseado. Esta lista es el resultado del ordenamiento de árbol.

"""

class TreeNode:
    def __init__(self, key):
        self.val = key  # Inicializa un nodo con un valor y sin hijos
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:  # Si el árbol está vacío, crea un nuevo nodo con el valor dado
        return TreeNode(key)
    else:
        if key < root.val: # Si el valor a insertar es menor que el valor del nodo actual
            root.left = insert(root.left, key) # Inserta el valor en el subárbol izquierdo recursivamente
        else:
            root.right = insert(root.right, key) # Inserta el valor en el subárbol derecho recursivamente
    return root

def inorder_traversal(root, sorted_list):
    if root:
        inorder_traversal(root.left, sorted_list) # Recorre el subárbol izquierdo
        sorted_list.append(root.val) # Agrega el valor del nodo actual a la lista ordenada
        inorder_traversal(root.right, sorted_list) # Recorre el subárbol derecho

def tree_sort(arr):
    root = None
    for element in arr:
        root = insert(root, element) # Construye el árbol insertando cada elemento de la lista
    sorted_list = []
    inorder_traversal(root, sorted_list)  # Realiza un recorrido en orden para obtener la lista ordenada
    return sorted_list

arr = [173, 65, 34, 75, 34, 23, 89, 103, 546, 1, 234, 1028] # Se le dan valores a la lista
sorted_arr = tree_sort(arr)
print("Lista ordenada:", sorted_arr) # Se imprime el resultado del ordenamiento
