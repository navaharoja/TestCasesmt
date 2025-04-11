from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
import json

# Define the project path
PROJECTPATH = os.path.dirname(__file__)

# Load from data.json file
data_file = os.path.join(PROJECTPATH, 'input_data', 'data.json')
with open(data_file, 'r') as f:
    data = json.load(f)

"""# Credenciales para conectarse a la Sucursal Virtual Empresa Mutual
usuario = 'AndresValdes'
rutTrabajadorCert = data['rutTrabajadorCert'][usuario]
claveTrabajadorCert = data['claveTrabajadorCert'][usuario]

# Si tiene mas de una empresa hay que seleccionar la empresa
empresaid = data['empresaid'] # MUTUAL DE SEGURIDAD C.CH.C [2] Cristian"""

def loginSVTMutual(driver, rutTrabajadorCert, claveTrabajadorCert):
    
    try:
        # Esperar a que mensaje de connection sea visible
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="details-button"]')))
        # Hacer clic en el botón "Avanzado"
        driver.find_element(By.ID, 'details-button').click()
        # Esperar a que el botón "Continuar" sea visible
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="proceed-link"]')))
        # Hacer clic en el botón "Continuar"
        driver.find_element(By.ID, 'proceed-link').click()
    except TimeoutException:
        # Si no se encuentra el mensaje de conexión, continuar con el script
        pass

    # Esperar a que el Boton de Sucursal Virtual sea visible
    dropdown_button = WebDriverWait(driver, 1).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="dropdownMenuButton"]'))
    )

    # Hacer clic en el botón de Sucursal Virtual
    dropdown_button.click()

    try:
        # Esperar a que el botón de Sucursal Virtual Trabajador Mutual sea visible
        dropdown_button = WebDriverWait(driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="viewns_Z7_JAA62IG0LORS30Q42FG62KJES3_:j_id_4"]/div[1]/div[1]/a[2]'))
        )                                                             

        # Hacer clic en el botón de Sucursal Virtual trabajador Mutual
        dropdown_button.click()
    except:
        print("No se encontro el boton de Sucursal Virtual Trabajador Mutual")
        # Esperar a que el botón de Sucursal Virtual Trabajador Mutual sea visible
        dropdown_button = WebDriverWait(driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="viewns_Z7_JAA62IG0LORS30Q42FG62KJES3_:ns_Z7_JAA62IG0LORS30Q42FG62KJES3_j_id1356445198_50d9b63a"]/div[1]/div[1]/a[2]'))
        )                                                                             

        # Hacer clic en el botón de Sucursal Virtual trabajador Mutual
        dropdown_button.click()    
    try:
        # Esperar a que el campo Ingrese su rut sea visible y pueda ser interactuado
        input_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="viewns_Z7_JAA62IG0LORS30Q42FG62KJES3_:j_id_4:rutUser"]'))
        )                                          
        
        # Ingresar Rut Trabajador
        input_element.send_keys(rutTrabajadorCert)
    except:    
        # Esperar a que el campo Ingrese su rut sea visible y pueda ser interactuado
        input_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="viewns_Z7_JAA62IG0LORS30Q42FG62KJES3_:ns_Z7_JAA62IG0LORS30Q42FG62KJES3_j_id1356445198_50d9b63a:rutUser"]'))
        )                                          
        
        # Ingresar Rut Trabajador
        input_element.send_keys(rutTrabajadorCert)
    try:
        # Esperar a que el campo Ingrese su clave sea visible y pueda ser interactuado
        input_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="viewns_Z7_JAA62IG0LORS30Q42FG62KJES3_:j_id_4:passUser"]'))
        )                                          
        
        # Ingresar Clave Trabajador
        input_element.send_keys(claveTrabajadorCert)
    except:
        # Esperar a que el campo Ingrese su clave sea visible y pueda ser interactuado
        input_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="viewns_Z7_JAA62IG0LORS30Q42FG62KJES3_:ns_Z7_JAA62IG0LORS30Q42FG62KJES3_j_id1356445198_50d9b63a:passUser"]'))
        )                                          
        
        # Ingresar Clave Trabajador
        input_element.send_keys(claveTrabajadorCert)

    try:
        # Inspecionar el botón de Ingresar
        input_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="viewns_Z7_JAA62IG0LORS30Q42FG62KJES3_:j_id_4:ingresoPersonas"]'))
        )                                          

        # Hacer clic en el botón de Ingresar
        input_element.click()
    except:
        # Inspecionar el botón de Ingresar
        input_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="viewns_Z7_JAA62IG0LORS30Q42FG62KJES3_:ns_Z7_JAA62IG0LORS30Q42FG62KJES3_j_id1356445198_50d9b63a:ingresoPersonas"]'))
        )                                          

        # Hacer clic en el botón de Ingresar
        input_element.click()

    return driver        

"""if __name__ == "__main__":
    loginSVEMutual(driver)
    time.sleep(5)
    driver.quit()"""








