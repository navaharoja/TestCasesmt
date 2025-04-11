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

def LlenarFormularioCET_EvalAdic(driver):
    try:# Ingresa los riesgos laborales y cargos
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        # Scroll hasta el elemento
        actions = ActionChains(driver)
        # Simular la tecla "TAB" 1 veces
        actions.send_keys(u'\ue004')
        actions.perform()
        
        # Evaluaciones adicionales
        # Click en Boton "Entendido" //*[@id="viewns_Z7_JAA62IG0LO55D0Q3QIHBBN10K1_:superFormulario:panelTipoMotivo"]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[3]/button
        xpath = elements_formCET['boton_entendido2']
        btnEntendido = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btnEntendido.click()
        
        # Otras evaluaciones
        xpath = elements_formCET['otras_evaluaciones']['seleccionar_otras_evaluaciones']
        seleccionar_otras_evaluaciones = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        seleccionar_otras_evaluaciones.click()
        xpath = elements_formCET['otras_evaluaciones']['ALCOHOL_ETILICO_EN_SANGRE']
        otras_evaluaciones = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        otras_evaluaciones.click()

        # Evaluaciones de drogas
        xpath = elements_formCET['evaluaciones_de_drogas']['seleccionar_eval_drogas']
        seleccionar_eval_drogas = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        seleccionar_eval_drogas.click()

        # Seleccionar drogas
        sustancias = [
            "Marihuana",
            #"Cocaina",
            #"Benzodiazepinas",
            #"Anfetamina",
            "Alcohol",
            #"Barbituricos",
            #"Opiaceos",
            "Metanfetaminas"
        ]
        for sustancia in sustancias:
            xpath = elements_formCET['evaluaciones_de_drogas'][sustancia]
            eval_drogas = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            eval_drogas.click()
        
        

        # Click en Boton "Siguiente"
        xpath = elements_formCET['boton_siguiente3']
        btnSiguiente = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btnSiguiente.click()

    except Exception as e:
        print(f"Error: {e}")    

    return driver

"""if __name__ == "__main__":
    LlenarFormularioSolicitudHoraCet(driver)
    time.sleep(5)
    driver.quit()"""
