'''

/*
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se
 *   lanzará una excepción.
 */

'''
from datetime import datetime as date

string_fecha1 = ('08/01/2024')
string_fecha2 = ('11/03/1983')


def dias_diferencia(string_fecha1,string_fecha2):
    fecha_1 = date.strptime(string_fecha1,"%d/%m/%Y")
    fecha_2= date.strptime(string_fecha2,"%d/%m/%Y")

    res = abs((fecha_1-fecha_2).days)
    return res


print(dias_diferencia(string_fecha1,string_fecha2))


