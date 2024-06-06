# Practica02_005_SelectionSort
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

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
