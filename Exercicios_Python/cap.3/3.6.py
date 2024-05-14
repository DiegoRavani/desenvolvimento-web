# Crie um programa que some e mostre todos os números ímpares de 1 a 100.
# faça em python

soma_impares = 0
for i in range(1, 101):
    if i % 2 != 0:
        soma_impares += i
print(f"A soma dos números ímpares de 1 a 100 é: {soma_impares}")
