#Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.

def ordenada(lista):
    lista = sorted(lista)
    return lista

lista_pessoas = [
    ("João", 30),
    ("Maria", 25),
    ("Pedro", 40),
    ("Ana", 35),
    ("Carlos", 28)
]

print(ordenada(lista_pessoas))