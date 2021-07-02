from random import randint

def dado(n):
    return randint(1, n)

def menuIr():
    print("Para onde deseja ir:\n[1] Mercado\n[2] Hospital\n[3] Posto de Combustível\n[4] Abrigo")
    return int(input(">> "))

def menuAcao(lugar):
    print("O que deseja fazer?\n[1] Ir para outro lugar\n[2] Comer\n[3] Tomar remédio")
    if lugar == 4:
        print("[4] Descansar")
    return int(input(">> "))

def luta(p, z):
    while p.vida > 0 and z.vida > 0:
        ini = dado(2)
        if ini == 1:
            print("O zumbi te atacou!")
            z.atacar(p)
            print(vars(p))
            print(vars(z))

        acao = int(input("O que deseja fazer?\n[1] Atacar\n[2] Fugir\n>> "))
        if acao == 1:
            arma = int(input("Selecione a Arma: \n[1] Faca\n[2] Pistola\n>> " ))
            print("Você atacou o zumbi!")
            p.atacar(z, arma)
            print(vars(p))
            print(vars(z))
        elif acao == 2:
            p.fugir()
            print("Você fugiu!")
            break

class Sobrevivente:
    def __init__(self, vida, infeccao = False):
        self.vida = vida
        self.infectado = infeccao
        self.dmg = 2
        self.energia = 20
    def atacar(self, inimigo, arma):
        if arma == 1:
            dmgMod = 1.3
        elif arma == 2:
            dmgMod = 2
        inimigo.tomarDano(dado(20) * dmgMod * self.dmg)
    def tomarDano(self,dmg):
        self.vida -= dmg
        if self.infectado == False:
            self.infectado = True if dado(2) == 1 else False
        elif self.infectado == True:
            pass
    def fugir(self):
        self.energia -= 2
    def descansar(self):
        self.energia += 10

class Zumbi:
    def __init__(self):
        self.vida = 20
        self.dmg = 1
    def atacar(self, inimigo):
        inimigo.tomarDano(dado(20) * self.dmg)
    def tomarDano(self,dmg):
        self.vida -= dmg
        if self.vida < 0:
            self.vida = 0

class inventario:
    def __init__(self, combustivel, comida, medicamento):
        self.combustivel = combustivel
        self.comida = comida
        self.medicamento = medicamento
        self.pistola = True
        self.faca = True

class Lugar:
    def __init__(self, nome):
        self.nome = nome
    
    def setLugar(self, x):
        if x == 1:
            self.nome = "Mercado"
            self.item = ["comida" , dado(5)]
        if x == 2:
            self.nome = "Hospital"
            self.item = ["remédio", dado(5)]
        if x == 3:
            self.nome = "Posto de Combustível"
            self.item = ["gasolina", dado(5)]


lugarAtual = Lugar("Abrigo")
lugar = menuIr()
personagem = Sobrevivente(100, False)
zumbi = Zumbi()
print(f"personagem {vars(personagem)}")
print(f"zumbi {vars(zumbi)}")
print(15*"-=-")
luta(personagem, zumbi)
