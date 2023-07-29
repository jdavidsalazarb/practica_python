# Ordernar una lista sort ascendete , parametro reserse = True descendente

numeros = [50,0,100,2,10,74,32,58,96,47,15,11,18,16,13]



# Ordenamos de forma descendente (menor a mayor)

numeros.sort()
print(numeros)

# numero menor
print(numeros[0])

# número mayor
print(numeros[-1])

# Ordnamos de forma ascendente (mayor a menor)

numeros.sort(reverse = True)
print(numeros)


# numero menor mejor función min()
print(min(numeros))


# numero mayor mejor función max()

print(max(numeros))


# las funciones que se utilizan llamano primero el objeto lista lista.sort() son funciones propiamente del objeto es decir de las listas

# Mientas que si se llama primero la función se utiliza para diferentes tipos de datos  min()


# comprobar si un número existe o no en una lista



nuevaLista = ['Juan', 'Carlos', 'Enrique']


print('juan' not in nuevaLista)