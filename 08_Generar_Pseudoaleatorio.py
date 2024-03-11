'''

/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del 
 *   lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

'''
class GeneradorPseudoaleatorio:
    def __init__(self, semilla):
        self.estado = semilla

    def generar_numero(self, rango_inicio, rango_fin):
        a = 1664525
        c = 1013904223
        m = 2**32

        self.estado = (a * self.estado + c) % m
        numero_pseudoaleatorio = self.estado % (rango_fin - rango_inicio + 1) + rango_inicio
        return numero_pseudoaleatorio

# Uso del generador pseudoaleatorio
semilla_inicial = 42  # Puedes cambiar la semilla inicial
generador = GeneradorPseudoaleatorio(semilla_inicial)

# Generar varios números pseudoaleatorios entre 0 y 100
for _ in range(10):
    numero_aleatorio = generador.generar_numero(0, 100)
    print(numero_aleatorio)
