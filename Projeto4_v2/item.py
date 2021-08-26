class Comida:
    def __init__(self, qtd):
        self.qtd = qtd
        self.life = 10

    def getLife(self):
        return self.life


class Backpack:
    def __init__(self):
        self.comida = Comida(10)

    def __str__(self):
        return f"Você tem {self.comida} porções de comida"

    def setComida(self, n):
        self.comida.qtd += n