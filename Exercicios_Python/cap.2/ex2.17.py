# Crie um programa que pergunte ao usuário sua idade e exiba uma mensagem de acordo com as seguintes regras: "Você é jovem" se a idade for menor do que 21; "Você é adulto" se a idade estiver entre 21 e 60; ou "Você é idoso" caso a idade seja superior a 60.

idade = input("Digite sua idade: ")

if int(idade) < 21:
    print("Você é jovem")
elif int(idade) > 21 and int(idade) <= 60:
    print("Você é adulto")       
else:
    print("Você é idoso")