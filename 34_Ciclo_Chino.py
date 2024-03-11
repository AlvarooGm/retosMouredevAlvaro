'''

/*
 * Crea un función, que dado un año, indique el elemento 
 * y animal correspondiente en el ciclo sexagenario del zodíaco chino.
 * - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.html
 * - El ciclo sexagenario se corresponde con la combinación de los elementos
 *   madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
 *   conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
 *   (en este orden).
 * - Cada elemento se repite dos años seguidos.
 * - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
 */

'''

elementos = ['madera', 'fuego', 'tierra', 'metal', 'agua']
diccionario_animales = {0: 'rata', 1: 'buey', 2: 'tigre', 3: 'conejo', 4: 'dragón', 5: 'serpiente', 6: 'caballo', 7: 'oveja', 8: 'mono', 9: 'gallo', 10: 'perro', 11: 'cerdo'}



cntA = 0
cntE = 0

anio = 1997

for a in range(1984,anio):

    if cntA >11 :
        cntA = 0
    if cntE >= 10:
        cntE =0
    cntA+=1
    cntE+=1

if cntE == 0 or cntE == 1:
        print(f'El año {anio} es : madera,{diccionario_animales[cntA]}')
if cntE == 2 or cntE == 3:
        print(f'El año {anio} es : fuego,{diccionario_animales[cntA]}')     
if cntE == 4 or cntE == 5:
        print(f'El año {anio} es : tierra,{diccionario_animales[cntA]}')  
if cntE == 6 or cntE == 7:
        print(f'El año {anio} es : metal,{diccionario_animales[cntA]}')                
if cntE == 8 or cntE == 9:
        print(f'El año {anio} es : agua,{diccionario_animales[cntA]}')                  
    
