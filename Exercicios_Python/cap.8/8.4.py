# Crie uma classe chamada Carro com o atributo velocidade e com métodos para acelerar e frear o carro por X segundos, sendo que o carro acelera a 10m/s2 e freia a 5m/s2. Crie uma instância da classe Carro e teste os métodos criados.

class Carro:
    def __init__(self):
        self.velocidade = 0
    
    def acelerar(self, segundos):
        aceleracao = 10
        distancia = 0.5 * aceleracao * segundos ** 2
        self.velocidade += distancia
    
    def frear(self, segundos):
        desaceleracao = 5
        distancia = 0.5 * desaceleracao * segundos ** 2
        if self.velocidade - distancia >= 0:
            self.velocidade -= distancia
        else:
            self.velocidade = 0
            
meu_carro = Carro()

meu_carro.acelerar(5)
print("Velocidade após acelerar:", meu_carro.velocidade)

meu_carro.frear(3)
print("Velocidade após frear:", meu_carro.velocidade)
