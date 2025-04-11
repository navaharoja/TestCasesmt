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

# load from elements_formularioCET.json file
elements_file = os.path.join(PROJECTPATH, 'input_data', 'elements_formularioCET.json')
with open(elements_file, 'r') as f:
    elements_formCET = json.load(f)

"""# Llamar a la función gotoMutual y obtener el driver
from utils.gotoMutual import gotoMutual
driver = gotoMutual(urlCertCloud)"""

def LlenarFormularioCET_IRLC(driver):
    try:# Ingresa los riesgos laborales y cargos
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        # Scroll hasta el elemento
        actions = ActionChains(driver)
        # Simular la tecla "TAB" 1 veces
        actions.send_keys(u'\ue004')
        actions.perform()
        
        # click en Agentes de riesgo //*[@id="agentesRiesgo"]
        xpath = elements_formCET['agentes_riesgo']['seleccionar_agentes']
        agentes_riesgo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        agentes_riesgo.click()
        # Seleccionar Agentes de riesgo
        xpath = elements_formCET['agentes_riesgo']['asma']
        asma = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        asma.click()

        # Simular la tecla "TAB" 1 veces
        actions.send_keys(u'\ue004')
        actions.perform()

        # Click en Cargos de riesgo
        xpath = elements_formCET['cargo_riesgo']['seleccionar_cargo']
        cargo_riesgo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        cargo_riesgo.click()
        # Seleccionar Cargos de riesgo
        xpath = elements_formCET['cargo_riesgo']['conductor_vehiculo_liviano']
        cargo_riesgo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        cargo_riesgo.click()

        # Simular la tecla "TAB" 1 veces
        actions.send_keys(u'\ue004')
        actions.perform()

        # Click en Condiciones de riesgo
        xpath = elements_formCET['condiciones_riesgo']['seleccionar_condiciones']
        condiciones_riesgo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        condiciones_riesgo.click()
        # Seleccionar Condiciones de riesgo
        xpath = elements_formCET['condiciones_riesgo']['certificacion_plaguicidas']
        condiciones_riesgo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        condiciones_riesgo.click()

        # Simular la tecla "TAB" 1 veces
        actions.send_keys(u'\ue004')
        actions.perform()

        # Click en Boton Siguiente 
        xpath = elements_formCET['boton_siguiente']
        boton_siguiente = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        boton_siguiente.click()     

    except Exception as e:
        print(f"Error: {e}")    

    return driver    

"""if __name__ == "__main__":
    LlenarFormularioSolicitudHoraCet(driver)
    time.sleep(5)
    driver.quit()"""
