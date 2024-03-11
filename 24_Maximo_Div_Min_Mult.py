'''

/*
 * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
 * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */

'''
def maximo_divisor(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return abs(n1)

resultado = maximo_divisor(10, 5)
print(resultado)


def min_comun_multi(n1,n2):
    res = (n1*n2)/maximo_divisor(n1,n2)
    return res

mcm=min_comun_multi(10,5)
print(mcm)