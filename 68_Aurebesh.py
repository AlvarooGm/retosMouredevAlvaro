'''

/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico
 * del universo Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */



'''

diccionario_aurebesh = {
    'a': 'Aurek', 'b': 'Besh', 'c': 'Cresh', 'd': 'Dorn', 'e': 'Esk', 'f': 'Forn', 'g': 'Greesh',
    'h': 'Herf', 'i': 'Isk', 'j': 'Jenth', 'k': 'Krill', 'l': 'Leth', 'm': 'Mern', 'n': 'Nern',
    'o': 'Osk', 'p': 'Peth', 'q': 'Qek', 'r': 'Resh', 's': 'Seesh', 't': 'Trill', 'u': 'Uth',
    'v': 'Vev', 'w': 'Wowf', 'x': 'Xesh', 'y': 'Yirt', 'z': 'Zerek',
}


def traducir_aurebesh(palabra):
    palabra = palabra.lower()
    nueva_pal = ''
    for a in palabra:
        if a in diccionario_aurebesh:
            nueva_pal += diccionario_aurebesh[a]+' '
        else:
            nueva_pal+=a+' '    
    return nueva_pal.strip()


palabra = 'Hola ¿como estas?'

palabra_aure = traducir_aurebesh(palabra)
print(palabra_aure)