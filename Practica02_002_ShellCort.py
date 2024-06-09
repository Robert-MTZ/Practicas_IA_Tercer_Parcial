# Practica02_002_ShellSort
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

"""

El algoritmo de ordenamiento Shell Sort es un método de clasificación que se basa en la técnica de inserción, pero mejora su eficiencia al reducir el número de intercambios necesarios.
Funciona dividiendo la lista en sublistas más pequeñas y luego ordenándolas de forma independiente utilizando el método de inserción estándar. La diferencia clave con el método de
inserción es que el Shell Sort no ordena las sublistas por completo en cada paso, sino que solo intercambia elementos que están a una distancia fija entre sí.
Esta distancia se va reduciendo gradualmente en cada iteración hasta que llega a ser 1, momento en el que el algoritmo se comporta como una versión mejorada del método de inserción estándar.

Funcionamiento:
Se elige un "intervalo" inicial, que determina la distancia entre los elementos que se compararán y, si es necesario, intercambiarán. Este intervalo puede ser determinado de diferentes maneras, como utilizar la secuencia de intervalos de Shell, que es una secuencia predefinida de números.
Se compara y, si es necesario, se intercambian los elementos que están separados por el intervalo elegido.
Se repite este proceso para todas las sublistas formadas por el intervalo dado.
Se reduce el intervalo y se repiten los pasos 2 y 3 hasta que el intervalo sea 1, momento en el que se realiza una última pasada con el método de inserción estándar.

"""

def shell_sort(List): # creamos la funcion que implementa el algoritmo de ordenamiento shell sort y se le adjudica una lista en la cual se guardaran los valores

    interval = len(List) // 2 # Calculamos el intervalo inicial, la mitad de la longitud de la lista

    while interval > 0: # Mientras el intervalo sea mayor que 0
        for i in range(interval, len(List)): # Iteramos sobre los elementos de la lista comenzando desde el intervalo
            current_value = List[i]  # Guardamos el valor actual y su posicion
            position = i

            while position >= interval and List[position - interval] > current_value: # Insertamos el elemento en su posición correcta dentro del subarreglo
                List[position] = List[position - interval]
                position -= interval

            List[position] = current_value

        interval //= 2 # Reducimos el intervalo

    return List # regresa la lista ya ordenada

if __name__ == "__main__":
    
    unsorted_list = [173, 65, 34, 75, 34, 23, 89, 103, 546, 1, 234, 1028] # Lista desordenada la mandamos llamar
    print("Esta es tu lista desordenada:", unsorted_list) # Imprimimos la lista desordenada

    sorted_list = shell_sort(unsorted_list) # Lista ordenada la mandamos llamar 
    print("Esta es tu lista ordenada:", sorted_list) # Imprimimos la lista ordenada
