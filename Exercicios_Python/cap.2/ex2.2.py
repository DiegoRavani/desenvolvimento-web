# Crie um programa que verifique se um número digitado pelo usuário é positivo, negativo ou zero.

numero = input("Digite um número: ")

if int(numero) > 0:
    print("o número é positivo")
elif int(numero) < 0:
       print("o número é negativo")
else:
    print("O número é igual a zero")
