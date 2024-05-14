# Crie um programa que encontre e mostre o maior e o menor número em uma lista de 10 números digitada pelo usuário.

# Inicializa uma lista vazia para armazenar os números digitados
numeros = []
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior_numero = max(numeros)
menor_numero = min(numeros)

print("O maior número digitado é:", maior_numero)
print("O menor número digitado é:", menor_numero)
