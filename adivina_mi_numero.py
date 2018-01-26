
numero_jugador_1 = int(input('Dime que numero quieres que adivine tu adversario (Del 1 al 20)?'))

numero_jugador_2 = int(input('Que numero crees que a puesto tu adversario? (Del 1 al 20)'))

while numero_jugador_2 != numero_jugador_1:

        print('Vuelve a probar!')
        numero_jugador_2 = int(input('Que numero crees que a puesto tu adversario? (Del 1 al 20)'))

print('You win!')

