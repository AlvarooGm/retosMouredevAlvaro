'''

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

'''


def esPar_Impar(num):
    par_impar = 'Par' if num%2==0 else 'Impar'
    return par_impar

def sucesionFibo(num):
    fibo = 0
    sig = 1
    res =[]
    for a in range(0,num+1):
        res.append(fibo)
        fibo,sig= sig , fibo+sig
    
   
    es_Fibo = 'Fibonacci' if num in res else 'No es fibonacci'
    return es_Fibo


def primo(num):
    cnt = 0
    for a in range(1,num):
        if num%a == 0:
            cnt*=1
    es_primo = 'Es primo' if cnt<=2 else 'No es primo'
    return es_primo

num = 6
resultado = f'{num}: {primo(num)}, {sucesionFibo(num)}, {esPar_Impar(num)}'  
print(resultado)