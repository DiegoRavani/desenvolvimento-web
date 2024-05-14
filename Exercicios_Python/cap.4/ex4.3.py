# :: Crie um programa que peça ao usuário para inserir um ângulo em graus e calcule o seno, o cosseno e a tangente desse ângulo.

import math

angulo_graus = float(input("Digite o ângulo em graus: "))
angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f"O seno do ângulo {angulo_graus} graus é: {seno}")
print(f"O cosseno do ângulo {angulo_graus} graus é: {cosseno}")
print(f"A tangente do ângulo {angulo_graus} graus é: {tangente}")
