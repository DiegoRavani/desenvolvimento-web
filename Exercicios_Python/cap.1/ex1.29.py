# Crie um programa que tenha um dicionário com os nomes, idades e cor dos olhos de 5 membros da sua família. Cada item do dicionário deve ter o nome da pessoa como chave e uma tupla associada contendo a idade e a cor dos olhos.

familia = {
    'Pai': (45, 'castanhos'),
    'Mãe': (40, 'Pretos'),
    'Irmão': (13, 'castanhos'),
    'Avó': (75, 'Verdes'),
    'Avô': (80, 'azuis')
}

for membro, detalhes in familia.items():
    idade, cor_olhos = detalhes
    print(f"{membro} - Idade: {idade}, Cor dos olhos: {cor_olhos}")
