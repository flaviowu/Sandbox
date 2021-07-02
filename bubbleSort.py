import random
from time import sleep
def bubbleSort(lista):
    for element in range(len(lista)-1,0,-1):
        for i in range(element):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                print(lista)
                sleep(1)

rand_lista = []
for i in range(0,21):
    n = random.randint(1,30)
    rand_lista.append(n)
print(rand_lista)
print(bubbleSort(rand_lista))
