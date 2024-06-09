# Practica02_011_Straight_merging
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

"""

El término "Straight Merging" se refiere a un algoritmo de clasificación (ordenación) que combina dos listas ordenadas en una sola lista ordenada.

Funcionamiento:

Se tienen dos listas ordenadas, digamos lista1 y lista2.
Se inicializan dos índices, uno para cada lista: i para lista1 y j para lista2, ambos en 0.
Se comparan los elementos en las posiciones i y j de lista1 y lista2 respectivamente.
El elemento más pequeño entre lista1[i] y lista2[j] se agrega a la lista fusionada.
El índice correspondiente (i o j) se incrementa para la lista de la que se tomó el elemento.
Se repiten los pasos 3 a 5 hasta que se recorran todos los elementos de ambas listas.
Si alguna lista tiene elementos restantes después de la fusión de los elementos comunes, se agregan todos esos elementos a la lista fusionada.

"""

def straight_merging(list1, list2): # Definición de la función straight_merging que toma dos listas ordenadas como entrada
    merged_list = [] # Lista vacia fusionada 
    
    i = 0 # Indice inicializado
    j = 0 # Indice inicializado

    while i < len(list1) and j < len(list2): # Bucle principal que se ejecuta mientras no se haya recorrido toda ninguna de las dos listas
        if list1[i] < list2[j]:  # Comparación de los elementos en las posiciones i y j de list1 y list2
            merged_list.append(list1[i])  # Si el elemento en list1 es menor, se agrega a la lista fusionada y se incrementa el índice de list1
            i += 1
        else:
            merged_list.append(list2[j])  # Si el elemento en list2 es menor o igual, se agrega a la lista fusionada y se incrementa el índice de list2
            j += 1

    # Agregar los elementos restantes de list1 (si hay alguno)
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Agregar los elementos restantes de list2 (si hay alguno)
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list # Retorna la lista ya ordenada 

lista1 = [100, 340, 560, 356, 987, 900]
lista2 = [130, 456, 234, 345, 700, 901]

resultado = straight_merging(lista1, lista2)# Llamar a la función straight_merging con las dos listas como argumentos y almacenar el resultado
print("Lista fusionada ordenada:", resultado) # Imprimir la lista fusionada ordenada


