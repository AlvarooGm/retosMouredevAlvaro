'''

/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */

'''

expresion_Eq = input('Escriba la expresion: ')


cnt_Corchetes = 0
cnt_Parentesis = 0
cnt_LLaves = 0

for a in expresion_Eq:
    if a == '{' or a == '}':
        cnt_LLaves+=1

    elif   a == '(' or a == ')':  
        cnt_Parentesis+=1

    elif   a == '[' or a == ']':      
        cnt_Corchetes+=1


if cnt_LLaves%2 == 0 and cnt_Corchetes%2 == 0 and cnt_Parentesis%2 == 0:
    print(f'La expresion {expresion_Eq} SI esta equilibrada')  
else:
    print(f'La expresion {expresion_Eq} NO esta equilibrada')           
