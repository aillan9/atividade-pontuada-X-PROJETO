import os
os.system ("cls || clear")

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.comprados = []

    def adicionar_livro(self, titulo, autor):
        self.livros.append({'titulo': titulo, 'autor': autor})
        print(f"Livro '{titulo}' adicionado!")

    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro['titulo'] == titulo:
                self.livros.remove(livro)
                print(f"Livro '{titulo}' removido!")
                return
        print(f"Livro '{titulo}' não encontrado.")