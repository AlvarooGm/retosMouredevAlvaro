'''

/*
 * Crea una función que transforme grados Celsius en Fahrenheit
 * y viceversa.
 *
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
 *   y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
 */

Grados centígrados = (grados Fahrenheit − 32) × 5/9.
Grados Fahrenheit = (grados centígrados × 9/5) +32.

'''

gradosC=27
gradosF=15

converF = (gradosC*(9/5))+32
print(f'Los grados Fahrenheit son : {converF}')

converC = (gradosF-32)*(9/5)
print(f'Los grados Celsius son : {converC}')