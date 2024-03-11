'''

/*
 * Simula el funcionamiento de una máquina expendedora creando una operación
 * que reciba dinero (array de monedas) y un número que indique la selección
 * del producto.
 * - El programa retornará el nombre del producto y un array con el dinero
 *   de vuelta (con el menor número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe,
 *   deberá indicarse con un mensaje y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas
 *   de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
 */

'''

arra_Mon = [5, 10, 50, 100, 200]
precio_Prod = 235
prod = 'Chocolate'

arr_Pago = []
arr_Vuelta = []

while sum(arr_Pago) < precio_Prod:
    try:
        mon = int(input('Ingrese moneda (5, 10, 50, 100, 200): '))
        if mon not in arra_Mon:
            print('Moneda no válida. Por favor, ingrese una moneda válida.')
            continue
        arr_Pago.append(mon)
    except ValueError:
        print('Por favor, ingrese un número válido.')

if sum(arr_Pago) >= precio_Prod:
    cambio = sum(arr_Pago) - precio_Prod
    cambio_restante = cambio

    for moneda in arra_Mon[::-1]:
        while cambio_restante >= moneda:
            arr_Vuelta.append(moneda)
            cambio_restante -= moneda

    if cambio_restante == 0:
        print(f'Se ha comprado {prod}. Cambio: {arr_Vuelta}')
    else:
        print('No se puede dar el cambio exacto con las monedas disponibles. Devolviendo todas las monedas.')
else:
    print('Dinero insuficiente para comprar el producto. Devolviendo todas las monedas.')
