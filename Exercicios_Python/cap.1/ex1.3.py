# Crie um programa que peça ao usuário para digitar três números, armazenando-os em variáveis distintas. Em seguida, imprima a média aritmética dos três números.

numero1 = input("Digite o primeiro número:")
numero2 = input("Digite o segundo número:")
numero3 = input("Digite o terceito número:")

media = int(numero1) + int(numero2) + int(numero3) / 3

print(f"A média aritmética é:{media}")