# Practica02_010_RadixSort
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

"""

El Radix Sort es un algoritmo de ordenamiento no comparativo que clasifica los elementos basándose en sus dígitos individuales. Funciona ordenando los elementos en diferentes "baldes"
según el valor de un dígito específico, comenzando desde el dígito menos significativo hasta el más significativo.

Funcionamiento:

Clasificación por dígito: El algoritmo comienza clasificando los elementos basándose en el valor del dígito menos significativo. Para hacer esto, los elementos se distribuyen en baldes según el valor de este dígito.
Reagrupación: Después de clasificar los elementos en los baldes, se reagrupan en una sola lista. La lista resultante conserva el orden de los elementos según el valor de ese dígito.
Repetición: Este proceso de clasificación y reagrupación se repite para cada dígito, desde el menos significativo hasta el más significativo. Por lo tanto, después de cada iteración, los elementos estarán más ordenados según los dígitos de derecha a izquierda.
Finalización: Después de repetir el proceso para todos los dígitos, la lista estará completamente ordenada.

"""

def counting_sort(arr, exp): #  Función auxiliar que realiza el ordenamiento por conteo para un dígito específico (exp) en el Radix Sort
    
    n = len(arr)

    # Inicializa la lista de conteo y la lista de salida
    count = [0] * 10
    output = [0] * n

    # Llena la lista de conteo
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Ajusta la lista de conteo
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construye la lista de salida
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copia la lista de salida a la lista original
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr): # Función principal que implementa el algoritmo Radix Sort
  
    # Encuentra el máximo número para saber cuántos dígitos tiene
    max_num = max(arr)

    # Ejecuta counting_sort para cada dígito, comenzando por el dígito menos significativo
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

arr = [173, 65, 34, 75, 34, 23, 89, 103, 546, 1, 234, 1028]
print("Esta es tu lista original:", arr)
radix_sort(arr)
print("Esta es tu lista ordenada:", arr)
