class View:
    @staticmethod
    def menu():
        print('\n============= GESTÃO: MERCADÃO DO ZE ==============\n')
        print('1. Adicionar Produto')
        print('2. Remover Produto')
        print('3. Atualizar Produto')
        print('4. Consultar Produto')
        print('5. Sair')

    @staticmethod
    def capturar_dados():
        nome = input("Digite o nome do produto:")
        quantidade = int(input("Digite a quantidade:"))
        preco = float(input("Digite o preço:"))
        return  nome, quantidade, preco

    @staticmethod
    def capturar_nome_produto():
        return  input("Digite o nome do produto:")

    @staticmethod
    def mostrar_produto(produtos):
        if produtos:
            for produto in produtos:
                print(produto.get_dados())
        else:
            print("Nenhum Produto.")

    @staticmethod
    def mensagem(mensagem):
        print(mensagem)