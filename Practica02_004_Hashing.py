# Practica02_004_Hashing
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

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
