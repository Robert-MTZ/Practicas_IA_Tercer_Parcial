# Practica02_002_ShellCort
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

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
