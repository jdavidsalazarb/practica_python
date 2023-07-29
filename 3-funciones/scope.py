
animal = 'Gato' ## Variable global, para usar en funcion condicion o ciclo



def zoologico():
    global animal
    animal = 'Perro' # Variable local
    ubicacion = 'Pereira'
    return animal, ubicacion




print(zoologico())

