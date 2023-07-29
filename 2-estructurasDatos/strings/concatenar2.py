nombres = 'Juan David'

apellidos = 'Salazar Botero'


nombreCompleto = '{} {}'.format(nombres,apellidos)


nombreCompleto2 = '{apellidos} {nombres}'.format(

nombres = nombres,
apellidos = apellidos

)


print(nombreCompleto2)