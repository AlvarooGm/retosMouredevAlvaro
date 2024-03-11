'''

/*
 * Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
 */

'''
import numpy as np

ar1 = np.array([1, 0, -1])
ar2 = np.array([1, 2, 1])

if np.dot(ar1,ar2)==0:
    print('SI son ortogonales')
else:
    print('NO son ortogonales')