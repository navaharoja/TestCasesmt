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

# load from elements_formularioCET.json file
elements_file = os.path.join(PROJECTPATH, 'input_data', 'elements_SVE.json')
with open(elements_file, 'r') as f:
    elements_SVE = json.load(f)

def BuscarInformesDeEvaluacion_Indiv_SVE(driver):
    try:# Pantalla Descargar Informes de Evaluación 
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        """# Scroll hasta el elemento
        actions = ActionChains(driver)
        # Simular la tecla "TAB" 3 veces
        for i in range(3):
            actions.send_keys(u'\ue004')
            actions.perform()"""
        
        # Informes de Evaluación Individual
        # Buscar el elemento "Datos del Trabajador"
        xpath = elements_SVE['form_Descargar_informes_de_Evaluacion']['Datos_del_Trabajador']
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()

        # Ingresar el RUT del trabajador
        rut_trabajador = elements_SVE['form_Descargar_informes_de_Evaluacion']['rut_trabajador']['rut_2']
        element.send_keys(rut_trabajador)
        time.sleep(5)

        actions = ActionChains(driver)
        actions.send_keys(u'\ue004') # Simular la tecla "TAB"
        actions.perform()

        time.sleep(5)

        # Buscar el elemento "Buscar"
        xpath = elements_SVE['form_Descargar_informes_de_Evaluacion']['btn_Buscar']
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()

        time.sleep(10)

        # Simular la flecha abajo
        actions = ActionChains(driver)
        actions.send_keys(u'\ue015') # Simular la tecla "DOWN"
        actions.perform()

        # Scroll hasta el elemento //*[@id="viewns_Z7_JAA62IG0LOKDA0QCG9LF3408T5_:formulariocet:resultadoIndividual"]/h1
        # Bajar hasta el elemento
        driver.execute_script("arguments[0].scrollIntoView();", element)
        # wait 3 seconds
        time.sleep(3)

        # Hacer click en el checkbox de seleccion
        xpath = elements_SVE['form_Descargar_informes_de_Evaluacion']['check_Listado_de_Informes']
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()

        time.sleep(5)

        # Hacer click en el boton "Descargar Seleccionados"
        xpath = elements_SVE['form_Descargar_informes_de_Evaluacion']['btn_Descargar_Seleccionados']
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()

    except Exception as e:
        print(f"Error: {e}")    

    return driver    

"""if __name__ == "__main__":
    LlenarFormularioSolicitudHoraCet(driver)
    time.sleep(5)
    driver.quit()"""
