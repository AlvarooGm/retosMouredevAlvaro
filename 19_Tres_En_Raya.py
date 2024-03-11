'''

*
 * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
 * y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 *   O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta.
 * Se podría representar con un vacío "", por ejemplo.
 */

'''

def verificar_ganador(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != ' ':
            return tablero[i][0]  # Retorna el jugador que ganó
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != ' ':
            return tablero[0][i]  # Retorna el jugador que ganó

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != ' ':
        return tablero[0][0]  # Retorna el jugador que ganó
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != ' ':
        return tablero[0][2]  # Retorna el jugador que ganó

    return None  # Nadie ha ganado todavía

# Ejemplo de uso
tablero_ejemplo = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['X', ' ', 'O']
]

ganador = verificar_ganador(tablero_ejemplo)

if ganador:
    print(f"¡El jugador {ganador} ha ganado!")
else:
    print("No hay un ganador todavía.")
