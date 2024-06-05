# Practica02_001_InsertionSort
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

def insertion_sort(List): # Se implementa la funcion que contiene el algoritmo de ordenamiento insertion sort y se le adjudica una lista la cual sera la que modificaremos

    for i in range(1, len(List)): # Iteramos sobre todos los elementos de la lista
        current_value = List[i] # Guardamos el valor actual para su posterior insercion
        position = i # Guardamos la posición actual para comparación

        while position > 0 and List[position - 1] > current_value: # Movemos los elementos mayores que el valor actual una posición hacia adelante
            List[position] = List[position - 1]
            position -= 1  # para abrir espacio para el valor actual

        List[position] = current_value  # Insertamos el valor actual en la posición correcta

    return List # retornamos la Lista ordenada 

if __name__ == "__main__":
   
    unsorted_list = [173, 65, 34, 75, 34, 23, 89, 103, 546, 1, 234, 1028] # Lista desordenada
    print("Esta es tu lista desordenada:", unsorted_list) # Imprimimos el resultado

    sorted_list = insertion_sort(unsorted_list)  # Llamamos a la función para ordenar la lista
    print("Esta es tu lista ordenada:", sorted_list) # Imprimimos el resultado
