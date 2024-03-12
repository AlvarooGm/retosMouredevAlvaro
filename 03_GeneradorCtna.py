'''
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

'''
import random as rd


todos_los_caracteres = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>?/")
sin_letras_mayusculas = list("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>?/")
sin_numeros = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[]{}|;:'\",.<>?/")
sin_simbolos = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
sin_mayusculas_numeros_simbolos = list("abcdefghijklmnopqrstuvwxyz")


salir = True
passwd=''
while salir:
    try:
        longitud_cadena = int(input('De que longitud quieres la contraseña entre 8-16: '))
        if longitud_cadena>=8 and longitud_cadena<=16:
            salir = False
    except Exception as e:
        print(e)


simb = True
num = True
may=True   


preg_may=input('¿Quieres mayusculuas?Si/No: ').lower()
if preg_may == 'no':
    may=False

preg_num=input('¿Quieres numeros?Si/No: ').lower()
if preg_num == 'no':
    num=False
                  
preg_simb=input('¿Quieres simbolos?Si/No: ').lower()
if preg_simb == 'no':
    simb=False
            
passwd=''
if simb and num and may :
    for a in range(longitud_cadena):
        car = rd.randint(0,len(todos_los_caracteres))
        passwd+=todos_los_caracteres[car]
elif simb  and  num and may==False:
    for a in range(longitud_cadena):
        car = rd.randint(0,len(sin_letras_mayusculas))
        passwd+=sin_letras_mayusculas[car] 
elif simb  and  num==False and may:
    for a in range(longitud_cadena):
        car = rd.randint(0,len(sin_numeros))
        passwd+=sin_numeros[car]  
elif simb==False  and  num and may:
    for a in range(longitud_cadena):
        car = rd.randint(0,len(sin_simbolos))
        passwd+=sin_simbolos[car]   
else:
    for a in range(longitud_cadena):
        car = rd.randint(0,len(sin_mayusculas_numeros_simbolos))
        passwd+=sin_mayusculas_numeros_simbolos[car]  



print(passwd)                                   