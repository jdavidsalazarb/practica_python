def promedio(*args):

    formula = sum(args) / len(args)

    return formula


print(promedio(10,20,58,48,79,28,474,62,487))




def valores(p1,p2,p3,*args, p5):
    print(p1)
    print(p2)
    print(p3)
    print(args)
    print(p5)

print(valores(1,2,3,4,5,6,7,8,9, p5=8))




def obtenerPersona(**kwargs):
    return kwargs



print(obtenerPersona(nombre='Juan', edad=26,ciudad='Manizales'))




def combinacion(*args,**kwars):
    
    return args, kwars


print(combinacion(1,2,3,4,5,valor =[1,2,3], nombre='juan'))
