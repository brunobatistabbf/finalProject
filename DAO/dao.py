class ClienteDAO:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        return True

    def remover_cliente(self, nome_cliente):
        for cliente in self.clientes:
            if cliente.nome == nome_cliente:
                self.clientes.remove(cliente)
                return True
        return False

    def atualizar_cliente(self, nome_cliente, email, telefone):
        for cliente in self.clientes:
            if cliente.nome == nome_cliente:
                cliente.email = email
                cliente.telefone = telefone
                return True
        return False

    def listar_clientes(self):
        return self.clientes