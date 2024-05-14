# Crie um programa que peça ao usuário para digitar seu peso e sua altura. Em seguida, calcule o índice de massa corporal (IMC) e imprima o resultado. A fórmula do IMC é:

peso = input("Digite seu peso: ")
altura = input("Digite sua altura: ")

imc = float(peso) / float(altura)**2
print(f"Seu IMC é: {imc}")
