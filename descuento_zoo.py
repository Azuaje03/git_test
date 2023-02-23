edad = int(input('Ingrese su edad:'))

carnet = input('Ingrese tipo de carnet (U para el carnet Universitario/ P para el carnet de Pensionado/ \
F para el carnet de Familia Numerosa/ N no tengo):')

if (18 <= edad <= 35 and carnet == 'U') or (edad <= 10) or (60 >= edad and carnet == 'P') or (carnet == 'F'):
    print('Se lleva un descuento')

else:
    print('No tiene descuento')
