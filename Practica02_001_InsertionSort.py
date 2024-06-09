# Practica02_001_InsertionSort
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

"""
El algoritmo de ordenamiento por inserción (Insertion Sort) es un algoritmo sencillo y eficiente para ordenar una lista de elementos. Funciona de manera similar a cómo ordenarías
cartas en tus manos: tomas una carta de la mano no ordenada e insertas (colocas) en la posición correcta en la mano ordenada.

Funcionamiento:

División en sublista ordenada y sublista no ordenada: Al inicio, se considera que la lista está dividida en dos partes: una sublista ordenada y una sublista no ordenada. Inicialmente, la sublista ordenada está vacía y la sublista no ordenada contiene todos los elementos de la lista.
Iteración sobre la sublista no ordenada: Se toma un elemento de la sublista no ordenada y se compara con los elementos de la sublista ordenada, comenzando desde el final de la sublista ordenada y retrocediendo hacia el principio.
Inserción en la posición correcta: Se encuentra la posición correcta para insertar el elemento seleccionado en la sublista ordenada. Esto implica desplazar los elementos mayores que el elemento seleccionado una posición hacia la derecha.
Repetición: Se repiten los pasos 2 y 3 hasta que todos los elementos de la sublista no ordenada hayan sido procesados. Al finalizar este proceso, la lista estará completamente ordenada.

"""

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
