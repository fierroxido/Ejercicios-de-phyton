
lista1=[]
lista2=[]

for usuario in range (1,21):
    usuario=int(input('Digite un valor para añadir en la lista '))
    if usuario%2==0:
        lista1.append(usuario)
    else:
        lista2.append(usuario)
print('Los elementos pares son: ',lista1)
print('Los elementos impares de la lista son: ',lista2)





