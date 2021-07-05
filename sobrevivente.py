from random import randint
import time
import sys


def escrever_rpg(texto):
    for letra in str(texto):
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.01)


def inicio():
    textoInicial = "O ano é 2035...\nO que começou em 2019 supostamente como uma gripezinha, se transformou em uma epidemia e de epidemia, evoluiu para pandemia e depois num PANDEMONIO.\n As pessoas infectadas desenvolveram um tipo de demencia e ficaram violentas. Logo, a doença atingiu a maioria das pessoas e tomou conta do mundo.\nSe você está lendo esta mensagem, você é um sobrevivente!!!\nRecebemos a sua localização, em 3 dias um helicóptero chegará para te resgatar...\nSobreviva até lá!!!\n\n\n"
    escrever_rpg(textoInicial)
    introducao = "Você está no seu abrigo, porém, há pouca comida e existem infectados nesta área!\n"
    escrever_rpg(introducao)


class Cronometro:
    def __init__(self, dias):
        self.dias = dias
        self.horas = 7
        self.minutos = 30

    def __str__(self):
        return f"{self.horas:02d}h{self.minutos:02d}\n"

    def passaTempo(self, minutos):
        self.minutos += minutos
        while self.minutos >= 60:
            self.minutos -= 60
            self.horas += 1
            while self.horas >= 24:
                self.horas -= 24
                self.dias -= 1


def dado(n, i=1):
    return randint(i, n)


def menu(lista):
    opcoes = enumerate(lista, 1)
    for i, v in opcoes:
        escrever_rpg(f"[{i}] - {v}\n")
    # resposta = int(input("Escolha da opção\n-> "))
    resposta = ""
    resposta_int = 0
    while True:
        resposta = input("\n-> ")
        if resposta.isnumeric():
            resposta_int = int(resposta)
            if resposta_int in list(range(1, len(lista)+1)):
                break
            else: continue
        else: continue
    return lista[int(resposta) - 1]


def status(personagem):
    escrever_rpg(f"Faltam {personagem.relogio.dias} dias para o resgate.\n")
    escrever_rpg(personagem.relogio)
    escrever_rpg(personagem)


def luta(p):
    n = dado(3, 1)
    escrever_rpg(f"Cuidado! Você encontrou {n} zumbi(s)!\n")
    while n > 0:
        z = Zumbi()
        while p.vida > 0 and z.vida > 0:
            iniciativa = dado(20)
            if iniciativa <= 4:
                escrever_rpg("O zumbi te atacou!\n")
                z.atacar(p)

            acao = menu(l_menu["luta"])
            if acao == "Atacar":
                if p.inventario.municao > 0:
                    arma = menu(l_menu["armas"])
                    escrever_rpg("Você atacou o zumbi!\n")
                else:
                    arma == "Faca"
                p.atacar(z, arma)
            elif acao == "Fugir":
                p.fugir()
                escrever_rpg("Você fugiu!\n")
                break
        n = n-1


