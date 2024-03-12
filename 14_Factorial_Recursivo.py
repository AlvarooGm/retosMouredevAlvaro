'''

/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */

'''

def factorial_recursivo(num):
    if num==1 or num == 0:
        return 1
    else:
     num = num*factorial_recursivo(num-1)
     return num
    
print(factorial_recursivo(5))    