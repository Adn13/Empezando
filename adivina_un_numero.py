

numero_a_adivinar = 13

pregunta_al_usuario = int(input('Adivina un numero del 1 al 20, tienes 3 oportunidades: '))

if pregunta_al_usuario == numero_a_adivinar:
    print('As ganado!')
else:
    segunda_pregunta = int(input('No as acertado, te quedan 2 intentos: '))

    if segunda_pregunta == numero_a_adivinar:
        print('As ganado!')
    else:
        tercera_pregunta = int(input('No as acertado, te quedan 1 intento: '))

        if tercera_pregunta == numero_a_adivinar:
            print('As ganado!')
        else:
            print('As perdido!')