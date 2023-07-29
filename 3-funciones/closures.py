def saludar(nombre):
     
    mensaje = f'Hola ,{nombre} ¿Cómo estás?'

    def llamado():

        print(mensaje)

    return llamado



persona = 'Juan David'


respuesta = saludar(persona)



