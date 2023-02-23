titulo = 'Bienvenido al conversor de monedas'
print('\n' + titulo + '\n' + '-' * len(titulo) + '\n')

dolar_a_euro = 0.95

dolar_a_libra = 0.83

dolar_a_bolivar = 20.23

pregunta = input('Que conversion desea realizar?\n'
                 'A - Convertir de dolar a euro.\n'
                 'B - Convertir de euro a dolar.\n'
                 'C - Convertir de dolar a libra.\n'
                 'D - Convertir de libra a dolar.\n'
                 'E - Convertir de dolar a bolivar.\n'
                 'F - Convertir de bolivar a dolar.\n'
                 'Respuesta:')

if pregunta == 'A':
    monto = int(input('Introduzca la cantidad de dolares a convertir:'))
    print('La cantidad en euros es:{}'.format(monto * dolar_a_euro))

elif pregunta == 'B':
    monto = int(input('Introduzca la cantidad de euros a convertir:'))
    print('La cantidad en dolares es:{}'.format(monto / dolar_a_euro))

elif pregunta == 'C':
    monto = int(input('Introduzca la cantidad de dolares a convertir:'))
    print('La cantidad en libras es:{}'.format(monto * dolar_a_libra))

elif pregunta == 'D':
    monto = int(input('Introduzca la cantidad de libras a convertir:'))
    print('La cantidad en dolares es:{}'.format(monto / dolar_a_libra))

elif pregunta == 'E':
    monto = int(input('Introduzca la cantidad de dolares a convertir:'))
    print('La cantidad en bolivares es:{}'.format(monto * dolar_a_bolivar))

elif pregunta == 'F':
    monto = int(input('Introduzca la cantidad de bolivares a convertir:'))
    print('La cantidad en dolares es:{}'.format(monto / dolar_a_bolivar))

else:
    print('No has introducido un caracter correcto.'
          'Intente de nuevo.')
