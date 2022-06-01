#realizar un programa que tenga definido el saldo en cuanta de ahorros 1000 y en cuenta de inversion
# el valor de 25000, se debe validar el tipo de cuenta, y asi poder soliciatr al usuario a retirar
#se debe tener en cuenta que  para cuenta de ahorros no puede queda un saldo menor que 500 y en inversion 
#un saldo menor que 10000, si se solicita un valor mayor al depositov debe generar un mensaje de retiro no autorizado.

print("\t.:!!! Banco sofia SAS:. !!!")

salAhor=1000
salInver=25000
tipoCuenta=int(input('digite tipo de cuenta 1.Ahorros  2.Inversion  3.salir  :'))
while tipoCuenta !=3:
    if tipoCuenta==1:
        if salAhor==1000:
            retiro=int(input('digite valor a retirar: '))
            saldoActual=salAhor-retiro
            if saldoActual<=500:
                print('retiro no autorizado')
            else:
                print('retiro autorizado')
                print('el saldo es: ',saldoActual)
    if tipoCuenta==2:           
        if salInver==25000:
            retiro=int(input('digite valor a retirar: '))
            saldoActual=salInver-retiro
            if saldoActual<=10000:
                print('retiro no autorizado')
            else:
                print('retiro autorizado')
                print('el saldo es: ',saldoActual)
    break         

print('VUELVA PRONTO')