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

"""# Llamar a la función gotoMutual y obtener el driver
from utils.gotoMutual import gotoMutual
driver = gotoMutual(urlCertCloud)"""

def NavegarAlModuloCET_SVE(driver):
    try:# Navegar al módulo CET en SVE 
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        """# Scroll hasta el elemento
        actions = ActionChains(driver)
        # Simular la tecla "TAB" 3 veces
        for i in range(3):
            actions.send_keys(u'\ue004')
            actions.perform()"""
        
        # Hacer click en la opción "CET" menu lateral izquierdo
        xpath = elements_SVE['menu_izq_CET']['xpath']
        btn_cet = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btn_cet.click()

        #  Pantalla Centro Evaluación del Trabajo CET
        xpath = elements_SVE['Centro_Evaluacion_del_Trabajo_CET']['Descargar_informes_de_Evaluacion']
        btn_descargar_informes = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btn_descargar_informes.click()

    except Exception as e:
        print(f"Error: {e}")    

    return driver    

"""if __name__ == "__main__":
    LlenarFormularioSolicitudHoraCet(driver)
    time.sleep(5)
    driver.quit()"""
