'''

/*
 * Crea un programa que calcule el daño de un ataque durante
 * una batalla Pokémon.
 * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
 *   (buscar su efectividad)
 * - El programa recibe los siguientes parámetros:
 *  - Tipo del Pokémon atacante.
 *  - Tipo del Pokémon defensor.
 *  - Ataque: Entre 1 y 100.
 *  - Defensa: Entre 1 y 100.
 */

'''


tipo1 = input('Introduzca el tipo del Atacante (a-Agua,f-Fuego,p-Planta,e-Electrico): ')
tipo2 = input('Introduzca el tipo del Defensor (a-Agua,f-Fuego,p-Planta,e-Electrico): ')
ataque = int(input('Ingrese el  Ataque: Entre 1 y 100: '))
defensa =  int(input('Ingrese el  Defensa: Entre 1 y 100: '))


if tipo1 == 'a':
    if tipo1 == 'a':
        dano = 50 * (ataque / defensa) * 1
    elif tipo1 == 'f':    
        dano = 50 * (ataque / defensa) * 2
    elif tipo1 == 'p':    
        dano = 50 * (ataque / defensa) * 0.5
    elif tipo1 == 'e':     
        dano = 50 * (ataque / defensa) * 0.5
    else:
        print('Tipo no valido')

elif tipo1 == 'f':    
    if tipo1 == 'a':
        dano = 50 * (ataque / defensa) * 0.5
    elif tipo1 == 'f':    
        dano = 50 * (ataque / defensa) * 0.5
    elif tipo1 == 'p':    
        dano = 50 * (ataque / defensa) * 2
    elif tipo1 == 'e':     
        dano = 50 * (ataque / defensa) * 1
    else:
        print('Tipo no valido')

elif tipo1 == 'p':   
    if tipo1 == 'a':
        dano = 50 * (ataque / defensa) * 2
    elif tipo1 == 'f':    
        dano = 50 * (ataque / defensa) * 0.5
    elif tipo1 == 'p':    
        dano = 50 * (ataque / defensa) * 0.5
    elif tipo1 == 'e':     
        dano = 50 * (ataque / defensa) * 1
    else:
        print('Tipo no valido') 

elif tipo1 == 'e': 
    if tipo1 == 'a':
        dano = 50 * (ataque / defensa) * 2
    elif tipo1 == 'f':    
        dano = 50 * (ataque / defensa) * 1
    elif tipo1 == 'p':    
        dano = 50 * (ataque / defensa) * 0.5
    elif tipo1 == 'e':     
        dano = 50 * (ataque / defensa) * 0.5
    else:
        print('Tipo no valido')    


else:
    print('Tipo no valido')    



print(dano)