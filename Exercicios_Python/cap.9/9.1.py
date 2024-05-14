# Crie um programa que solicite ao usuário dois números inteiros e exiba a divisão do primeiro número pelo segundo. Trate possíveis exceções de divisão por zero.

def dividir_numeros():
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número inteiro: "))

        resultado = num1 / num2
        print("Resultado da divisão:", resultado)

    except ValueError:
        print("Por favor, digite apenas números inteiros.")
    
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")

dividir_numeros()

