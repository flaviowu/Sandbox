import random

class dadoMoeda:
    def __init__(self):
        self.lado1 = 1
        self.lado2 = 2
        self.lado3 = 3
        self.lado4 = 4
        self.lado5 = 5
        self.lado6 = 6
    
    def jogarDados(self):
        resultado = random.choice([self.lado1, self.lado2, self.lado3, self.lado4, self.lado5, self.lado6])
        return resultado
    
    def jogarMoeda(self):
        resultado = random.choice([self.lado1, self.lado2])
        if resultado == 1:
            resultado = "CARA"
        elif resultado == 2:
            resultado = "COROA"
        return resultado

aposta = input("Cara ou Coroa? -> ")
m = dadoMoeda()
resultado = m.jogarMoeda()
if aposta == resultado:
    print(f"vc ganhou, deu {resultado}")
else: print(f"vc perdeu, deu {resultado}")
