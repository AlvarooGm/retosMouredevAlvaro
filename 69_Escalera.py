'''
*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 *
 * Ejemplo: 4
 *         _
 *       _|
 *     _|
 *   _|
 * _|
 *
 */


'''
def dibujar_escalera(numero_escalones):
    if numero_escalones > 0:
        for i in range(numero_escalones, 0, -1):
            print(" " * (i-1) + "_" + "|")
    elif numero_escalones < 0:
        for i in range(abs(numero_escalones)):
            print(" " * i + "_" + "|")
    else:
        print("__")

# Ejemplo de uso:
numero_escalones = 4
dibujar_escalera(numero_escalones)
