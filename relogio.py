import time
class Cronometro:
    def __init__(self, dias):
        self.dias = dias
        self.horas = 7
        self.minutos = 30

    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"

    def passaTempo(self, minutos):
        self.minutos += minutos
        while self.minutos >= 60:
            self.minutos -= 60
            self.horas +=1
            while self.horas >= 24:
                self.horas -= 24
                self.dias -= 1

# dias = 0
# relogio = Cronometro(dias)
# while relogio.dias > -1:
#     relogio.passaTempo(30)
#     print(f"Faltam {relogio.dias} para o resgate")
#     print(f"São {relogio}")
#     time.sleep(0.5)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(lista))
print(list(range(1, len(lista))))
