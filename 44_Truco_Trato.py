'''

/*
 * Este es un reto especial por Halloween.
 * Deberemos crear un programa al que le indiquemos si queremos realizar "Truco
 * o Trato" y un listado (array) de personas con las siguientes propiedades:
 * - Nombre de la niña o niño
 * - Edad
 * - Altura en centímetros
 *
 * Si las personas han pedido truco, el programa retornará sustos (aleatorios)
 * siguiendo estos criterios:
 * - Un susto por cada 2 letras del nombre por persona
 * - Dos sustos por cada edad que sea un número par
 * - Tres sustos por cada 100 cm de altura entre todas las personas
 * - Sustos: 🎃 👻 💀 🕷 🕸 🦇
 *
 * Si las personas han pedido trato, el programa retornará dulces (aleatorios)
 * siguiendo estos criterios:
 * - Un dulce por cada letra de nombre
 * - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
 * - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
 * - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
 * - En caso contrario retornará un error.
 */


'''
import random  # Importamos el módulo random para generar números aleatorios

class Persona:  # Definimos la clase Persona
    def __init__(self, nombre, edad, altura):  # Definimos el constructor de la clase Persona
        self.nombre = nombre  # Asignamos el nombre de la persona al atributo 'nombre'
        self.edad = edad  # Asignamos la edad de la persona al atributo 'edad'
        self.altura = altura  # Asignamos la altura de la persona al atributo 'altura'

def truco_o_trato(pedido, personas):  # Definimos la función truco_o_trato que recibe el pedido y la lista de personas
    sustos = ['🎃', '👻', '💀', '🕷', '🕸', '🦇']  # Lista de sustos disponibles
    dulces = ['🍰', '🍬', '🍡', '🍭', '🍪', '🍫', '🧁', '🍩']  # Lista de dulces disponibles
    
    if pedido == 'truco':  # Si el pedido es 'truco'
        sustos_generados = []  # Inicializamos una lista vacía para almacenar los sustos generados
        for persona in personas:  # Iteramos sobre cada persona en la lista de personas
            sustos_generados.extend([random.choice(sustos) for _ in range(len(persona.nombre)//2)])  # Generamos sustos basados en la longitud del nombre de la persona
            if persona.edad % 2 == 0:  # Si la edad de la persona es par
                sustos_generados.extend([random.choice(sustos) for _ in range(2)])  # Generamos más sustos
        sustos_generados.extend([random.choice(sustos) for _ in range(sum([persona.altura//100 for persona in personas])*3)])  # Generamos sustos adicionales basados en la altura total de las personas
        return sustos_generados  # Devolvemos la lista de sustos generados
    elif pedido == 'trato':  # Si el pedido es 'trato'
        dulces_generados = []  # Inicializamos una lista vacía para almacenar los dulces generados
        for persona in personas:  # Iteramos sobre cada persona en la lista de personas
            dulces_generados.extend([random.choice(dulces) for _ in range(len(persona.nombre))])  # Generamos dulces basados en la longitud del nombre de la persona
            dulces_generados.extend([random.choice(dulces) for _ in range(min(persona.edad//3, 10))])  # Generamos más dulces basados en la edad de la persona, con un máximo de 10 dulces
            dulces_generados.extend([random.choice(dulces) for _ in range(min(persona.altura//50, 3)*2)])  # Generamos dulces adicionales basados en la altura de la persona, con un máximo de 150 cm
        return dulces_generados  # Devolvemos la lista de dulces generados
    else:  # Si el pedido no es válido
        return "Error: Pedido no válido"  # Devolvemos un mensaje de error

# Ejemplo de uso:
personas = [  # Creamos una lista de personas
    Persona('Ana', 8, 120),  # Creamos una instancia de Persona con nombre 'Ana', edad 8 y altura 120 cm
    Persona('Pedro', 10, 140),  # Creamos una instancia de Persona con nombre 'Pedro', edad 10 y altura 140 cm
    Persona('María', 7, 110)  # Creamos una instancia de Persona con nombre 'María', edad 7 y altura 110 cm
]

print(truco_o_trato('truco', personas))  # Ejecutamos la función con el pedido 'truco' y la lista de personas, e imprimimos los sustos generados
print(truco_o_trato('trato', personas))  # Ejecutamos la función con el pedido 'trato' y la lista de personas, e imprimimos los dulces generados
