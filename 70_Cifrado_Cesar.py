'''


/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */


'''

def cifrar_cesar(texto, clave):
    texto_cifrado = ""
    for caracter in texto:
        # Comprobar si el caracter es una letra del alfabeto
        if caracter.isalpha():
            # Obtener el código ASCII del caracter
            codigo = ord(caracter)
            # Aplicar el cifrado César
            if caracter.islower():
                texto_cifrado += chr((codigo - 97 + clave) % 26 + 97)
            else:
                texto_cifrado += chr((codigo - 65 + clave) % 26 + 65)
        else:
            # Mantener los caracteres que no son letras del alfabeto
            texto_cifrado += caracter
    return texto_cifrado

def descifrar_cesar(texto_cifrado, clave):
    return cifrar_cesar(texto_cifrado, -clave)

# Ejemplo de uso:
texto_original = "Hola Mundo!"
clave = 3

texto_cifrado = cifrar_cesar(texto_original, clave)
print("Texto cifrado:", texto_cifrado)

texto_descifrado = descifrar_cesar(texto_cifrado, clave)
print("Texto descifrado:", texto_descifrado)
