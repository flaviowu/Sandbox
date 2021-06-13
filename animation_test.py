# apenas um teste de animação
# uma @ seguindo um padrão senoidal
import math
import time
 # lista de elementos a serem printados
lista1 = list(range(0, 31, 1))

# normalizamos lista1 para serem usados na função senoidal
lista2 = [x * 0.1 for x in lista1]
listaSin = []

# calculando a "altura" da @
for i in lista2:
    listaSin.append(math.sin(i))
print(listaSin)

while True:
    for i in listaSin:
        print(int(i*100) * ' ' + '@')
        time.sleep(.1)
    print('Ctrl+C para parar')
