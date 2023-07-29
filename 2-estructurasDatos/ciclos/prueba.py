
numeros = [3,4,7,4,65,7,5,34,2,34,34,65,2345,5]


pares = []
impares = []

for num in numeros:
    if( num % 2 == 0):
       pares.append(num)
    else:
        impares.append(num) 


print(f'Los numeros pares son: {pares}, los numeros impares son: {impares}')


