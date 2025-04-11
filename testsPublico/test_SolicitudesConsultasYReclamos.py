import time
import json
import os
import sys

# Define the project path
SCRIP_PATH = os.path.dirname(__file__)
PROJECTPATH = os.path.dirname(SCRIP_PATH)

# Agrega la ruta de 'utils' al sys.path
utils_path = os.path.join(PROJECTPATH, 'utils')
sys.path.append(utils_path)

# Test_Name
test_name = "Formulario de Solicitudes, Consultas y Reclamos"

#urlCertCloud = 'https://172.177.177.139/portal/publico/mutual/inicio/home'

# Load from data.json file
data_file = os.path.join(PROJECTPATH, 'utils/input_data', 'data.json')
with open(data_file, 'r') as f:
    data = json.load(f)

urlCertCloud = data['urlCertCloud']

#Load elements from elements.json file
elements_file = os.path.join(PROJECTPATH, 'utils/input_data', 'elements.json')
with open(elements_file, 'r') as f:
    elements_Menu = json.load(f) 

if __name__ == "__main__":
    print(f"Iniciando el test: {test_name}")
    # 1 - Llamar a la función gotoMutual y obtener el driver
    from gotoMutual import gotoMutual
    driver = gotoMutual(urlCertCloud)
    # 2 - Llamar a la funcion LlenarFormularioSCR
    from LlenarFormularioSCR import LlenarFormularioSCR
    driver = LlenarFormularioSCR(driver)

    time.sleep(5)
    driver.quit()
    print(f"Test finalizado: {test_name}")
