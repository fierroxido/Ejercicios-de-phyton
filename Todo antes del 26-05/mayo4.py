#Ejercicio 4
lista=[]
for x in range (20):
    valor=int(input('Digite un número: '))
    lista.append(valor)
    if lista[x]<0:
        lista[x]=int(input('Escriba un número con valores positivos: '))
print(lista)