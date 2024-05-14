# Crie um programa que calcule a média de três números e exiba a mensagem "Aprovado" se a média for maior ou igual a 6 ou "Reprovado" caso contrário. Se a nota for 10, exiba também a mensagem "Parabéns".

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = nota1 + nota2 + nota3 / 3
if media >= 6:
    print("Aprovado")
if media == 10:
    print("Parabéns")            
if media < 6:
    print("Reprovado")    