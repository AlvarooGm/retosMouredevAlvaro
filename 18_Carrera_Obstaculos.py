'''

/*
 * Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras
 *        "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo)
 *        o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 *        será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
 */


'''
import random as rn


def carrera():
    
    suelo_valla = ['_','|']
    nums_posibles = [0,1]
    prob = [0.7,0.3]
    bien_fin = True
    for a in range(1,50):
        print(suelo_valla[0],end='')
        eleccion_1 = rn.choices(nums_posibles,weights=prob)[0]
        eleccion_2 = rn.choices(nums_posibles,weights=prob)[0]
        
        if eleccion_1 == eleccion_2:
            print(suelo_valla[eleccion_1],end='')
        elif eleccion_1 == 1 and eleccion_2 == 0:
            print('x',end='')   
            bien_fin=False
        elif eleccion_1 == 0 and eleccion_2 == 1:
            print('/',end='')      
            bien_fin=False
    return bien_fin         


print(carrera())