import random

numero_ganador = random.randint(1, 10)
numero_elegido = int(input('Elige un numero:'))

if numero_elegido == numero_ganador:
    print('Has ganado!')

if numero_elegido > 10:
    print('Te has pasado un poco... Era entre 1 y 10.')

if numero_elegido < 1:
    print('Te has quedado corto.')

if numero_elegido == 666:
    print('Has elegido el numero de la bestia')

if numero_elegido == -666:
    print('Has elegido el numero de la bestia, pero demas en numero negativo, eso es doblemente maligno.')

if numero_elegido == 69:
    print('Has puesto el numero del sexo, goloso.')

if numero_elegido == -66:
    print('Has elegido el numero del sexo, ademas lo pusiste en negativo indica que eres alguien de poco pito.')


print('El numero ganador era:{}'.format(numero_ganador))