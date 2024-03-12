'''

/*
 * Crea una función que retorne el número total de bumeranes de
 * un array de números enteros e imprima cada uno de ellos.
 * - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números
 *   seguidos, en el que el primero y el último son iguales, y el segundo
 *   es diferente. Por ejemplo [2, 1, 2].
 * - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2]
 *   y [4, 2, 4]).
 */

'''

arrayLargo = [2, 1, 2, 3, 3, 4, 2, 4,6,7,6] 
arraRet = []

pos = 0
posSig = pos+2

while pos != len(arrayLargo):
    posSig = pos+2
    if posSig>len(arrayLargo):
        break
    if arrayLargo[pos] == arrayLargo[posSig]:
        arraRet.append(arrayLargo[pos])
        arraRet.append(arrayLargo[pos+1])
        arraRet.append(arrayLargo[posSig])
        pos=posSig+1
    else:
        pos+=1


print(arraRet)            