class Sobrevivente:
    def __init__(self, vida=100, t=1):
        self.vida = vida
        self.infectado = False
        self.dmg = 2
        self.energia = 20
        self.lugar = "Abrigo"
        self.inventario = Inventario(2, 2, 2)
        self.relogio = Cronometro(t)

    def __str__(self):
        return f"Vida: {self.vida}\nEnergia: {self.energia}\nStatus: {'Infectado' if self.infectado == True else 'Saudável'}\nLocal Atual: {self.lugar}\n"

    def getInventario(self):
        escrever_rpg(self.inventario)

    def atacar(self, inimigo, arma):
        if arma == "Faca":
            dmgMod = 1.3
        elif arma == "Pistola":
            dmgMod = 2
            self.inventario.municao -= 1
            escrever_rpg(f"Voce tem {self.inventario.municao} balas\n")
        inimigo.tomarDano(dado(20) * dmgMod * self.dmg)
        self.relogio.passaTempo(10)
        self.energia -= 1

    def tomarDano(self, dmg):
        self.vida -= dmg
        self.energia -= 1
        if self.vida < 0:
            escrever_rpg("Você Morreu!\n")
        if self.infectado == False:
            self.infectado = True if dado(2) == 1 else False
        elif self.infectado == True:
            pass
        self.relogio.passaTempo(10)

    def fugir(self):
        self.energia -= 2
        escrever_rpg("Você tentou fugir e consumiu 2 de energia\n")
        self.relogio.passaTempo(dado(15))

    def comer(self):
        if self.vida <= 90:
            self.vida += 10
            escrever_rpg(f"Você consumiu 1 porção de comida e recuperou 10 de vida.\n")
        elif self.vida == 100:
            escrever_rpg("Você consumiu 1 porção de comida.\nSua vida ja está no máximo.\n\n")
        elif 91 < self.vida < 100:
            escrever_rpg(f"Você consumiu 1 porção de comida e recuperou {100 - self.vida} de vida.\n\n")
            self.vida += 10
        self.inventario.comida -= 1
        if self.vida > 100:
            self.vida = 100
        self.relogio.passaTempo(dado(120, 30))

    def tomarRemedio(self):
        if self.inventario.medicamento > 0:
            if self.infectado == True:
                self.infectado = False
                self.inventario.medicamento -= 1
                escrever_rpg("Você consumiu 1 medicamento e deteve a infecção.\n")
            else:
                escrever_rpg(
                    "Você consumiu 1 medicamento mas não surtiu efeito pois você já estava saudável.\n")
            self.inventario.medicamento -= 1
        elif self.inventario.medicamento <= 0:
            escrever_rpg(
                    "Você não tem mais medicamentos.\nVá até um Hospital procurar.\n")
        self.relogio.passaTempo(10)
        

    def locomover(self, lugar):
        if self.inventario.combustivel == 0:
            self.energia -= 5
            deltaT = dado(360, 30)
            escrever_rpg(
                f"Você foi empurrando a moto até o {lugar} mais próximo, levou {deltaT} minutos e consumiu 5 de energia\n")
        else:
            deltaT = dado(120, 10)
            self.inventario.combustivel -= 1
            escrever_rpg(
                f"Você pegou a sua moto e pilotou até o {lugar} mais próximo, levou {deltaT} minutos e consumiu 1 gl de combustível\n")
        self.lugar = lugar
        self.relogio.passaTempo(deltaT)

    def pegarSuprimento(self, lugar):
        if lugar.nome == "Mercado":
            escrever_rpg(
                f"Você encontrou {lugar.item} un de comida e colocou na mochila\n")
            self.inventario.comida += lugar.item
        elif lugar.nome == "Hospital":
            escrever_rpg(
                f"Você encontrou {lugar.item} un de cloropina e colocou na mochila\n")
            self.inventario.medicamento += lugar.item
        elif lugar.nome == "Posto de Combustível":
            escrever_rpg(
                f"Você encontrou {lugar.item} gl de Gasolina e colocou na moto\n")
            self.inventario.combustivel += lugar.item
        elif lugar.nome == "Abrigo":
            pass
        self.relogio.passaTempo(dado(10, 2))

    def descansar(self):
        self.energia += 3
        if self.lugar != "Abrigo":
            self.inventario.comida -= 3
        if self.energia > 20:
            self.energia = 20
        self.relogio.passaTempo(360)
        escrever_rpg(
            f"Você dormiu por 8h e recuperou {3 if self.energia <= 17 else 20 - self.energia} de energia.\n")


class Zumbi:
    def __init__(self):
        self.vida = dado(30)
        self.dmg = 1

    def atacar(self, inimigo):
        inimigo.tomarDano(dado(20) * self.dmg)

    def tomarDano(self, dmg):
        self.vida -= dmg
        if self.vida < 0:
            self.vida = 0
            print("Você derrotou o zumbi.\n")


class Inventario:
    def __init__(self, combustivel, comida, medicamento):
        self.combustivel = combustivel
        self.comida = comida
        self.medicamento = medicamento
        self.municao = 10
        self.pistola = True
        self.faca = True

    def __str__(self):
        return f"Sua mochila tem:\n  Comida: {self.comida} un\n  Medicamentos: {self.medicamento} un\n  Munição: {self.municao}\n  Combustivel: {self.combustivel} gal\n  1 Faca\n  1 Pistola\n"


class Lugar:
    def __init__(self, nome):
        self.nome = nome
        self.item = 0

    def __str__(self):
        return {self.nome}

    def setLugar(self, novoLugar):
        if novoLugar != "Abrigo":
            self.item = dado(3)
        self.nome = novoLugar


l_menu = {"lugares": ["Mercado", "Hospital", "Posto de Combustível"], "armas": ["Faca", "Pistola"],
          "luta": ["Atacar", "Fugir"],
          "acoes": ["Ir para outro lugar", "Comer", "Medicar", "Descansar", "Ver Mochila", "Sair"]}

personagem = Sobrevivente(100, 1)
lugarAtual = Lugar("Abrigo")
# inicio()
while personagem.vida > 0 and personagem.relogio.dias >= 0:
    status(personagem)
    resp = menu(l_menu["acoes"])
    if resp == "Ir para outro lugar":
        resp = menu(l_menu["lugares"])
        l_menu["lugares"].append(lugarAtual.nome)
        print(l_menu["lugares"])
        personagem.locomover(resp)
        lugarAtual.setLugar(resp)
        l_menu["lugares"].remove(resp)
        print(l_menu["lugares"])
        luta(personagem)
        personagem.pegarSuprimento(lugarAtual)
    elif resp == "Comer":
        personagem.comer()
    elif resp == "Medicar":
        personagem.tomarRemedio()
    elif resp == "Descansar":
        personagem.descansar()
    elif resp == "Ver Mochila":
        personagem.getInventario()
    elif resp == "Sair":
        break
# teste git
# teste git2
# teste git3