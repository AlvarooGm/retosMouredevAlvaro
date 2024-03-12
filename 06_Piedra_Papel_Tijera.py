'''

/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

'''
import random as rd





res=[]

cnt1=0
cnt2=0

numero_jugadas=int(input('¿Cuantas veces quieres que jueguen?'))

for a in range(numero_jugadas):
    p1 = rd.randint(0,2)
    p2 = rd.randint(0,2)
    if p1 == 0 :
        res.append("🗿")
        
        if p2 == 0:
            
            res.append("🗿")
        elif p2 == 1 :
            res.append("📄")
            cnt2+=1
        else:    
            res.append("✂️")
            cnt1+=1
    elif p1 == 1 :
        res.append("📄")
        if p2 == 0:
            res.append("🗿")
            cnt1+=1  
        elif p2 == 1 :
            res.append("📄")
        else:    
            res.append("✂️")
            cnt2+=1
    else:
        res.append("✂️")
        if p2 == 0:
            res.append("🗿")
            cnt2+=1 
        elif p2 == 1 :
            res.append("📄")
            cnt1+=1 
        else:    
            res.append("✂️")


if cnt1>cnt2:
    print('Ganador Player 1')
    print(res)
elif cnt2>cnt1:
    print('Ganador Player 2')
    print(res)
else:
    print('Empate')
    print(res)    


