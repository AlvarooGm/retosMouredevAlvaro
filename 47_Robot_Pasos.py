'''


/*
 * Calcula dónde estará un robot (sus coordenadas finales) que se
 * encuentra en una cuadrícula representada por los ejes "x" e "y".
 * - El robot comienza en la coordenada (0, 0).
 * - Para idicarle que se mueva, le enviamos un array formado por enteros
 *   (positivos o negativos) que indican la secuencia de pasos a dar.
 * - Por ejemplo: [10, 5, -2] indica que primero se mueve 10 pasos, se detiene,
 *   luego 5, se detiene, y finalmente 2.
 *   El resultado en este caso sería (x: -5, y: 12)
 * - Si el número de pasos es negativo, se desplazaría en sentido contrario al
 *   que está mirando.
 * - Los primeros pasos los hace en el eje "y". Interpretamos que está mirando
 *   hacia la parte positiva del eje "y".
 * - El robot tiene un fallo en su programación: cada vez que finaliza una
 *   secuencia de pasos gira 90 grados en el sentido contrario a las agujas
 *   del reloj.
 */


'''

import matplotlib.pyplot as plt


ejeY = 0
ejeX = 0

pasosR = []

primerosPasos = [3,4,5,6]

axis_Y_X = True #Si es true eje Y si es false eje X

for p in primerosPasos:
    if axis_Y_X:
        ejeY+=p
        axis_Y_X = False
    else:
        ejeX+=p
        axis_Y_X = True
pasosR = [ejeX,ejeY]
  

print("Coordenadas finales del robot:", (ejeX, ejeY))

# Crear la figura y los ejes para el gráfico
fig, ax = plt.subplots(figsize=(6, 7))

# Crear el gráfico de dispersión
ax.scatter(ejeX, ejeY)

# Configurar etiquetas y título
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Posición final del robot')

# Mostrar el gráfico
plt.show()