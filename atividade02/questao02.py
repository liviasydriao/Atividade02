#Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

def primos(lista):
    lista_primos = []
    cont = 0
    for num in lista:
        if num == 1: continue
        if num == 2 and num not in lista_primos: 
            lista_primos.append(num)
            continue
        for div in range(2,num):
            if num % div == 0:
                cont += 1
                break
        if cont == 0 and num not in lista_primos:
            lista_primos.append(num)
        cont = 0
    return lista_primos

numeros = [1,2,3,4,2,5,13,41,6,1211,1213]

print(primos(numeros))