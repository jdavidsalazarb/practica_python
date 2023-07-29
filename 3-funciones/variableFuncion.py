

def conversionGrados(grados):
        
        farenheit = grados * 1.8 + 32 
     
        return farenheit



# podemos asignar una función a una variable esto es conocido como ciudadanos de primera clase
#argumentos para otras funciones, funciones pueden retornar funciones

gradosFarenheit = conversionGrados



print(gradosFarenheit(80))