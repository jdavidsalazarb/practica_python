class Animal(): #clase padre
    def Comer(self):
          print('Llamado a la mascota a comer')

    def Dormir(self):
          print('Llamado a la mascota a dormir')


class Mascota(Animal): 
      
      def Tipo(self):
           preguntaTipo = str(input('Ingrese el tipo de Mascota: '))
           preguntaTipo = preguntaTipo.lower()
           preguntaTipo = preguntaTipo.strip()
           if(preguntaTipo=='perro' or preguntaTipo=='gato'):
                print('Este tipo de animal es permitido para ser mascota')
           else: 
                print('Tipo de animal no permitido')         


class Perro(Mascota, Animal):
       
        #clase hija
       

       
       def __init__(self, nombre):
             self.nombre = nombre

       def Comer(self):
             super().Comer()
             print(f'{self.nombre} come.')

       def Dormir(self):
             print(f'{self.nombre} duerme.')           




tayson = Perro('tayson')
tayson.Comer()
tayson.Dormir()
tayson.Tipo()



