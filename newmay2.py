ciudades=dict(
    ibague=541101,
    bogota=7900.000,
    armenia=2963.000,
    neiva=488927,
    popayan=270000,    
)
print(ciudades)

for word in ciudades.keys():
    print('Las ciudades son',word)

for dato in ciudades.values():
    print('La población de las ciudades son:',dato)

for palabra,datos in ciudades.items():
    print(f'{palabra}:{datos}')
    
