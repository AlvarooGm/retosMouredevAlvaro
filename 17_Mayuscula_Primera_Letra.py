'''

/*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */

'''

string_pal = 'hola que tal'

def capitaliza_primera (string_pal):
    pal_splited = string_pal.split()
    nueva_pal = ''
    for pal in pal_splited:
        nueva_pal +=  pal[0].upper()+pal[1:]+' '
    return nueva_pal


print(capitaliza_primera(string_pal))