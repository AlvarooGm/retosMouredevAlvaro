'''

/*
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.
 */

'''
from datetime import datetime as date



string_fecha1 = ('08/01/2024')
fecha_1 = date.strptime(string_fecha1,"%d/%m/%Y")

milisegs = fecha_1.timestamp()
print(milisegs)
