from functions import *

opcion = 100
while opcion != 4:
    opcion = select_option()
    match opcion:
        case 1:
            turn_farma()
        case 2:
            turn_perfum()
        case 3:
            turn_cosme()
