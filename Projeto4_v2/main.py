import human
import item
from time import sleep

personagem = human.Survivor(50, 1)
zombio = human.Zombie(50, 10)
i = 0
while personagem.isAlive() == True:
    print("--==--")
    i += 1
    print(f"O Zumbi te atacou {i}x")
    zombio.atack(personagem)
    print(f"Vc após ser atacado: {personagem}")
    personagem.comer()
    print(f"Vc após comer: {personagem}")
    print(f"Zumbi: {zombio}")
    sleep(1)
