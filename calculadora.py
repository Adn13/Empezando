
pregunta_operacion = input('Que operacion quieres realizar? (Multiplicar / Divir / Sumar / Restar)')

resultado = 0

primer_numero = int(input('Cual es el primer numero?'))

segundo_numero = int(input('Cual es el segundo numero?'))

if pregunta_operacion == 'Multiplicar':
    resultado = primer_numero * segundo_numero

elif pregunta_operacion == 'Dividir':
    resultado = primer_numero / segundo_numero

    if resultado == type(int):
        resultado = int(resultado)

    elif resultado == type(float):
        resultado = float(resultado)

elif pregunta_operacion == 'Sumar':
    resultado = primer_numero + segundo_numero

elif pregunta_operacion == 'Restar':
    resultado = primer_numero - segundo_numero

print('Tu resultado es {}'.format(resultado))


