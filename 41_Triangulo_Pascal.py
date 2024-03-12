'''

/*
 * Crea una función que sea capaz de dibujar el "Triángulo de Pascal"
 * indicándole únicamente el tamaño del lado.
 *
 * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
 *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
 */


'''
# Define una función llamada pascal_triangle que toma un argumento "size" que indica el tamaño del lado del Triángulo de Pascal que se desea dibujar.
def pascal_triangle(size):
    # Define una función interna llamada binomial_coefficient para calcular los coeficientes binomiales necesarios para el Triángulo de Pascal.
    def binomial_coefficient(n, k):
        # Si k es 0 o n, devuelve 1, ya que los extremos del Triángulo de Pascal siempre son 1.
        if k == 0 or k == n:
            return 1
        else:
            # Calcula recursivamente los coeficientes binomiales utilizando la fórmula recursiva C(n, k) = C(n-1, k-1) + C(n-1, k).
            return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

    # Itera sobre las filas del Triángulo de Pascal (i representa el número de la fila).
    for i in range(size):
        # Imprime espacios en blanco para alinear los coeficientes en forma de triángulo.
        for j in range(size - i - 1):
            print(" ", end="")
        # Itera sobre los elementos de la fila i para imprimir los coeficientes binomiales.
        for j in range(i + 1):
            # Llama a la función binomial_coefficient para obtener el coeficiente binomial correspondiente y lo imprime.
            print(binomial_coefficient(i, j), end=" ")
        # Imprime una nueva línea después de imprimir todos los elementos de la fila i.
        print()

# Ejemplo de uso:
# Asigna el tamaño del lado del Triángulo de Pascal que deseas dibujar.
size = 20
# Llama a la función pascal_triangle con el tamaño especificado para dibujar el Triángulo de Pascal.
pascal_triangle(size)
