class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    # métodos set e get. Set envia, get pega

    # método get
    @property
    def nome(self):
        return self.__nome
    
    # método set
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # Agora para o CPF
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf