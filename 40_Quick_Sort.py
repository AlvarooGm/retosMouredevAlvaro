'''

/*
 * Implementa uno de los algoritmos de ordenación más famosos:
 * el "Quick Sort", creado por C.A.R. Hoare.
 * - Entender el funcionamiento de los algoritmos más utilizados de la historia
 *   Nos ayuda a mejorar nuestro conocimiento sobre ingeniería de software.
 *   Dedícale tiempo a entenderlo, no únicamente a copiar su implementación.
 * - Esta es una nueva serie de retos llamada "TOP ALGORITMOS",
 *   donde trabajaremos y entenderemos los más famosos de la historia.
 */

'''


# Define la función quick_sort que toma una lista como entrada y devuelve la lista ordenada.
def quick_sort(arr):
    # Comprueba si la longitud de la lista es menor o igual a 1, en cuyo caso la lista ya está ordenada y se devuelve tal cual.
    if len(arr) <= 1:
        return arr
    else:
        # Establece el primer elemento de la lista como el pivote.
        pivot = arr[0]
        # Crea una lista de elementos menores o iguales al pivote, excluyendo el propio pivote.
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        # Crea una lista de elementos mayores que el pivote, excluyendo el propio pivote.
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        # Aplica recursivamente quick_sort a las sublistas de elementos menores o iguales y mayores que el pivote, y luego concatena las sublistas ordenadas junto con el pivote en el medio.
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Ejemplo de uso:
# Define una lista desordenada.
arr = [3, 6, 8, 10, 1, 2, 1]
# Ordena la lista utilizando quick_sort.
sorted_arr = quick_sort(arr)
# Imprime la lista ordenada.
print("Array ordenado:", sorted_arr)
