'''

/*
 * Crea una función que sea capaz de detectar y retornar todos los
 * handles de un texto usando solamente Expresiones Regulares.
 * Debes crear una expresión regular para cada caso:
 * - Handle usuario: Los que comienzan por "@"
 * - Handle hashtag: Los que comienzan por "#"
 * - Handle web: Los que comienzan por "www.", "http://", "https://"
 *   y finalizan con un dominio (.com, .es...)
 */


'''

handleUser = '@'
handleHastag = '#'
handleWeb = ["www.", "http://", "https://"]
handleWebFin = ['.com', '.es']

palabra = 'www.alvaro.com'

if palabra.startswith(handleUser):
    print('Es un usuario')
elif palabra.startswith(handleHastag):
    print('Es un hastag')    
else:
    for h,a in zip(handleWeb,handleWebFin):
        if palabra.startswith(h) and palabra.endswith(a):
            print('Es un dominio')
