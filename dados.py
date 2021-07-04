import random

class Moeda:
    def __init__(self):
        self.lado1 = "CARA"
        self.lado2 = "COROA"
    def jogar(self):
        return random.choice([self.lado1, self.lado2])

class Dados:
    def __init__(self):
        self.lado1 = 1
        self.lado2 = 2
        self.lado3 = 3
        self.lado4 = 4
        self.lado5 = 5
        self.lado6 = 6
    def jogar(self):
        random.choice([self.lado1, self.lado2, self.lado3, self.lado4, self.lado5, self.lado6])

#programa principal
aposta = input("Cara ou Coroa? -> ")
m = Moeda()
resultado = m.jogar()
if aposta == resultado:
    print(f"vc ganhou, deu {resultado}")
else: print(f"vc perdeu, deu {aposta}")

# d = Dados()
# print(d.jogar())