persona = {

    'nombres': 'Juan David',
    'apellidos': 'Salazar Botero',
    'edad': 25


}


persona['ciudad'] = 'Manizales'
persona['edad'] = 26

# obtener el valor de una llave por medio de get
valor = persona.get('nombres')

print(valor)

# obtener el valor de una llave por medio de setdefault, en caso de que no exista se crea la llave con el valor del segundo parametro de la función
print(persona.setdefault('nombres', 'Desempleado' ))

print(persona)