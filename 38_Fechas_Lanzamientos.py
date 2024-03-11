'''

/*
 * ¡Han anunciado un nuevo "The Legend of Zelda"!
 * Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
 * Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos
 * "The Legend of Zelda" de la historia?
 * Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda
 * que tú selecciones.
 * - Debes buscar cada uno de los títulos y su día de lanzamiento 
 *   (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)
 */

'''

from datetime import datetime as date

string_fecha1 = ('12/05/2023')
string_fecha2 = ('11/03/1983')


def dias_diferencia(string_fecha1,string_fecha2):
    fecha_1 = date.strptime(string_fecha1,"%d/%m/%Y")
    fecha_2= date.strptime(string_fecha2,"%d/%m/%Y")

    res = abs((fecha_1-fecha_2).days)
    return res


print(dias_diferencia(string_fecha1,string_fecha2))
