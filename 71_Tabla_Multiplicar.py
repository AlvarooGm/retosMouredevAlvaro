'''

/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ...
 */

'''


def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

try:
    # Solicitar al usuario un número
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    
    # Imprimir la tabla de multiplicar del número ingresado
    print(f"Tabla de multiplicar del número {numero}:")
    tabla_multiplicar(numero)

except ValueError:
    print("Error: Por favor, ingrese un número válido.")
