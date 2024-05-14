# Crie uma classe chamada Retangulo com um método __init__ que inicialize a largura e a altura do retângulo. Crie um método chamado area que retorne a área do retângulo. Crie uma instância da classe Retangulo e chame o método area

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura

retangulo1 = Retangulo(5, 8)

print("Área do retângulo:", retangulo1.area())
