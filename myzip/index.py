import datetime
import os
import re
import time
import math

find_dir = os.path.join(os.getcwd(), 'unpack_project', 'Mi_Gran_Directorio')
fecha = datetime.date.today()
fechaform = fecha.strftime('%d/%m/%Y')
counter = 0
inicio = time.time()
print('--------------------------------------------')
print('Fecha de búsqueda:', fechaform, '\n')
print('ARCHIVO\t \t\tNRO SERIE')
print('-------\t \t\t---------')
patron = r'N\D{3}-\d{5}'

for directory, subdirectory, files in os.walk(find_dir):
    if files:
        for file in files:
            path = os.path.join(directory, file)
            open_file = open(path)
            content = open_file.read()
            coincidence = re.findall(patron, content)
            if coincidence:
                counter += 1
                print(file, '\t', coincidence)

final = time.time()
duracion = final - inicio
print('\nNúmeros encontrados:', counter)
print('Duración de la búsqueda:', duracion, 'segundos')
print('--------------------------------------------')
