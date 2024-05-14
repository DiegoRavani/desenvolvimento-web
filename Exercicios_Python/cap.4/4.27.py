# Faça um programa que crie um objeto datetime representando um instante específico. Em seguida, adicione 2 dias e 5 horas a esse instante utilizando timedelta.

from datetime import datetime, timedelta

instante_especifico = datetime.now()

duracao = timedelta(days=2, hours=5)
novo_instante = instante_especifico + duracao

print("Instante específico original:", instante_especifico)
print("Novo instante após adicionar 2 dias e 5 horas:", novo_instante)


