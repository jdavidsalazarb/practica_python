persona = {
        
     'nombre': 'Juan',
     'apellido': 'Salazar',
     'edad': 26,
     'ciudad': 'Manizales'

}
           


print(persona)
print(len(persona))

del(persona['nombre'])
print(persona)
print(len(persona))

persona.pop('edad')
print(persona)
print(len(persona))

persona.clear()
print(persona)
print(len(persona))