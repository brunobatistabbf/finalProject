from model import Estoque, Produto
from view import  View

class Controller:
    def __init__(self):
        self.estoque = Estoque()
        self.view = View()

    def adicionar_produto(self):
        nome, quantidade, preco = self.view.capturar_dados()
        produto = Produto(nome, quantidade, preco)
        self.estoque.adicionar(produto)
        self.view.mensagem("Produto adicionado com sucesso!!!")

    def remover_produto(self):
        nome = self.view.capturar_nome_produto()
        if self.estoque.remover(nome):
            self.view.mensagem("Produto removido!")
        else:
            self.view.mensagem("Produto não encontrado")

    def atualizar_produto(self):
        nome = self.view.capturar_nome_produto()
        if nome:
            quantidade, preco = self.view.capturar_dados()[1:]
            if self.estoque.atualizar(nome, quantidade, preco):
                self.view.mensagem("Produto atualizado!")
            else:
                self.view.mensagem("Produto não encontrado")

    def consultar_produto(self):
        produtos = self.estoque.consultar()
        self.view.mostrar_produto(produtos)

    def executar(self):
        while True:
            self.view.menu()
            opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                self.adicionar_produto()
            elif opcao == '2':
                self.remover_produto()
            elif opcao == '3':
                self.atualizar_produto()
            elif opcao == '4':
                self.consultar_produto()
            elif opcao == '5':
                self.view.mensagem("Saindo...")
                break
            else:
                self.view.mensagem("Escolha uma opção válida!\n")