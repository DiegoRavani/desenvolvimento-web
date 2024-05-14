# Crie uma classe chamada Livro com um método __init__ que inicialize o título e o autor do livro. Crie um método chamado mostrar_dados que exiba o título e o autor do livro. Crie uma classe chamada LivroFisico que herde da classe Livro e adicione um atributo chamado paginas. Crie um método chamado mostrar_dados na classe LivroFisico que exiba o título, o autor e o número de páginas do livro. Crie uma instância da classe LivroFisico e chame o método mostrar_dados.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrar_dados(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)

class LivroFisico(Livro):
    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo, autor)
        self.paginas = paginas
    
    def mostrar_dados(self):
        super().mostrar_dados()
        print("Número de páginas:", self.paginas)

livro1 = LivroFisico("Dom Quixote", "Miguel de Cervantes", 1033)

livro1.mostrar_dados()
