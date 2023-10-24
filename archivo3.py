#Esta función suma dos números
def add_numbers():
    try:
        print('\nLa suma de los números ingresados es:', int(input('\nDigita el primer número a sumar: ')) + int(input('\nDigita el segundo número a sumar: ')))
    except ValueError: print('\nRecuerda la función solo suma números!')    

add_numbers()