

def funcionA (funcionB):

    def funcionC(*args,**kwargs):

        resultado = funcionB(*args,**kwargs)

        return resultado 
    
    return funcionC


@funcionA
def suma(a,b):
    return a + b


print(suma(5,20))