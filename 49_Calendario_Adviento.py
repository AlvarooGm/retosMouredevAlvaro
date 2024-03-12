'''

/*
 * ¿Conoces el calendario de adviento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software,
 * ciencia y tecnología desde el 1 de diciembre.
 *
 * Enunciado: Crea una función que reciba un objeto de tipo "Date" y retorne
 * lo siguiente:
 * - Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo
 *   de ese día (a tu elección) y cuánto queda para que finalice el sorteo de ese día.
 * - Si la fecha es anterior: Cuánto queda para que comience el calendario.
 * - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.
 *
 * Notas:
 * - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00
 *   y finaliza a las 23:59:59.
 * - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos
 *   y segundos.
 */


'''

from datetime import datetime, timedelta

def calcular_regalo_adviento(fecha):
    adviento_2022 = {
        1: "Un libro electrónico sobre Python",
        2: "Una suscripción gratuita a una plataforma de cursos en línea",
        # Aquí puedes añadir los regalos para los demás días del calendario
    }
    
    adviento_inicio = datetime(2022, 12, 1)
    adviento_fin = datetime(2022, 12, 24, 23, 59, 59)
    
    if fecha < adviento_inicio:
        tiempo_para_inicio = adviento_inicio - fecha
        return f"Faltan {tiempo_para_inicio.days} días para el inicio de aDEViento 2022."
    elif fecha <= adviento_fin:
        dia_adviento = fecha.day
        regalo = adviento_2022.get(dia_adviento, "¡Hoy no hay regalo! 😔")
        tiempo_restante = adviento_fin - fecha
        return f"¡Feliz aDEViento 2022! El regalo de hoy es: {regalo}."
    else:
        tiempo_pasado = fecha - adviento_fin
        return f"El aDEViento 2022 ha finalizado. Han pasado {tiempo_pasado.days} días desde entonces."

# Ejemplo de uso
fecha_actual = datetime(2022, 12, 5, 15, 30, 0)
print(calcular_regalo_adviento(fecha_actual))
