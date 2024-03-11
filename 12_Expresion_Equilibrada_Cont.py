'''

/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */

'''
def caracteres_no_comunes(str1, str2):
    # Obtiene los caracteres en str1 pero no en str2
    out1 = ''.join([char for char in str1 if char not in str2])

    # Obtiene los caracteres en str2 pero no en str1
    out2 = ''.join([char for char in str2 if char not in str1])

    return out1, out2

op1,op2 = caracteres_no_comunes('hola','adios')

print(op1)
print(op2)

