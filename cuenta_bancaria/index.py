from functions import *

mi_cliente = crear_cliente()
print(f'Cuenta creada con éxito! {mi_cliente.__str__()}')
operacion = 100
while operacion != 3:
    print(f'Balance: {mi_cliente.balance}€')
    operacion = seleccionar_operacion()
    match operacion:
        case 1:
            mi_cliente.depositar()
        case 2:
            mi_cliente.retirar()
        case 3:
            print('Adios')
