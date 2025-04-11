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
test_name = "Solicitar hora CET - Examen PreOcupacional - Con Evaluacion Psicologica"

#urlCertCloud = 'https://172.177.177.139/portal/publico/mutual/inicio/home'

# Load from data.json file
data_file = os.path.join(PROJECTPATH, 'utils/input_data', 'data.json')
with open(data_file, 'r') as f:
    data = json.load(f)

urlCertCloud = data['urlCertCloud']

if __name__ == "__main__":
    print(f"Iniciando el test: {test_name}")
    # 1 - Llamar a la función gotoMutual y obtener el driver
    from gotoMutual import gotoMutual
    driver = gotoMutual(urlCertCloud)
    # 2 - Llamar a la funcion LlenarFormularioCET_SolicitudHoraCet
    from LlenarFormularioCET_SolicitudHoraCet import LlenarFormularioCET_SolicitudHoraCet_ExPreOc
    driver = LlenarFormularioCET_SolicitudHoraCet_ExPreOc(driver)
    # 3 - Llamar a la funcion LlenarFormularioCET_IRLC
    from LlenarFormularioCET_IRLC import LlenarFormularioCET_IRLC
    driver = LlenarFormularioCET_IRLC(driver)
    # 4 - Llamar a la funcion LlenarFormularioCET_EvaPsico
    from LlenarFormularioCET_EvaPsico import LlenarFormularioCET_EvaPsico
    driver = LlenarFormularioCET_EvaPsico(driver)
    # 5 - Llamar a la funcion LlenarFormularioCET_EvalAdic
    from LlenarFormularioCET_EvalAdic import LlenarFormularioCET_EvalAdic
    driver = LlenarFormularioCET_EvalAdic(driver)
    # 6 - Llamar a la funcion LlenarFormularioCET_NomTrab
    from LlenarFormularioCET_NomTrab import LlenarFormularioCET_NomTrab_ExPreOc
    driver = LlenarFormularioCET_NomTrab_ExPreOc(driver)
    # 7 - Llamar a la funcion LlenarFormularioCET_Confirmacion
    from LlenarFormularioCET_Confirmacion import LlenarFormularioCET_Confirmacion
    driver = LlenarFormularioCET_Confirmacion(driver)

    time.sleep(5)
    driver.quit()
    print(f"Test finalizado: {test_name}")
