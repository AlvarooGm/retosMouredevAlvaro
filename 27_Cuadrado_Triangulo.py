'''

/*
 * Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?
 */

 
 #Cuadrado
for a in range(max_range):
    for b in range(max_range):
        print('*',end=' ')
    print('')            


'''
max_range = 5

for a in range(1, max_range + 1):
    print(' ' * (max_range - a) + '*' * a)
