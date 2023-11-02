# Esta función suma dos números
def add_numbers():
    try:
        print('\nLa suma de los números ingresados es:', int(input('\nDigita el primer número a sumar: ')) + int(input('\nDigita el segundo número a sumar: ')))
    except ValueError: print('\n😯 No corazón, lo que ingresaste no es un número, intenta nuevamente mi cielo 😗')    


# Main de Python
if __name__ == "__main__":
    
    add_numbers()