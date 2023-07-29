class Circulo():
      
      pi = 3.1416
      
      @classmethod
      def Area(cls,radio):
            
            return cls.pi * (radio ** 2)



resultado = Circulo.Area(14)

print(resultado)


