# keys
# values
#items



persona = {
     
      'nombres': 'Juan David',
      'apellidos': 'Salazar Botero',
      'edad': 26,
      'pais': 'Colombia',
      'ciudad': 'Manizales'     

}


# Mostrar todas las llaves de un diccionario, convertirlo a tupla para que sea más facil de leer y seguro para que no se modifique
print(tuple(persona.keys()))

# Mostrar todos los valores de un diccionario
print(tuple(persona.values()))

# mostrar todos los elemtos de un diccionario tanto llaves como valores
print(tuple(persona.items()))