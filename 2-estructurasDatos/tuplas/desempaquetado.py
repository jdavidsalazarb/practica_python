#desempaquetar tuplas, descomprimir asignar sus valores a variables

# * -> lista

#*_ -> se almacenan los valores restantes a una lista pero sin variable

#_ omitir valor


numeros = (1,10,58,45,2,3,69,7,8)

#print(len(numeros))

uno, dos, tres, cuatro, *lista = numeros


#obtener el primer valor, el cuarto valor, el secto valor y el ultimo valor desmepaquetando la tupla
uno, _,_,_,cuatro,_,seis, *lista2,ultimo = numeros

print(uno,cuatro,seis,ultimo)


print(lista2)



print(uno)
print(dos)
print(tres)
print(cuatro)
print(lista)


