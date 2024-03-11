'''

/*
 * Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

'''
import datetime

mes = 9
anio = 2024

def es_viernes_trece (mes , anio):

    fecha = datetime.date(anio,mes,13)

    if fecha.weekday()==4:
        return True
    else:
        return False
    

if es_viernes_trece (mes,anio):
    print('Hay un viernes 13')
else:
    print('No hay un viernes 13')



