lista = []
# tupla = (1, 2, 3)
# print(tupla)

numeros = [22, 51, 44, 15]
primeiro = set(numeros)
segundo = {1, 32, 15, 3, 4, 5, 6}
lista = list(segundo)
print(lista)
tupla = tuple(lista)
print(tupla)
lista2 = list(tupla)
print(lista2)

print(primeiro | segundo)#junta sem repetir valor
print(primeiro ^ segundo) #pega valores que não se repetem
print(primeiro & segundo)#pega só valores repetidos
print(primeiro - segundo)
print(segundo - primeiro)


