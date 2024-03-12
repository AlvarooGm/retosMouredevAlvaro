'''

/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */

'''

def decimal_a_binario(decimal):
    if decimal < 0:
        return "No se admite la conversión de números negativos"
    elif decimal == 0:
        return "0b0"
    else:
        binario = ""
        while decimal > 0:
            residuo = decimal % 2
            binario = str(residuo) + binario
            decimal = decimal // 2
        return "0b" + binario

# Ejemplo de uso
numero_decimal = int(input("Ingresa un número decimal: "))
resultado_binario = decimal_a_binario(numero_decimal)
print(f"El número binario equivalente es: {resultado_binario}")