from Computador import Computador


class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return super().getInformacoes() + f", Potência da fonte: {self._potenciaDaFonte} watts"

    def cadastrar(self):
        return f"Cadastrando Desktop: {self.modelo}, da cor {self.cor}, valor: R$ {self.preco}\nPotencia da fonte: {self._potenciaDaFonte} Watts"
