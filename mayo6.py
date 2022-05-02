#ejercicio 6
a=[]
limite=int(input('Escriba el número limite de su lista'))
for i in range (limite):
    valores=int(input('Escriba los valores'))
    a.append(valores**2)
print(a)