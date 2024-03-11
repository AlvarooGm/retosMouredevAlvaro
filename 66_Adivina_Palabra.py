'''

/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
 *   ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */

'''
import random as rn
palabra = 'mouredev'
letras_adivinar = []
for i in range(3):
    letra_quitada = rn.randint(0,len(palabra)-1)
    if palabra[letra_quitada]!='_':
        letras_adivinar.append(palabra[letra_quitada])
    palabra = palabra.replace(palabra[letra_quitada],'_')
    palabra_adivinar = palabra


print(palabra_adivinar)    

vidas = 3
cnt = 0
print(len(letras_adivinar))
while vidas != 0 and cnt != len(letras_adivinar):
    letra_preg = input('Que letra falta? ')

    if letra_preg  in letras_adivinar:
        print('Muy bien es una de esas')
        cnt+=1
        
    else:
        vidas -= 1
        print(f'Una vida menos te quedan {vidas}')    

if cnt == len(letras_adivinar):
    print('Enhorabuena has ganado') 
else:
    print('Lo siento has perdido')    