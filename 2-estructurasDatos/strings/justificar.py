nombre = 'Soy Juan!!'

#ljust justificar a la izquierda (texto se mueve hacia la izquierda)
#rjust  justufucar a la derecha (texto se mueve hacia la derecha)
#center centrarcenter(20), 10 espacios a la izquierda, 10 espacios a la derecha

# Ejemplo: los string son inmutables, se debe almacenar a modificación del string en una nueva variable
nombre.rjust(20)

print(nombre)


nombreJustificado = nombre.center(20)


print(nombreJustificado, '.')
