'''

/*
 * Dado un array de números enteros positivos, donde cada uno
 * representa unidades de bloques apilados, debemos calcular cuantas unidades
 * de agua quedarán atrapadas entre ellos.
 *
 * - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].
 *
 *         ⏹
 *         ⏹
 *   ⏹💧💧⏹
 *   ⏹💧⏹⏹💧⏹
 *   ⏹💧⏹⏹💧⏹
 *   ⏹💧⏹⏹⏹⏹
 *
 *   Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades
 *   de agua. Suponemos que existe un suelo impermeable en la parte inferior
 *   que retiene el agua.
 */

'''


def trap_water(heights):
    n = len(heights)
    if n <= 2:
        return 0
    
    left_max = [0] * n
    right_max = [0] * n
    
    # Calcular la altura máxima a la izquierda de cada bloque
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], heights[i])
    
    # Calcular la altura máxima a la derecha de cada bloque
    right_max[n-1] = heights[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], heights[i])
    
    # Calcular el agua atrapada para cada bloque y sumarla
    water_trapped = 0
    for i in range(n):
        water_trapped += max(min(left_max[i], right_max[i]) - heights[i], 0)
    
    return water_trapped

# Ejemplo de uso
heights = [4, 0, 3, 6, 1, 3]
print("Unidades de agua atrapadas:", trap_water(heights))
