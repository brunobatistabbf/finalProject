from model import Cliente
from dao import ClienteDAO

class APP:
    def __init__(self):
        self.dao = ClienteDAO()

    def dados_cliente(self):
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o email do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        return nome, email, telefone

    def adicionar_cliente(self):
        nome, email, telefone = self.dados_cliente()
        cliente = Cliente(nome, email, telefone)
        self.dao.adicionar_cliente(cliente)
        print("Cliente adicionado com Sucesso!!!")

    def remover_cliente(self):
        nome = input("Digite o nome do cleinte: ")
        if self.dao.remover_cliente(nome):
            print("Cliente removido com sucesso!")
        else:
            print("Cliente não encontrado")

    def atualizar_cliente(self):
        nome = input("Digite o nome do cliente: ")
        if nome:
            email, telefone  = self.dados_cliente()[1:]
            if self.dao.atualizar_cliente(nome, email, telefone):
                print("Cliente atualizado!")
            else:
                print("Cliente não encontrado.")

    def listar_clientes(self):
        clientes = self.dao.listar_clientes()
        if clientes:
            for cliente in clientes:
                print(cliente.get_dados())
        else:
            print("Nenhum cliente encontrado.")


    def executar(self):
        while True:
            print('\n=============Cadastro de Clientes==========')
            print('1. Adicionar Cliente')
            print('2. Remover Cliente')
            print('3. Atualizar Cliente')
            print('4. Listar Cliente')
            print('5. Sair')
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.adicionar_cliente()
            elif opcao == '2':
                self.remover_cliente()
            elif opcao == '3':
                self.atualizar_cliente()
            elif opcao == '4':
                self.listar_clientes()
            elif opcao == '5':
                print("Saindo...")
                break
            else:
                print("Opção Invalida")