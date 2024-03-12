'''

/*
 * Crea un función que reciba un texto y retorne la vocal que
 * más veces se repita.
 * - Ten cuidado con algunos casos especiales.
 * - Si no hay vocales podrá devolver vacío.
 */

'''

palabra = 'hola caracola amarilla'
vocal = ''
num = 0

if palabra.count('a') > palabra.count('e') and palabra.count('a') > palabra.count('i') and palabra.count('a') > palabra.count('o') and palabra.count('a') > palabra.count('u') :
    vocal = 'a' 
    num = palabra.count('a')
elif  palabra.count('e') > palabra.count('a') and palabra.count('e') > palabra.count('i') and palabra.count('e') > palabra.count('o') and palabra.count('e') > palabra.count('u') :
    vocal = 'e'   
    num = palabra.count('e')
elif palabra.count('i') > palabra.count('a') and palabra.count('i') > palabra.count('e') and palabra.count('i') > palabra.count('o') and palabra.count('i') > palabra.count('u') :
    vocal = 'i' 
    num = palabra.count('i')   
elif palabra.count('o') > palabra.count('a') and palabra.count('o') > palabra.count('e') and palabra.count('o') > palabra.count('i') and palabra.count('o') > palabra.count('u') :
    vocal = 'o' 
    num = palabra.count('o')
else:
    vocal = 'u'          
    num = palabra.count('u')



print(f'La vocal mas repetida es ({vocal}) con un total de {num} veces')
