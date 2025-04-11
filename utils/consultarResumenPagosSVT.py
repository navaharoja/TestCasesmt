import time
import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Define the project path
PROJECTPATH = os.path.dirname(__file__)

#urlCertCloud = 'https://172.177.177.139/portal/publico/mutual/inicio/home'

# Load from data.json file
data_file = os.path.join(PROJECTPATH, 'input_data', 'data.json')
with open(data_file, 'r') as f:
    data = json.load(f)

urlCertCloud = data['urlCertCloud']

#Load elements from elements.json file
elements_file = os.path.join(PROJECTPATH, 'input_data', 'elements.json')
with open(elements_file, 'r') as f:
    elements_Menu = json.load(f) 

# load from elements_SVT.json file
elements_file = os.path.join(PROJECTPATH, 'input_data', 'elements_SVT.json')
with open(elements_file, 'r') as f:
    elements_SVT = json.load(f)

"""# Llamar a la función gotoMutual y obtener el driver
from utils.gotoMutual import gotoMutual
driver = gotoMutual(urlCertCloud)"""

def consultarResumenPagosSVT(driver):
    try:# Ingresa los riesgos laborales y cargos
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        """# Scroll hasta el elemento
        actions = ActionChains(driver)
        # Simular la tecla "TAB" 3 veces
        for i in range(3):
            actions.send_keys(u'\ue004')
            actions.perform()"""
        
        # Confirmación_solicitud_hora_CET

        # pantala de Confirmación
        xpath = elements_SVT['menu_izq']['options_buttons']['Consulta_pago_Licencias']
        opcion_menu_izq = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        opcion_menu_izq.click()
        # esperar 3 segundos
        time.sleep(3)

        # pantalla "INFORME DE PAGOS"

        

    except Exception as e:
        print(f"Error: {e}")    

    return driver    

"""if __name__ == "__main__":
    LlenarFormularioSolicitudHoraCet(driver)
    time.sleep(5)
    driver.quit()"""
