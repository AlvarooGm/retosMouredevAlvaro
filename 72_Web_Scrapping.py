'''

/*
 * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 */


'''

import re

import requests

url = 'https://www.vulnhub.com'

res = requests.get(url)
content = res.text
patron = r'/entry/[\w-]*'
maquinas_repetidas = re.findall(patron,str(content))
sin_duplicados = list(set(maquinas_repetidas))

print(sin_duplicados)

maquinas_final = []

for m in sin_duplicados:    
    nombre = m.replace('/entry/' , '')
    maquinas_final.append(nombre)

print(maquinas_final)    
