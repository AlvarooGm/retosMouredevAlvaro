'''

/*
 * Crea una función que ordene y retorne una matriz de números.
 * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
 *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
 *   o de mayor a menor.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
 *   automáticamente.
 */

'''
import numpy as np

ar = np.array([2,1,4,6,3,8,5,7])
ar.sort() #Si lo quiere descendente darla la vuelta [::-1]
print(ar)