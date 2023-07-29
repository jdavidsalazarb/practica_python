string = 'Juan/David/Salazar/Botero'

# split convierte un string a una lista, si no tiene espacio y otro separador se pasa entre comillas en separador como parametro
stringLista = string.split('/')


# segundo parametro limitar el numero de registros a separar

stringLista2 = string.split('/',2)

print(stringLista)
print(type(stringLista))

print(stringLista2)


lista = ['Reanult', 'Mazda', 'Bmw', 'Audi']


listaString = ' '.join(lista)


print(listaString)
print(type(listaString))