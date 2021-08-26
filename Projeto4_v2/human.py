from time import sleep
from random import choice
import item


class Human:
    def __init__(self, life=100, dmg=1):
        self.life = life
        self.dmg = dmg
        self.alive = True
        self.infected = False
        self.backpack = item.Backpack()

    def __str__(self):
        return f"Vida: {self.getLife()}\nStatus: {'Morto' if self.isAlive() == False else 'Vivo'}"

    def getLife(self):
        return self.life

    def lifeUp(self, up):
        self.life += up

    def lifeDown(self, down):
        self.life -= down
        if self.life <= 0:
            self.dead()
            self.life = 0

    def isInfected(self):
        return self.infected

    def setInfection(self):
        self.infected = False

    def isAlive(self):
        return self.alive

    def dead(self):
        self.alive = False

    def comer(self):
        self.lifeUp(self.backpack.comida.getLife())
        self.backpack.setComida(-1)


class Survivor(Human):
    def __init__(self, life, dmg):
        super().__init__(life=life, dmg=dmg)
        self.energy = 50

    def getEnergy(self):
        return self.energy

    def energyUP(self, up=5):
        self.energy += up

    def energyDown(self, down):
        self.energy -= down


class Zombie(Human):
    def __init__(self, life, dmg):
        super().__init__(life=life, dmg=dmg)
        self.alive = False
        self.infected = True

    def atack(self, enemy):
        enemy.lifeDown(self.dmg)
        enemy.infected = choice([True, False])


# personagem = Survivor(50, 1)
# zombio = Zombie(50, 10)
# i = 0
# while personagem.isAlive() == True:
#     print("--==--")
#     i += 1
#     print(f"O Zumbi te atacou {i}x")
#     zombio.atack(personagem)
#     print(f"Vc: {personagem}")
#     print(f"Zumbi: {zombio}")
#     sleep(1)
