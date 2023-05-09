from Computador import Computador


class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        return super().getInformacoes() + f", Tempo de Bateria: {self.__tempoDeBateria} horas"

    def cadastrar(self):
        return f"Cadastrando Notebook: {self.modelo}, da cor {self.cor}, valor: R$ {self.preco} \nTempo de Bateria: {self.__tempoDeBateria} horas"
