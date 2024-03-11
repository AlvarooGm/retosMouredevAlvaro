'''

/*
 * Crea una función que sume 2 números y retorne su resultado pasados
 * unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que
 *   debe tardar en finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma
 *   asíncrona, es decir, sin detener la ejecución del programa principal.
 *   Se podría ejecutar varias veces al mismo tiempo.
 */

'''
import asyncio



async def suma_espera(n1,n2,segs):
    await asyncio.sleep(segs)
    return n1+n2


async def main():
    # Llamada asíncrona a la función sumar_asincrono
    resultado = await suma_espera(5, 7, 3)
    print(f"El resultado de la suma es: {resultado}")

# Ejecutar el programa principal
if __name__ == "__main__":
    asyncio.run(main())