'''

/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs:
 * https://github.com/public-apis/public-apis
 */

'''


import requests

# Definir la URL de la API
url = "https://randomuser.me/api/"

# Realizar una solicitud GET
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # La respuesta se devuelve como JSON, por lo que puedes usar .json() para convertirla a un diccionario de Python
    data = response.json()
    # Haz algo con los datos, como imprimirlos
    print(data)
else:
    # Si la solicitud no fue exitosa, imprime el código de estado para depuración
    print("Error al realizar la solicitud. Código de estado:", response.status_code)
