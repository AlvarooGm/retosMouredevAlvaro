'''

/*
 * Crea un programa se encargue de transformar un número binario
 * a decimal sin utilizar funciones propias del lenguaje que
 * lo hagan directamente.
 */

'''

potencia = [0,1,2,3,4,5,6,7,8]
num = 1101
longitud = len(str(num))
numero_invertido = str(num)[::-1]
pos = 0
num_dec = 0
for a in numero_invertido:
    
    if numero_invertido[pos] == '1':
        num_dec+=2**potencia[pos]
    pos+=1    

print(num_dec)