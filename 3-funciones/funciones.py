'''Buenas noches alguien podría ayudarme con el siguiente ejercicio de funciones?
Definir una función reciba como 
parámetro una lista de números enteros. 
La función deberá devolver la cantidad 
de números en la lista que tienen al menos 
un dígito igual a 5.
'''






def contarNumeros(numeros):
    sublistaNumero = []
    contador = 0
    for numero in numeros: 
        if '5' in str(numero): 
            sublistaNumero.append(numero)
            contador +=1
    
    return contador , sublistaNumero    





numeros = [1548,10,69,74,15,48,1555,12,47,52,47,51,5558,47455]


valor1, valor2 = contarNumeros(numeros)

print(valor1)
print(valor2)


'''
def suma():
   n1 = int(input('Ingrese el primer valor: '))
   n2 = int(input('ingrese el segundo valor: '))

   resultado = n1 + n2

   return resultado


print(suma()) 
'''