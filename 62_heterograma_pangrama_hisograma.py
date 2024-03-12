'''

/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

'''


def Heterograma(palabra):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    pal = palabra.lower()
    is_het = True
    for l in alfabeto:
        if l in pal:
            cnt = pal.count(l)
            if cnt > 1:
                is_het = False
                
                
        else:
            is_het = False
            
    return is_het   


def Pangrama (palabra):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    pal = palabra.lower()
    is_pan = True
    for l in alfabeto:
        if l not in pal:
            is_pan=False
            
    return is_pan



cadena1 = "El rápido zorro marrón salta sobre el perro perezoso"
cadena2 = "Pack my box with five dozen liquor jugs"
cadena3 = "The quick brown fox jumps over the lazy dog"
cadena4 = "Máximas y mínimas "

print("Es un Heterograma:", Heterograma(cadena4))
print("Es un Pangrama:", Pangrama(cadena2))

