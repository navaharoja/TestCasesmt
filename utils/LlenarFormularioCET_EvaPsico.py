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

def LlenarFormularioCET_EvaPsico(driver):
    try:# Ingresa los riesgos laborales y cargos
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        # Scroll hasta el elemento
        actions = ActionChains(driver)
        # Simular la tecla "TAB" 1 veces
        actions.send_keys(u'\ue004')
        actions.perform()
        
        # Evaluaciones psicológicas
        # Click en Boton "Entendido" 
        xpath = elements_formCET['boton_entendido']
        btnEntendido = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btnEntendido.click()
        
        # Psicosensotécnico
        xpath = elements_formCET['psicosensotecnico']['seleccionar_evaluacion']
        seleccionar_evaluacion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        seleccionar_evaluacion.click()
        xpath = elements_formCET['psicosensotecnico']['sensotecnico']
        Sensotécnico = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        Sensotécnico.click()

        # Evaluaciones psicolaborales
        xpath = elements_formCET['evaluaciones_psicolaborales']['seleccionar_eval_psicolaboral']
        seleccionar_eval_psicolaboral = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        seleccionar_eval_psicolaboral.click()
        xpath = elements_formCET['evaluaciones_psicolaborales']['Evaluacion_de_Aversion_al_Riesgo']
        eval_psicolaboral = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        eval_psicolaboral.click()

        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        # Click en Boton "Siguiente"
        xpath = elements_formCET['boton_siguiente2']
        btnSiguiente = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btnSiguiente.click()

    except Exception as e:
        print(f"Error: {e}")    

    return driver    

def LlenarFormularioCET_EvaPsico_Vacio(driver):
    try:# Ingresa los riesgos laborales y cargos
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        # Scroll hasta el elemento
        actions = ActionChains(driver)
        # Simular la tecla "TAB" 1 veces
        actions.send_keys(u'\ue004')
        actions.perform()
        
        # Evaluaciones psicológicas
        # Click en Boton "Entendido" 
        xpath = elements_formCET['boton_entendido']
        btnEntendido = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btnEntendido.click()

        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        # Click en Boton "Siguiente"
        xpath = elements_formCET['boton_siguiente2']
        btnSiguiente = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btnSiguiente.click()

    except Exception as e:
        print(f"Error: {e}")    

    return driver       



"""if __name__ == "__main__":
    LlenarFormularioSolicitudHoraCet(driver)
    time.sleep(5)
    driver.quit()"""
