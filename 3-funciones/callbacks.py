
aprobacionMateria = lambda nota : nota >= 7

promedioNotas = lambda *args : sum(args) / len(args)



def reprobacionMateria(nota):
    return nota >=7


def calificacionMateria(funAprobacion,funPromedio, *args ):

    promedio = funPromedio(*args)

    if(funAprobacion(promedio)):
        return f'Aprobado, nota final: {promedio}'
    else:
        return f'Reprobado, nota final: {promedio}'
    


print(calificacionMateria(reprobacionMateria,promedioNotas,1,1,2,1,2,2.5,3))


