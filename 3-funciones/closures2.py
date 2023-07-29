def calcularimpuesto(impuesto):
    def calculartotal(valor):
        valorImpuesto = valor * impuesto
        valorTotal = valor + valorImpuesto
        resultado = f'El valor total a pagar es {valorTotal}'
        return  resultado

    return calculartotal                          
    


calcularImpuestoColombia = calcularimpuesto(0.19)

total = calcularImpuestoColombia(50000)

print(total)



