#Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.

def segundo_maior(lista):
    lista1 = list(sorted(set(lista)))
    return lista1[1]

list1 = [22,3,4,89,34,6,3,3,5,432,678]
list2 = [472,56,19874,1000]
print(segundo_maior(list1))
print(segundo_maior(list2))
