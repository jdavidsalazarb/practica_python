listaNombres = ['Juan', 'Camilo', 'Mariana', 'Luisa', 'Cristian', 'Elkin']


print(len(listaNombres))

listaNombres.append('Camila')
print(len(listaNombres))

print(listaNombres)


listaNombres.append('David')
print(len(listaNombres))


listaNombres.insert(0, 'Henry')

listaNombres.insert(2, 'Vanesa')

print(len(listaNombres))
print(listaNombres)


listaNombres2 = ['Luz', 'Stella', 'Omar']

listaNombres.extend(listaNombres2)


print(listaNombres)
print(len(listaNombres))





del(listaNombres[0])
del(listaNombres[-1])
print(listaNombres)
print(len(listaNombres))


listaNombres.clear()

print(listaNombres)
print(len(listaNombres))