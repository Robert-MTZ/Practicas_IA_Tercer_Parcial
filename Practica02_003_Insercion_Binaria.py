# Practica02_003_Insercion_Binaria
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

def binary_insertion_sort(List): # Se crea una funcion que implementara el algoritmo de ordenamiento de insercion binaria a la cual tambien se le adjudica una lista en donde se guardaran los valores 

    for i in range(1, len(List)): # Iteramos sobre todos los elementos de la lista
        current_value = List[i]  # Guardamos el valor actual para su posterior insercion

        # Inicializamos los índices para busqueda binaria
        left = 0
        right = i - 1

        # Realizamos la búsqueda binaria para encontrar la posición de inserción del valor actual
        while left <= right:
            mid = (left + right) // 2
            if List[mid] < current_value:
                left = mid + 1
            else:
                right = mid - 1

        # Desplazamos los elementos mayores que el valor actual una posición hacia adelante
        # para abrir espacio para el valor actual
        for j in range(i, left, -1):
            List[j] = List[j - 1]

        # Insertamos el valor actual en la posición correcta
        List[left] = current_value

    return List

if __name__ == "__main__":
    # Lista desordenada
    unsorted_list = [173, 65, 34, 75, 34, 23, 89, 103, 546, 1, 234, 1028] # Lista desordenada la mandamos llamar
    print("Esta es la lista desordenada:", unsorted_list) # Imprimimos la lista desordenada

    sorted_list = binary_insertion_sort(unsorted_list) # Lista ordenada la mandamos llamar 
    print("Esta es la lista ordenada:", sorted_list) # Imprimimos la lista ordenada
