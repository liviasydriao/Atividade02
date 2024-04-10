#Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.
#retornar uma terceira lista que contenha apenas os elementos que estão na lista 1 e não estão na lista2 e os que estão na lista2 e não estão na lista1. 

def em_comum3(lista1,lista2):
    lista3 = set()
    for num in lista1:
        if num not in lista2:
            lista3.add(num)
    for num in lista2:
        if num not in lista1:
            lista3.add(num)
    return list(lista3)

list1 = [1,23,4,4,5,5,435,480,34,102,1345,1345]
list2 = [1,23,90,369,4,4,5,5,435,480,90]

print(em_comum3(list1,list2))
