from os import system


def select_option():
    # Forces the user to select an option and write it in the correct format.
    # Returns the option selected
    order = 'x'
    while not order.isnumeric() or int(order) not in range(1, 5):
        print('''[1] - Farmácia
[2] - Perfumería
[3] - Cosmética
[4] - Salir                
''')
        order = input('Select the option (write the number): ')
        if not order.isnumeric() or int(order) not in range(1, 5):
            system('cls')
            print('Invalid input. Please enter a number from 1 to 4.')
    return int(order)


def decorator(function):
    result = function()

    def my_function():
        print('Su turno es: ')
        print(next(result))
        print('Aguarde y será atendido...')
    return my_function

# funciones generadoras
@decorator
def turn_farma():
    x = 1
    while True:
        yield 'F - ' + str(x)
        x += 1


@decorator
def turn_perfum():
    x = 1
    while True:
        yield 'P - ' + str(x)
        x += 1


@decorator
def turn_cosme():
    x = 1
    while True:
        yield 'C - ' + str(x)
        x += 1
