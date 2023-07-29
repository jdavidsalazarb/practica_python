def suma(n1,n2):
    resultado = n1 + n2
    return resultado


numeroUno = int(input('ingresen el valor del primer número'))
numeroDos = int(input('ingrese el valor del segundo número'))

print(suma(numeroUno,numeroDos))



def areaCirculo(radio, pi=3.14):

    return pi * (radio ** 2)


print(areaCirculo(radio=5,pi=3.1416))