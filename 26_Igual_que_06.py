'''

/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
 *   o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
 */


'''

import random as rn

resultados_posibles = [('R', 'P'), ('R', 'S'), ('P', 'R'), ('P', 'S'), ('S', 'R'), ('S', 'P'), ('R', 'R'), ('P', 'P'), ('S', 'S')]

p1 = [('R', 'S'),('P', 'R'),('S', 'P')]
p2 = [('R', 'P'),('P', 'S'),('S', 'R')]



jugada = rn.randint(0,len(resultados_posibles)-1)

if resultados_posibles[jugada] in p1:
    print(resultados_posibles[jugada])
    print('Ganador Player 1')
elif resultados_posibles[jugada] in p2:
    print(resultados_posibles[jugada])
    print('Ganador Player 2')    
else:
    print(resultados_posibles[jugada])
    print('Empate')    