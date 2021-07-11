
# List comprehension
from random import randrange

# Multiplica todos os valores por 2 um a um
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
newList = [valor*2 for valor in list]
print(f"Lista: {list}")
print(f"Nova Lista: {newList}")
print ("=-"*20)

# Executa um oeração caso condição atendida
list1 = [randrange(1, 100, 1) for i in range(10)]
newList1 = [v/2 for v in list1 if v >= 27]
print(f"Lista 1: {list1}")
print(f"Nova Lista 1: {newList1}")
print ("=-"*30)

# Pega o valor da tupla se for par
fonte = (10, 25, 62, 11, 27, 67, 96, 47)
res = [i for i in fonte if i % 2 == 0]
print(f"Tupla: {fonte}")
print(f"Lista: {res}")
print ("=-"*20)

