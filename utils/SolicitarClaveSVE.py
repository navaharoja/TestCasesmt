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
    elements = json.load(f) 

"""# Llamar a la función gotoMutual y obtener el driver
from utils.gotoMutual import gotoMutual
driver = gotoMutual(urlCertCloud)"""

def SolicitarClaveSVE(driver):
    try:# Ingresa a la pantalla de Solicitud de Clave SVE
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        """# Scroll hasta el elemento
        actions = ActionChains(driver)
        # Simular la tecla "TAB" 3 veces
        for i in range(3):
            actions.send_keys(u'\ue004')
            actions.perform()"""
        
        # Hacer click en el boton "Sucursal Virtual"
        xpath_btnSucursalVirtual = elements['btnSucursalVirtual']['xpath']
        btnSucursalVirtual = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_btnSucursalVirtual)))
        btnSucursalVirtual.click()

        # Hacer click en el boton "Solicitar Clave SVE"
        xpath_btnSolicitarClaveSVE = elements['btnSolicitarClaveSVE']['xpath']
        btnSolicitarClaveSVE = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_btnSolicitarClaveSVE)))
        btnSolicitarClaveSVE.click()

        # Esperar 3 segundos
        time.sleep(3)

        # Pantalla de Solicitud de Clave SVE
        # Completar formulario de solitud de clave SVE

        # ingresar RUT del usuario
        xpath_rutUsuario = elements['formSolicitarClaveSVE']['rutUsuario']
        rutUsuario = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_rutUsuario)))
        rutUsuario.click() 
        rutUsuario.send_keys(elements['formSolicitarClaveSVE']['rut'])

        # Click en btnBuscarUsuario
        xpath_btnBuscarUsuario = elements['formSolicitarClaveSVE']['btnBuscarUsuario']
        btnBuscarUsuario = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_btnBuscarUsuario)))
        btnBuscarUsuario.click()

        # Bajar hasta el elemento
        #driver.execute_script("arguments[0].scrollIntoView();", btnBuscarUsuario)

        # Scroll hasta el elemento
        actions = ActionChains(driver)
        # Simular la tecla "TAB" 3 veces
        for i in range(7):
            actions.send_keys(u'\ue004')
            actions.perform()



        # Esperar 3 segundos
        time.sleep(3)

        # Seleccionar Cargo
        xpath_cargo = elements['formSolicitarClaveSVE']['Cargo']['xpath']
        cargo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_cargo)))
        cargo.click()
        
        xpath_cargoOption = elements['formSolicitarClaveSVE']['Cargo']['Analista']
        cargoOption = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_cargoOption)))
        cargoOption.click()

        # Ingresar Rut empresa
        xpath_rutEmpresa = elements['formSolicitarClaveSVE']['rutEmpresa']
        rutEmpresa = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_rutEmpresa)))
        rutEmpresa.click()

        rutEmpresa.send_keys(elements['formSolicitarClaveSVE']['rutEmpresa'])

        # Click en btnBuscarEmpresa
        xpath_btnBuscarEmpresa = elements['formSolicitarClaveSVE']['btnBuscarEmpresa']
        btnBuscarEmpresa = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_btnBuscarEmpresa)))
        btnBuscarEmpresa.click()

        # Esperar 3 segundos
        time.sleep(3)        

    except Exception as e:
        print(f"Error: {e}")    

    return driver    

"""if __name__ == "__main__":
    LlenarFormularioSolicitudHoraCet(driver)
    time.sleep(5)
    driver.quit()"""
