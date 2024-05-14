# :: Implemente uma calculadora que realize operações de soma, subtração, multiplicação e divisão. Utilize tratamento de exceções para lidar com operações inválidas.

def calcular(operacao, num1, num2):
    try:
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida.")
        
        return resultado

    except ZeroDivisionError:
        print("Erro: Divisão por zero.")
    except ValueError as e:
        print("Erro:", e)
    except Exception as e:
        print("Erro inesperado:", e)

try:
    operacao = input("Digite a operaçãoc: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = calcular(operacao, num1, num2)
    if resultado is not None:
        print("Resultado:", resultado)

except ValueError:
    print("Erro: Por favor, insira números válidos.")
except KeyboardInterrupt:
    print("\nOperação interrompida pelo usuário.")
except Exception as e:
    print("Erro inesperado:", e)
