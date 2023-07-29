


def cajero(monto, saldo, tipo): 

    monto = float(monto)
    saldo = float(saldo)
    tipo = str(tipo)
    tipo = tipo.lower()

    def retiro(monto, saldo):
        if(monto <= saldo):
            return saldo - monto
        else: 
             return f'el monto supera el saldo: {saldo}'
        
    def deposito(monto, saldo):
            return saldo + monto

    
    if(tipo == 'retiro'):
         return retiro(monto,saldo)
    elif(tipo == 'deposito'):
         return deposito(monto,saldo)
    else:
         print('tipo de movimiento no disponible')
    

print(cajero(50,100,'deposito'))



