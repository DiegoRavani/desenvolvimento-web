# Crie uma classe chamada Pessoa com um método __init__ que inicialize o nome e a idade da pessoa. Crie um método chamado mostrar_dados que exiba o nome e a idade da pessoa. Crie duas instâncias da classe Pessoa e chame o método mostrar_dados de cada uma das instâncias. 

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)

pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

print("Dados da pessoa 1:")
pessoa1.mostrar_dados()

print("\nDados da pessoa 2:")
pessoa2.mostrar_dados()
