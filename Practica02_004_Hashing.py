# Practica02_004_Hashing
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

"""

El hashing no es un algoritmo de ordenamiento per se, sino una técnica utilizada en computación para mapear datos de tamaño variable a datos de tamaño fijo.
Es especialmente útil en la creación de estructuras de datos como tablas hash, que permiten un acceso rápido a los elementos almacenados.

Funcionamiento:

Función de Hash: Se utiliza una función de hash para convertir los datos de entrada (llamados claves) en un valor hash, que es un valor entero. Esta función toma la clave como entrada y genera un valor hash único. La idea es que la función de hash distribuya las claves de manera uniforme sobre un rango de valores posibles, pero en la práctica, pueden ocurrir colisiones, donde dos claves diferentes generan el mismo valor hash.
Tabla Hash: La tabla hash es una estructura de datos que utiliza un arreglo para almacenar los elementos. Cada elemento se almacena en una posición determinada del arreglo, que se calcula utilizando su valor hash como índice. Si ocurre una colisión, es decir, dos claves generan el mismo valor hash, se utiliza una técnica de resolución de colisiones para manejar este escenario, como encadenamiento o direccionamiento abierto.
Acceso y Almacenamiento: Para acceder a un elemento en la tabla hash, se calcula su valor hash y se utiliza como índice para acceder al arreglo. Debido a que la función de hash tiende a distribuir las claves uniformemente, el acceso a los elementos es generalmente rápido. Del mismo modo, para almacenar un elemento en la tabla hash, se calcula su valor hash y se utiliza para determinar la posición en la tabla donde se almacenará.


"""

def simple_hash(value, size): # Se define una funcion en donde se utilizara el algoritmo hash simple que devuelve un índice basado en el valor de entrada
    return value % size

def hash_sort(array): # Definimos la función de ordenamiento utilizando hashing (bucket sort)
    hash_buckets = {} # Creamos un diccionario vacío para almacenar los buckets
    for num in array: # Recorremos cada elemento del arreglo
        hash_value = simple_hash(num, len(array)) # Obtenemos el hash del elemento
        if hash_value not in hash_buckets: # Si el hash no está en el diccionario, creamos una lista vacía en esa posicion
            hash_buckets[hash_value] = []
        hash_buckets[hash_value].append(num) # Añadimos el elemento al bucket correspondiente
    sorted_array = [] # Creamos una lista vacía para almacenar los elementos ordenados
    
    for key in sorted(hash_buckets.keys()):   # Recorremos cada bucket en orden y ordenamos los elementos dentro de cada bucket 
        hash_buckets[key].sort() # Ordenamos los elementos dentro del bucket 
        sorted_array.extend(hash_buckets[key]) # Añadimos los elementos ordenados del bucket al arreglo ordenado
    return sorted_array  # Devolvemos el arreglo ordenado

if __name__ == "__main__":
    
    unsorted_array = [7, 9, 5, 2, 3, 4, 9, 1, 5, 6, 2, 8, 3, 10, 10, 11, 12, 10] # Arreglo desordenado
    sorted_array = hash_sort(unsorted_array) # Ordenamos el arreglo utilizando hash_sort
    print("Tu arreglo ordenado es el siguiente:", sorted_array) # Imprimimos el arreglo ordenado
