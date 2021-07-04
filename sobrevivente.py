from random import randint
import time
import sys


def escrever_rpg(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.01)


def inicio():
    textoInicial = "O ano é 2035...\nA humanidade não encontrou a cura para o COVID-19XF (Evolução do vírus original).\nVocê é um dos poucos ainda vivo!!!\nEm 7 dias, um helicóptero virá lhe buscar....\nSobreviva!!!\n \n \n \n"
    escrever_rpg(textoInicial)
    introducao = "Você está no seu abrigo, porém, há pouca comida e existem infectados nesta área!\n"
    escrever_rpg(introducao)
    menu(l_menu["acoes"])


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
            self.horas += 1
            while self.horas >= 24:
                self.horas -= 24
                self.dias -= 1


def dado(n):
    return randint(1, n)


def menu(lista):
    opcoes = enumerate(lista, 1)
    for i, v in opcoes:
        print(f"[{i}] - {v}")
    resposta = int(input("Escolha da opção\n-> "))
    while resposta not in range(1, len(lista)):
        resposta = int(input("\n\n->  "))
        return resposta - 1

# def menuAcao(lugar):
#     print(
#         "O que deseja fazer?\n[1] Ir para outro lugar\n[2] Comer\n[3] Tomar remédio")
#     if lugar == 4:
#         print("[4] Descansar")
#     return int(input(">> "))


def luta(p, z):
    while p.vida > 0 and z.vida > 0:
        ini = dado(20)
        if ini <= 4:
            print("O zumbi te atacou!")
            z.atacar(p)
            print(vars(p))
            print(vars(z))

        acao = menu(l_menu["luta"])
        if acao == 1:
            arma = menu(l_menu["armas"])
            print("Você atacou o zumbi!")
            p.atacar(z, arma)
            print(vars(p))
            print(vars(z))
        elif acao == 2:
            p.fugir()
            print("Você fugiu!")
            break


class Sobrevivente:
    def __init__(self, vida, infeccao=False, t=3):
        self.vida = vida
        self.infectado = infeccao
        self.dmg = 2
        self.energia = 20
        self.lugar = "Abrigo"
        self.inventario = Inventario(5, 10, 5)

    def __str__(self):
        return f"Vida: {self.vida}\nEnergia: {self.energia}\n{'Infectado' if self.infectado == True else 'Saudável'}"

    def atacar(self, inimigo, arma):
        if arma == 1:
            dmgMod = 1.3
        elif arma == 2:
            dmgMod = 2
        inimigo.tomarDano(dado(20) * dmgMod * self.dmg)

    def tomarDano(self, dmg):
        self.vida -= dmg
        if self.infectado == False:
            self.infectado = True if dado(2) == 1 else False
        elif self.infectado == True:
            pass

    def fugir(self):
        self.energia -= 2

    def comer(self):
        self.vida += 10
        self.inventario.comida -= 1
        if self.vida > 100:
            self.vida = 100

    def tomarRemedio(self):
        self.infectado = False
        self.inventario.medicamento -= 1

    def locomover(self, lugar):
        self.lugar = lugar
        self.inventario.combustivel -= 1

    def descansar(self):
        self.energia += 5
        self.inventario.comida -= 3
        if self.energia > 20:
            self.energia = 20


class Zumbi:
    def __init__(self):
        self.vida = 20
        self.dmg = 1

    def atacar(self, inimigo):
        inimigo.tomarDano(dado(20) * self.dmg)

    def tomarDano(self, dmg):
        self.vida -= dmg
        if self.vida < 0:
            self.vida = 0


class Inventario:
    def __init__(self, combustivel, comida, medicamento):
        self.combustivel = combustivel
        self.comida = comida
        self.medicamento = medicamento
        self.pistola = True
        self.faca = True


class Lugar:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Localização: {self.nome}"

    def setLugar(self, x):
        if x == 1:
            self.nome = "Mercado"
            self.item = {"comida": dado(3)}
        if x == 2:
            self.nome = "Hospital"
            self.item = {"remédio": dado(3)}
        if x == 3:
            self.nome = "Posto de Combustível"
            self.item = {"gasolina": dado(3)}
        if x == 4:
            self.nome = "Abrigo"


l_menu = {"lugares": ["Mercado", "Hospital", "Posto de Combustível", "Abrigo"], "armas": ["Faca", "Pistola"],
          "luta": ["Atacar", "Fugir"],
          "acoes": ["Ir para outro lugar", "Comer", "Tomar Remédio", "Descansar"]}

personagem = Sobrevivente(100, False)
lugarAtual = Lugar("Abrigo")
relogio = Cronometro(2)
inicio()
print(relogio)
print(personagem)
print(lugarAtual)

zumbi = Zumbi()
