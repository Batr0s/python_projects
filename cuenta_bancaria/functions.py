class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, num_cuenta, balance):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance

    def depositar(self):
        deposito = 'x'
        while not deposito.isnumeric() or int(deposito) < 0:
            deposito = input('¿Cuánto dinero quieres depositar?: ')
            if not deposito.isnumeric() or int(deposito) < 0:
                print('Por favor, introduce un valor adecuado.')
        self.balance += int(deposito)

    def retirar(self):
        retiro = 'x'
        while not retiro.isnumeric() or int(retiro) < 0 or self.balance - int(retiro) < 0:
            retiro = input('¿Cuánto dinero quieres retirar?: ')
            if not retiro.isnumeric() or int(retiro) < 0:
                print('Por favor, introduce un valor adecuado.')
            elif self.balance - int(retiro) < 0:
                print('No puedes tener un balance negativo.')

        self.balance -= int(retiro)

    def __str__(self):
        return f'Nombre: {self.nombre}, apellido: {self.apellido}, cuenta: {self.num_cuenta}, balance: {self.balance}€'


def crear_cliente():
    print('A continuación vamos a crear tu cuenta bancaria. Necesitaré los siguientes datos:')
    nombre = input('Nombre: ')
    while not nombre.isalpha():
        print('Por favor, introduce un nombre correcto.')
        nombre = input('Nombre: ')

    apellido = input('Apellido: ')
    while not apellido.isalpha():
        print('Por favor, introduce un apellido correcto.')
        apellido = input('Apellido: ')

    num_cuenta = input('Número de cuenta: ')

    balance = input('Balance: ')
    while not balance.isnumeric():
        print('Por favor, introduce un balance numérico.')
        balance = input('Balance: ')
    return Cliente(nombre, apellido, num_cuenta, int(balance))


def mostrar_operaciones():
    print('[1] - Depositar dinero')
    print('[2] - Retirar dinero')
    print('[3] - Salir')


def seleccionar_operacion():
    mostrar_operaciones()
    operacion = input('Escoge la operación: ')
    while not operacion.isnumeric() or int(operacion) not in range(1, 4):
        print('ERROR, el valor introducido no es correcto.')
        mostrar_operaciones()
        operacion = input('Escoge la operación: ')
    return int(operacion)
