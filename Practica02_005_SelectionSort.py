# Practica02_005_SelectionSort
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

"""

El Selection Sort (ordenamiento por selección) es un algoritmo de ordenamiento simple e intuitivo que funciona encontrando repetidamente el elemento más pequeño (o más grande,
dependiendo del orden deseado) de la lista no ordenada y moviéndolo al inicio de la lista ordenada. Este proceso se repite hasta que toda la lista esté ordenada.

Funcionamiento:

División en sublistas ordenada y no ordenada: Al principio, la lista se divide en dos partes: una sublista ordenada y una sublista no ordenada. La sublista ordenada está vacía inicialmente, mientras que la sublista no ordenada contiene todos los elementos de la lista.
Búsqueda del elemento mínimo: Se busca el elemento más pequeño en la sublista no ordenada. Esto se puede hacer recorriendo la sublista no ordenada y manteniendo un seguimiento del índice del elemento más pequeño encontrado.
Intercambio con el primer elemento de la sublista ordenada: Una vez que se encuentra el elemento más pequeño, se intercambia con el primer elemento de la sublista no ordenada. Esto coloca el elemento más pequeño en la posición correcta dentro de la sublista ordenada, y ahora forma parte de la sublista ordenada.
Repetición: Se repiten los pasos 2 y 3 hasta que toda la lista esté ordenada. En cada iteración, la sublista ordenada crece en un elemento, mientras que la sublista no ordenada se reduce en un elemento.
Finalización: Una vez que todos los elementos están en la sublista ordenada, la lista completa estará ordenada.

"""

def selection_sort(arr): # Implementación del algoritmo de ordenamiento Selection Sort.

    # Iteramos sobre todos los elementos del arreglo
    for i in range(len(arr)):
        
        # Encontramos el índice del elemento más pequeño en el subarreglo no ordenado
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # Intercambiamos el elemento actual con el elemento más pequeño encontrado
    
    return arr # Retornamos con la lista ordenada

if __name__ == "__main__":
    
    unsorted_array = [173, 65, 34, 75, 34, 23, 89, 103, 546, 1, 234, 1028] # insertamos el arreglo desordenado
    sorted_array = selection_sort(unsorted_array)  # Ordenamos el arreglo utilizando Selection Sort
    print("Tu arreglo ordenado es el siguiente:", sorted_array) # Imprimimos el arreglo ordenado
