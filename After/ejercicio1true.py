#Ejercicio bien hecho

def sueldev(salariobasico,diaslaborados):
    Sueldodev= salariobasico*diaslaborados/30
    return Sueldodev

def comimes(ventasemes):
    comisionventas=0.02*ventasmes
    return comisionventas


def tode(Totaldevengado,totaldeducciones):
    deduciones=Totaldevengado - totaldeducciones
    return deduciones
'''def sane(Totaldevengado,b):
    salarioneto= Totaldevengado - b
    return salarioneto'''

# Principal 
cd=int(input("Digite su documento de identidad: "))
salariobasico=int(input("Sueldo recibido: "))
diaslaborados=int(input("dias laborados: "))
a=sueldev(salariobasico,diaslaborados)
print(f"Su sueldo devengado es: {a}")
#ventas por mes

ventasmes=int(input("Digite el total de ventas por mes: "))
b=comimes(ventasmes)
print(f"Su comision es: {b}")

# total devengado 
Totaldevengado=a+b
print(f"El total devengado es: {Totaldevengado}")

# Total deducciones 
totaldeducciones=int(input("Digite el total de sus deducciones: "))
c=tode(Totaldevengado,totaldeducciones)
print(f"Toatl de deducciones: {c}")

#salario neto 

print(f"su salario neto es: {c}")
if c < 2000000:
     DL=(diaslaborados * 117112)/30
     fin=DL+c
     print(f"Su sueldo neto con  en el auxilio de trasporte es:{fin}") 