'''

/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */


'''

def obtener_valores_parametros(url):
    parametros = []
    parametro_actual = ""
    capturar_valor = False

    for caracter in url:
        if caracter == '?':
            capturar_valor = True
        elif capturar_valor:
            if caracter == '&':
                parametros.append(parametro_actual)
                parametro_actual = ""
            else:
                parametro_actual += caracter

    # Agregar el último parámetro después del último '&'
    if parametro_actual:
        parametros.append(parametro_actual)

   

    # Extraer los valores de los parámetros
    valores_parametros = [parametro.split('=')[1] for parametro in parametros]

    return valores_parametros

# Ejemplo de uso
url_ejemplo = "https://retosdeprogramacion.com?year=2023&challenge=0"
valores = obtener_valores_parametros(url_ejemplo)
print(valores)  # Output: ['2023', '0']
