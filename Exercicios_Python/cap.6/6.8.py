# Faça um programa que peça ao usuário para digitar uma lista de números e que use mapeamento (map()) para retornar uma nova lista com os quadrados de cada número.

numeros = input("Digite uma lista de números separados por espaço: ").split()

quadrados = list(map(lambda x: int(x) ** 2, numeros))

print("Quadrados dos números digitados:", quadrados)
