def funcionA(funcionB):
    
    def funcionC():
     
     print('Esto es una nueva funcionalidad')
     funcionB()
     print('Esto es otra funcionalidad')
    return funcionC    
    




@funcionA
def saludo():
   print('Hola ¿Cómo estás?')    

saludo()

@funcionA
def suma():
    print(15 + 20)

suma()

