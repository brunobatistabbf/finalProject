class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def get_dados(self):
        return f'Produto:{self.nome}\n Quantidade: {self.quantidade}\n Preço: R${self.preco:.2f}'



class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)


    def remover(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                self.produtos.remove(produto)
                return  True
            else:
                return False

    def atualizar(self, nome_produto, quantidade, preco):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                produto.quantidade = quantidade
                produto.preco = preco
                return True
            else:
                return False

    def consultar(self):
        return self.produtos