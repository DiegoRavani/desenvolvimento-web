# Faça um programa que declare duas listas de mesmo tamanho, uma com 3 nomes de alunos e outra com 3 notas. Em seguida, usando a função zip() e list comprehension, retorne uma lista com as tuplas (nome, nota) em ordem decrescente de nota.

nomes = ["João", "Diego", "José"]
notas = [7.5, 8.0, 6.5]

lista_tuplas = sorted([(nome, nota) for nome, nota in zip(nomes, notas)], key=lambda x: x[1], reverse=True)

print("Lista de tuplas em ordem decrescente de nota:")
for tupla in lista_tuplas:
    print(tupla)
