import random

while len(lista)< 6:
    aleatorio = random.randint(1,60)
    if aleatorio not in lista:
        lista.append(aleatorio)
print(lista)

 x = [random.randint(1,60) for p in range(0, 6)]
print(x)
