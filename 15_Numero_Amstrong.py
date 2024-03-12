'''

/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
 */

'''

def numero_armstrong(num):
    n = len(str(num))
    res=0
    for a in str(num):
        res+=int(a)**n

    if res == num:
        return True
    else:
        return False


print(numero_armstrong(548834))        