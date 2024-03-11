'''

/*
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 */

'''


def palindromo(palabra):
    res = palabra.replace(' ','').lower()
    reves = res[::-1]
    print(res)
    print(reves)
    if res == reves:
        return True
    else:
        return False
    








    
palabra = input()

if palindromo(palabra):
    print('SI')
else:
    print('NO')    
