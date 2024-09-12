class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def get_dados(self):
        return  f'Nome: {self.nome}\n Email: {self.email}\n Telefone: {self.telefone}'

