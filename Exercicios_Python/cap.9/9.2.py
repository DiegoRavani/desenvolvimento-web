# Crie uma função que receba uma lista de números e retorne a média aritmética deles. Trate exceções caso a lista seja vazia ou contenha valores não numéricos.

def calcular_media(lista):
    try:
        numeros = [float(x) for x in lista]
        return sum(numeros) / len(numeros)

    except (ValueError, ZeroDivisionError) as e:
        print("Erro:", e)
        return None

lista_numeros = input("Digite uma lista de números separados por espaço: ").split()

media = calcular_media(lista_numeros)

if media is not None:
    print("A média dos números é:", media)
