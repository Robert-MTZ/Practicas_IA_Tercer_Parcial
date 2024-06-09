# Practica02_012_Natural_merging
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

"""

Natural Merging Sort es un algoritmo de ordenación que explota las subsecuencias ya ordenadas dentro de la lista que se está ordenando

Funcionamiento:

Identificación de subsecuencias ordenadas: En primer lugar, se identifican las subsecuencias ordenadas dentro de la lista. Estas subsecuencias pueden ser de cualquier tamaño y no necesariamente contiguas.
Fusión de subsecuencias: Luego, se fusionan estas subsecuencias ordenadas en sublistas más grandes, combinando gradualmente sublistas adyacentes hasta que toda la lista esté ordenada.
Iteración: Este proceso de fusión se repite hasta que solo queda una sublista, que será la lista ordenada final.

"""

def natural_merging_sort(arr):
    # Función para dividir la lista en sublistas ordenadas
    def find_sublists(arr):
        sublists = []
        sublist = [arr[0]]  # Comenzamos con el primer elemento en una sublista

        for i in range(1, len(arr)):
            # Si el elemento actual es mayor o igual al anterior, lo agregamos a la sublista actual
            if arr[i] >= arr[i-1]:
                sublist.append(arr[i])
            else:
                # Si el elemento actual es menor que el anterior, finalizamos la sublista actual
                sublists.append(sublist)
                sublist = [arr[i]]  # Iniciamos una nueva sublista con el elemento actual

        sublists.append(sublist)  # Agregamos la última sublista creada
        return sublists

    # Función para fusionar dos sublistas ordenadas
    def merge_lists(list1, list2):
        merged_list = []
        i = j = 0

        # Mientras haya elementos en ambas listas, los comparamos y los agregamos al resultado
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list2[j])
                j += 1

        # Agregamos los elementos restantes de ambas listas
        merged_list.extend(list1[i:])
        merged_list.extend(list2[j:])
        return merged_list

    # Dividimos la lista original en sublistas ordenadas
    sublists = find_sublists(arr)

    # Mientras haya más de una sublista, las fusionamos
    while len(sublists) > 1:
        new_sublists = []
        i = 0

        # Recorremos las sublistas de dos en dos, fusionándolas
        while i < len(sublists) - 1:
            merged_list = merge_lists(sublists[i], sublists[i + 1])
            new_sublists.append(merged_list)
            i += 2

        # Si queda una sublista sin fusionar, la agregamos sin cambios
        if i == len(sublists) - 1:
            new_sublists.append(sublists[i])

        sublists = new_sublists

    # La lista final ordenada será la única sublista restante
    return sublists[0]

arr = [134, 29, 7, 23, 54, 123, 543, 789] # Lista desordenada
sorted_arr = natural_merging_sort(arr)
print("Esta es tu lista ordenada:", sorted_arr) # Se imprime la lista ordenada
