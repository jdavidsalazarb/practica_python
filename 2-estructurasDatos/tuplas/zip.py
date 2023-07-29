# Comprimir tuplas



tupla = (1,30,50,60)

lista = [20,30,40,50,48]

lista2 = [25,87,89,52,47,85]


comprimir = zip(tupla, lista, lista2)


print(comprimir)


descomprimir = tuple(comprimir)

print(descomprimir)