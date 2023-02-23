titulo = 'Bienvenido al test para elegir tu smartphone indicado'
print('\n' + titulo + '\n' + '-' * len(titulo) + '\n')

pregunta1 = input('Que tipo de software prefieres para tu nuevo smartphone?\n'
                  'A - Android.\n'
                  'B - Ios.\n'
                  'Respuesta:')

if pregunta1 == 'A':
    pregunta2 = input('Tienes suficiente presupuesto?\n'
                      'A - Mucho.\n'
                      'B - No mucho.\n'
                      'Respuesta:')
    if pregunta2 == 'B':
        print('Al tener poco presupuesto, te recomiendo un smartphone chino por 100$.')

    elif pregunta2 == 'A':
        pregunta3 = input('Te importa que el smartphone cuente con buenas camaras?\n'
                          'A - Si me importa.\n'
                          'B - No me importa.\n'
                          'Respuesta:')

        if pregunta3 == 'A':
            print('Si te importa tener una buena camara, te recomiendo que optes por un Google Pixel.')

        elif pregunta3 == 'B':
            print('Si no te importa tener una buena camara, te recomiendo que optes por un calidad precio como un '
                  'Xiaomi.')
        else:
            print('No elegistes un caracter correcto.')

    else:
        print('No elegistes un caracter correcto.')

elif pregunta1 == 'B':
    pregunta4 = input('Tienes suficiente presupuesto?\n'
                      'A - Mucho.\n'
                      'B - No mucho.\n'
                      'Respuesta:')

    if pregunta4 == 'A':
        print('Al tener suficiente presupuesto, te recomiendo un Iphone 14 Pro Max.')

    elif pregunta4 == 'B':
        print('Al tener poco presupuesto, te recomiendo un Iphone de segunda mano.')

    else:
        print('No elegistes un caracter correcto.')

else:
    print('No elegistes un caracter correcto.')
