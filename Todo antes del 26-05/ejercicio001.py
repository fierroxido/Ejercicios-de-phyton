from ast import Lambda
from multiprocessing.sharedctypes import Value


produccion= dict(
    enero=12345,
    febrero=23456,
    marzo=45678,
    abril=56789,
    mayo=78901,
    junio=89012,
    julio=20210507,
    agosto=1223,
    septiembre=9876,
    octubre=65734,
    noviembre=10283,
    diciembre=62920   
)

pmaxi=max(produccion.keys(), key=lambda k:produccion[k])
print('El mes de mayor producción del año 2021 es: ', pmaxi,produccion[pmaxi])

pmin=min(produccion.keys(), key=lambda k:produccion[k])
print('El mes de menor producción del año 2021 es: ', pmin, produccion[pmin])

prom=tuple(produccion.values())
b=len(prom)
suma=0
for val in prom:
    suma+=val
total=suma/b
print('El promedio de producción del año 2021 es:', total)

for datos in produccion.keys():
    if (produccion[datos]>=total):
        
        print('El valor menor al promedio de la producción del año 2021 es',datos)
    else:
        print('El valor menor al promedio de la produccion del año 2021 es', datos)




