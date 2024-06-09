# Practica02_009_MergeSort
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

"""

El Merge Sort es un algoritmo de ordenamiento eficiente y estable que sigue el paradigma "divide y vencerás". Fue desarrollado por John von Neumann en 1945 y es ampliamente utilizado
en la práctica debido a su eficiencia y facilidad de implementación.

Funcionamiento:

Dividir: La lista no ordenada se divide en dos sublistas de aproximadamente la misma longitud. Este proceso se repite recursivamente hasta que cada sublista contenga un solo elemento, lo que se considera trivialmente ordenado.
Conquistar: Luego, las sublistas ordenadas se combinan en una sola lista ordenada. Esto se hace comparando los elementos de las dos sublistas y colocando el elemento más pequeño (o más grande, dependiendo del orden deseado) en la lista resultante. Este proceso de combinación se realiza de manera recursiva hasta que se haya combinado toda la lista.

"""


def merge_sort(arr): # Función para ordenar la lista usando Merge Sort

    if len(arr) > 1:  # Verifica si la lista tiene más de un elemento
        mid = len(arr) // 2  # Encuentra el punto medio de la lista
        left_half = arr[:mid]  # Divide la lista en dos mitades
        right_half = arr[mid:]

        merge_sort(left_half)  # Llama recursivamente a merge_sort() para ordenar la mitad izquierda
        merge_sort(right_half)  # Llama recursivamente a merge_sort() para ordenar la mitad derecha

        i = j = k = 0  # Inicializa los índices para recorrer las dos mitades y la lista original

        # Combina las dos mitades ordenadas en la lista original
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verifica si quedan elementos sin agregar de la mitad izquierda
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Verifica si quedan elementos sin agregar de la mitad derecha
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [173, 65, 34, 75, 34, 23, 89, 103, 546, 1, 234, 1028]
print("Esta es tu lista original:", arr) # Se imprime la lista original
merge_sort(arr)
print("Esta es tu lista ordenada:", arr) # Se imprime la lista ya ordenada


