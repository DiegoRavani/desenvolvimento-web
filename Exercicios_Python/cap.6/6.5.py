# Faça um programa que crie um dicionário com nomes e notas de alunos, ambos digitados pelo usuário, usando os nomes dos alunos como chave e as notas como valor. Em seguida, use dict comprehension para criar um dicionário com os alunos com nota igual ou superior a 7.

num_alunos = int(input("Digite o número de alunos: "))

alunos_notas = {}

for _ in range(num_alunos):
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos_notas[nome] = nota

alunos_aprovados = {nome: nota for nome, nota in alunos_notas.items() if nota >= 7}

print("Alunos aprovados:")
for nome, nota in alunos_aprovados.items():
    print(f"{nome}: {nota}")
