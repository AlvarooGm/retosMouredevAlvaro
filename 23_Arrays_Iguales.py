def encontrar_igual(ar1, ar2, ig_noig):
    resultado = []

    if ig_noig:
        for a in ar1:
            if a in ar2:
                resultado.append(a)
    else:
        resultado=ar2
        for a in ar1:
            if a not in ar2:
                resultado.append(a)
            else:
                indice = ar2.index(a)
                resultado.pop(indice)    

                

    return resultado

ar1 = [1, 2, 3, 4]
ar2 = [4, 5, 6, 1]
ar3 = encontrar_igual(ar1, ar2, True)
ar4 = encontrar_igual(ar1, ar2, False)

print(ar3)
print('------')
print(ar4)
