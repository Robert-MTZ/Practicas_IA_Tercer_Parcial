# Practica02_014_Polyphase_sort
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

"""

El Polyphase Sort se basa en el concepto de dividir el conjunto de datos en múltiples fases o etapas de ordenación, donde cada fase utiliza una cantidad limitada de memoria principal.
Durante cada fase, se leen bloques de datos desde el medio de almacenamiento externo, se ordenan en la memoria principal y luego se escriben de vuelta al medio de almacenamiento.
Este proceso se repite hasta que todos los datos estén completamente ordenados.

Funcionamiento:

División inicial: El conjunto de datos se divide en bloques más pequeños, que son suficientemente pequeños para caber en la memoria principal.

Ordenación inicial: Durante la primera fase, se leen varios bloques de datos desde el medio de almacenamiento externo y se ordenan en la memoria principal utilizando un algoritmo de ordenación eficiente, como QuickSort o MergeSort.

Escritura en el medio de almacenamiento: Después de que se haya ordenado un bloque de datos en la memoria principal, se escribe de vuelta al medio de almacenamiento externo.

Fusión y reescritura: Durante las siguientes fases, se leen bloques de datos de los medios de almacenamiento externo, se fusionan con los bloques de datos previamente ordenados en la memoria principal y luego se escriben de vuelta al medio de almacenamiento externo. Este proceso de fusión y reescritura continúa hasta que todos los bloques de datos estén completamente ordenados.

"""

def merge(arr, left, mid, right): #  Función para fusionar dos subarreglos ordenados

    n1 = mid - left + 1
    n2 = right - mid

    # Crear subarreglos temporales
    L = [0] * n1
    R = [0] * n2

    # Copiar datos a los subarreglos temporales L[] y R[]
    for i in range(0, n1):
        L[i] = arr[left + i]
    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]

    # Fusionar los subarreglos temporales de vuelta en arr[left..right]
    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copiar los elementos restantes de L[], si los hay
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copiar los elementos restantes de R[], si los hay
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def polyphase_sort(arr):# Función principal para ordenar utilizando Polyphase sort

    n = len(arr)

    # Tamaño del bloque
    size = 1

    # Hasta que el tamaño del bloque sea menor que la longitud del arreglo
    while size < n:

        left = 0

        # Hacer fusiones de subarreglos de tamaño size
        while left < n - 1:

            # Encontrar el medio y el derecho del subarreglo
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)

            # Fusionar subarreglos arr[left...mid] y arr[mid+1...right]
            merge(arr, left, mid, right)

            # Mover al siguiente subarreglo
            left += 2 * size

        # Duplicar el tamaño del bloque
        size = 2 * size

if __name__ == "__main__":
    arr = [173, 65, 34, 75, 34, 23, 89, 103, 546, 1, 234, 1028]
    print("Tu arreglo original es:") # Se imprime el mensaje
    print(arr) # Se imprime el arreglo

    polyphase_sort(arr)

    print("\n Tu arreglo ordenado es el siguiente:") # Se imprime el mensaje
    print(arr) # Se imprime el arreglo ordenado
