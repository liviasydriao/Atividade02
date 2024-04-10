#Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.

def lista_impares(lista):
    impares = [num for num in lista if num % 2==1]
    return impares


lista_num = []
x = 0
print("Digite um número ou '-1' quando desejar parar de inseri-los")
while True:
    x = int(input())
    if x == -1:
        break
    lista_num.append(x)


print("dos números que você digitou, apenas esses são ímpares: " , lista_impares(lista_num))
