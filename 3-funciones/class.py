class Persona: 
   
    def __init__(self,nombres,apellidos,edad, ciudad):

        self.nombres = nombres,
        self.apellidos = apellidos, 
        self.edad = edad,
        self.ciudad = ciudad


class Trabajador(Persona):

    def Departamento(self):
    
        departamento = None
        if self.ciudad == 'Manizales':
                departamento = 'Caldas'

        return departamento
            







juan = Trabajador('Juan David', 'Salazar Botero', 26,'Manizales')
print(juan.Departamento())
print(juan.__dict__) 










