
titulo = 'Bienvenido al test de que tan amante eres a las cotufas'

print('\n' + titulo + '\n' + '-' * len(titulo) + '\n')

puntuacion = 0

opcion = input('Pregunta 1: Si vas a ver una peli, que es lo primero que te provoca comer?\n'
               'A - Cotufas.\n'
               'B - Helado.\n'
               'C - Nada.\n'
               'Respuesta=')

if opcion == 'A':
    puntuacion += 10

elif opcion == 'B':
    puntuacion += 5

elif opcion == 'C':
    puntuacion += 0

else:
    print('Lo sentimos, solo puesdes responder con los caracteres A, B, C.')

opcion = input('\nPregunta 2: Si en una fiesta hay cotufas y/o entre otros aperitivos, cual probarias primero?\n'
               'A - Las cotufas.\n'
               'B - Cualquier otro aperitivo y segundo las cotufas.\n'
               'C - No me anima nada.\n'
               'Respuesta=')

if opcion == 'A':
    puntuacion += 10

elif opcion == 'B':
    puntuacion += 5

elif opcion == 'C':
    puntuacion += 0

else:
    print('Lo sentimos, solo puesdes responder con los caracteres A, B, C.')

opcion = input('\nPregunta 3: Segun tu opinion, cuanto te gustan las cotufas?\n'
               'A - Nada.\n'
               'B - Poco.\n'
               'C - Mucho.\n'
               'D - Bastante.\n'
               'Respuesta=')

if opcion == 'A':
    puntuacion += 0

elif opcion == 'B':
    puntuacion += 5

elif opcion == 'C':
    puntuacion += 10

elif opcion == 'D':
    puntuacion += 15

else:
    print('Lo sentimos, solo puesdes responder con los caracteres A, B, C.')


if puntuacion >= 35:
    print('Felicidades, te encantan las cotufas!!')

elif (puntuacion <= 34) and (puntuacion >= 11):
    print('Felicidades, no te gusta mucho las cotufas.')

elif (puntuacion <= 10) and (puntuacion >= 1):
    print('Felicidades, no eres tan fan de las cotufas.')

elif puntuacion == 0:
    print('No te gusta para nada las cotufas.')
