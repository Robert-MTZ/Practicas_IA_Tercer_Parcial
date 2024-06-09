# Practica02_007_QuickSort
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

"""


ChatGPT
El algoritmo QuickSort es un eficiente algoritmo de ordenamiento que utiliza la técnica de "divide y vencerás" para ordenar una lista de elementos. Fue desarrollado por Tony
Hoare en 1960 y es uno de los algoritmos de ordenamiento más utilizados en la práctica debido a su velocidad y eficiencia en la mayoría de los casos.

Funcionamiento:

Elección del pivote: Se elige un elemento de la lista, llamado "pivote". Este pivote puede seleccionarse de varias maneras, como tomar el primer elemento, el último elemento o algún elemento al azar. La elección del pivote influye en el rendimiento del algoritmo.
División de la lista: Se reorganiza la lista de manera que todos los elementos menores que el pivote estén antes que él, y todos los elementos mayores que el pivote estén después de él. Después de esta partición, el pivote se encuentra en su posición final en la lista ordenada. Este proceso se llama "partición".
Ordenación recursiva de las sublistas: Se aplica recursivamente el mismo proceso a las sublistas generadas por la partición. Es decir, se selecciona un nuevo pivote en cada sublista y se repite el proceso de partición hasta que todas las sublistas estén ordenadas.
Combinación de sublistas ordenadas: Como el algoritmo utiliza el enfoque de "divide y vencerás", no es necesario realizar ninguna operación adicional para combinar las sublistas ordenadas, ya que el ordenamiento ocurre in situ.

"""

def partition(arr, low, high): # Función de partición que selecciona un pivote y coloca todos los elementos más pequeños a su izquierda y todos los elementos más grandes a su derecha.

    pivot = arr[high]  # Tomamos el último elemento como pivote
    i = low - 1  # Índice del elemento más pequeño
    for j in range(low, high):
        # Si el elemento actual es menor o igual al pivote
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Intercambiamos el elemento actual con el elemento en el índice i
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Colocamos el pivote en su posición correcta
    return i + 1


def quicksort(arr, low, high): #  Función principal de Quicksort que ordena recursivamente la lista.
 
    if low < high:
        # Obtenemos el índice de partición
        pi = partition(arr, low, high)
        
        # Ordenamos recursivamente los elementos antes y después de la partición
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

arr = [173, 65, 34, 75, 34, 23, 89, 103, 546, 1, 234, 1028]
n = len(arr)
quicksort(arr, 0, n - 1)
print("Esta es tu lista ordenada:", arr) # Imrpimimos la lista ya ordenada
