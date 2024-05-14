# Crie um programa que calcule e mostre a sequência de Fibonacci até o n-ésimo termo, onde n é digitado pelo usuário.

n = int(input("Digite o número de termos da sequência Fibonacci: "))

fibonacci = [0, 1]

for i in range(2, n):
    termo_atual = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(termo_atual)
    
print("Sequência de Fibonacci até o", n, "º termo:")
for termo in fibonacci:
    print(termo, end=" ")
