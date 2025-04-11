# Description: Este script debe ejecutar los scripts SitioPublicoMutualScrab.py, SVEmpresaMutual.py y SVTrabajadorMutual.py

import time
# Guardar el tiempo de inicio
start_time = time.time()
print("------------------------------------------------------------------------") 
print(f"Inicio de ejecución - Smoke Test Mutual Cert: {time.strftime('%Y-%m-%d %H:%M:%S')}")

import SitioPublicoMutualScrab as spms
import SVEmpresaMutualScrab as svems
import SVTrabajadorMutualScrab as svtrs

# Guardar el tiempo de finalización
end_time = time.time()

# Calcular y mostrar el tiempo total de ejecución
total_time = end_time - start_time
hours, remainder = divmod(total_time, 3600)
minutes, seconds = divmod(remainder, 60)
formatted_time = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
print("------------------------------------------------------------------------") 
print(f"Tiempo total de ejecución - Smoke Test Mutual Cert: {formatted_time}")
print(f"Fecha y Hora de Finalización - Smoke Test Mutual Cert: {time.strftime('%Y-%m-%d %H:%M:%S')}")
print("------------------------------------------------------------------------") 







    

    