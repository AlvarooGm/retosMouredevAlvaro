'''

/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */


'''

def decimal_a_octal(numero):
    resultado = ''
    while numero > 0:
        residuo = numero % 8
        resultado = str(residuo) + resultado
        numero //= 8
    return resultado

def decimal_a_hexadecimal(numero):
    hexadecimal = ''
    while numero > 0:
        residuo = numero % 16
        if residuo < 10:
            hexadecimal = str(residuo) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + residuo - 10) + hexadecimal
        numero //= 16
    return hexadecimal

# Ejemplo de uso
numero_decimal = 123
print("El número decimal", numero_decimal, "en octal es:", decimal_a_octal(numero_decimal))
print("El número decimal", numero_decimal, "en hexadecimal es:", decimal_a_hexadecimal(numero_decimal))
