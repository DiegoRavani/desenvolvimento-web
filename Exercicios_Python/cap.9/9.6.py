# Implemente um jogo de adivinhação em que o usuário deve acertar um número entre 1 e 10. Utilize tratamento de exceções para garantir que o usuário insira apenas números válidos.

import random

def jogo_adivinha():
    numero_secreto = random.randint(1, 10)
    
    try:
        while True:
            try:
                palpite = int(input("Adivinhe um número entre 1 e 10: "))
                if palpite < 1 or palpite > 10:
                    raise ValueError("Por favor, insira um número entre 1 e 10.")
            except ValueError as ve:
                print("Erro:", ve)
                continue
            
            if palpite == numero_secreto:
                print("Parabéns! Você acertou o número!")
                break
            else:
                print("Número incorreto. Tente novamente.")
    
    except KeyboardInterrupt:
        print("\nJogo interrompido pelo usuário.")

jogo_adivinha()
