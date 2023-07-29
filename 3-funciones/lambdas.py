# las labmda función o conocinas tambien como funciones anonimas
# función expresada en una sola linea de codigo, realizan tareas pequeñas, no poseen nombres


# parametros, variables que se utilizan en la defición de una función

# argumentos, valores reales que se dan a las variables de una función cuando se llama

farenheit = lambda grados : grados * 1.8 + 32

corte = lambda calificacion : 'Aprobaste' if calificacion == 10 else 'Reprobaste'


"""
sin parametros = lambda  : true

paramtros con valor default = lambda n1=2, n2=3, n3=5 : n1 + n2 + n3

*args =   labmda *args = sum(args)

**kwars = labmda *kwars = sum(kwars)
"""


print(farenheit(10))
print(corte(5))