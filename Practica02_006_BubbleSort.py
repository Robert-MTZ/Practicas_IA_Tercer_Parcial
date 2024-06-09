# Practica02_006_BubbleSort
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

"""

El Bubble Sort (ordenamiento de burbuja) es un algoritmo de ordenamiento simple que funciona comparando repetidamente pares de elementos adyacentes y los intercambia si están
en el orden incorrecto. El proceso se repite varias veces hasta que no se requieren más intercambios, lo que indica que la lista está ordenada.

Funcionamiento:

Comparación de elementos adyacentes: El algoritmo compara cada par de elementos adyacentes en la lista. Comienza desde el primer par de elementos, luego el segundo par, y así sucesivamente, hasta llegar al último par de elementos.
Intercambio si es necesario: Si el primer elemento de un par es mayor (o menor, dependiendo del orden deseado) que el segundo elemento, se intercambian. Esto coloca los elementos más grandes hacia el final de la lista y los más pequeños hacia el principio.
Repetición de pasos 1 y 2: El proceso de comparación e intercambio se repite varias veces, pasando por la lista hasta que no se realicen más intercambios durante una pasada completa. Esto indica que la lista está ordenada.
Finalización: Una vez que no se realizan más intercambios durante una pasada completa, la lista está ordenada y el algoritmo termina.

"""

def bubble_sort(arr): # Función que ordena una lista utilizando el algoritmo Bubble Sort

    n = len(arr)  # Obtiene la longitud de la lista
    for i in range(n):  # Itera sobre todos los elementos de la lista
        # Cada iteración de este bucle coloca el elemento más grande en la posición correcta
        for j in range(0, n-i-1):
            # Compara cada par de elementos adyacentes y los intercambia si están en el orden incorrecto
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr  # Devuelve la lista ordenada

if __name__ == "__main__":
   
    unsorted_list = [173, 65, 34, 75, 34, 23, 89, 103, 546, 1, 234, 1028] # Lista desordenada
    
    print("Lista desordenada:") # escribimos el texto que queremos imprimir antes de la lista
    print(unsorted_list)# imprimimos la lista ordenada
    
    sorted_list = bubble_sort(unsorted_list) # Ordena la lista utilizando Bubble Sort
    
    print("Lista ordenada:") # escribimos el texto que queremos imprimir antes de la lista
    print(sorted_list) # imprimimos la lista ordenada


