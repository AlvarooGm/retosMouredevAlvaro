'''
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */

'''
import random

def crearSerie(rango):

    puntos = []
    
    for a in range(rango):
      player = random.randint(1,2)
      if player == 1:
          puntos.append('P1')   
      else:
          puntos.append('P2')       

    return puntos










def dibujarPuntos():
    player = crearSerie(4)
    print(player)
    cntA=0
    cntB=0
  
    puntos = [0,15,30,40,'ventaja','win']

    print(f'{puntos[cntA]}-{puntos[cntB]}')

    for a in player:
        
        if a == 'P1':
            cntA+=1
            print(f'{puntos[cntA]}-{puntos[cntB]}')
        else:
            cntB+=1
            print(f'{puntos[cntA]}-{puntos[cntB]}')    

   
    

    while True:
        p=crearSerie(1)
         
        if p[0] == 'P1':
            

            if cntA == 3 and cntB == 3:
                cntA+=1
                print(f'{puntos[cntA]}-{puntos[cntB]}')
                
            if cntA == 4 and cntB == 3:
                cntA+=1
                print(f'{puntos[cntA]}-{puntos[cntB]}')
                break
            elif cntA == 3 and cntB == 4: 
                cntB-=1
                print(f'{puntos[cntA]}-{puntos[cntB]}')  

            elif cntA==3:
                        cntA+=2
                        print(f'{puntos[cntA]}-{puntos[cntB]}')      
                        break
                          
            else:
                        cntA+=1
                        print(f'{puntos[cntA]}-{puntos[cntB]}')
        elif p[0] == 'P2':
            if cntA == 3 and cntB == 3:
                cntB+=1
                print(f'{puntos[cntA]}-{puntos[cntB]}')
                
            if cntB == 4 and cntA == 3:
                cntB+=1
                print(f'{puntos[cntA]}-{puntos[cntB]}')
                break
            elif cntB == 3 and cntA == 4: 
                cntA-=1
                print(f'{puntos[cntA]}-{puntos[cntB]}')  

            elif cntB==3:
                    cntB+=2
                    print(f'{puntos[cntA]}-{puntos[cntB]}')  
                    break
                            
            else:
                    cntB+=1
                    print(f'{puntos[cntA]}-{puntos[cntB]}')



          
    


dibujarPuntos()


