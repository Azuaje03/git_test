input('\nAVISO:"HAY DESCUENTO ACTIVO CON SOLO TENER A DISPOSICION".\
\n\nCarnet Universitario, valido para edades entre los "18" y "35".\
\nCarnet Pensionado, valido para edades mayores a "60".\
\nCarnet Familia Numerosa, valido para todas las edades.\
\n\nENTER PARA CONTINUAR:')

edad = int(input('\nIngrese su edad:'))
flag = 0

if ( 18 <= edad <= 35):
    print('\nSi optas por el carnet Universitario, ingresa el caracter (U)\
          \n\nSi no tienes el carnet, ingrasa el caracter (N)')
    flag = 1

if 10 <= edad:
    print('\nSi optas por el carnet Familia Numerosa, ingresa el caracter (F)\
              \n\nSi no tienes el carnet, ingrasa el caracter (N)')
    flag = 1

if 60 <= edad:
    print('\nSi optas por el carnet Pensionado, ingrsa el caracter (P)\
                  \n\nSi no tienes el carnet, ingrasa el caracter (N)')
    flag = 1

if flag == 0:
    print('\nNo tiene el descuento.')

if flag == 1:

    descuento = input('\nSi dispones del carnet, ingresar dicho caracter:')

    if (18 <= edad <= 35 and descuento == 'U') or (60 >= edad and descuento == 'P') or (descuento == 'F'):
        print('\nSi tiene el descuento')

    else:
        print('\nNo tiene descuento.')
