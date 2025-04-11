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

def loginSVEMutual(driver, rutEmpresa, claveEmpresa, empresaid):
    # Esperar a que el Boton de Sucursal Virtual sea visible
    dropdown_button = WebDriverWait(driver, 1).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="dropdownMenuButton"]'))
    )

    # Hacer clic en el botón de Sucursal Virtual
    dropdown_button.click()

    try:
        # Esperar a que el campo Ingrese su rut sea visible y pueda ser interactuado
        input_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="viewns_Z7_JAA62IG0LORS30Q42FG62KJES3_:j_id_4:rutCompany"]'))
        )

        # Ingresar Rut Empresa
        input_element.send_keys(rutEmpresa)
    except:
        # Esperar a que el campo Ingrese su rut sea visible y pueda ser interactuado
        input_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="viewns_Z7_JAA62IG0LORS30Q42FG62KJES3_:ns_Z7_JAA62IG0LORS30Q42FG62KJES3_j_id1356445198_50d9b63a:rutCompany"]'))
        )                           

        # Ingresar Rut Empresa
        input_element.send_keys(rutEmpresa)

    try:
        # Esperar a que el campo Ingrese su clave sea visible y pueda ser interactuado
        input_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="viewns_Z7_JAA62IG0LORS30Q42FG62KJES3_:j_id_4:passCompany"]'))
        )

        # Ingresar Clave Empresa
        input_element.send_keys(claveEmpresa)
    except:
        # Esperar a que el campo Ingrese su clave sea visible y pueda ser interactuado
        input_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="viewns_Z7_JAA62IG0LORS30Q42FG62KJES3_:ns_Z7_JAA62IG0LORS30Q42FG62KJES3_j_id1356445198_50d9b63a:passCompany"]'))
        )

        # Ingresar Clave Empresa
        input_element.send_keys(claveEmpresa)

    try:
        # Inspecionar el botón de Ingresar
        input_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="viewns_Z7_JAA62IG0LORS30Q42FG62KJES3_:j_id_4:ingresoEmpresas"]'))
        )

        # Hacer clic en el botón de Ingresar
        input_element.click()
    except:
        # Inspecionar el botón de Ingresar
        input_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="viewns_Z7_JAA62IG0LORS30Q42FG62KJES3_:ns_Z7_JAA62IG0LORS30Q42FG62KJES3_j_id1356445198_50d9b63a:ingresoEmpresas"]'))
        )

        # Hacer clic en el botón de Ingresar
        input_element.click()


    try:
        # Seleccionar Empresa del Dropdown
        dropdown = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="viewns_Z7_JAA62IG0LORS30Q42FG62KJES3_:formSeleccionEmpresaMutual"]/div[1]/div[1]/div/i'))
        )                                          

        # Hacer clic en el elemento para abrir el dropdown
        dropdown.click()

        # Esperar a que el elemento específico en el dropdown sea clickable
        elemento_especifico = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, f'//div[@class="item" and @data-value="{empresaid}"]'))
        )

        # Hacer clic en el elemento específico del dropdown
        elemento_especifico.click()

        # Click en el boton Continuar
        continuar = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="viewns_Z7_JAA62IG0LORS30Q42FG62KJES3_:formSeleccionEmpresaMutual"]/div[1]/div[4]/button'))
        )

        # Hacer clic en el botón Continuar
        continuar.click()

    except Exception as e:
        print(f"Error: {e} - No selecciona Empresa")    

    # Logueado en la Sucursal Virtual Empresa Mutual

    try:    # Esperar a que el elemento Tour Virtual esté presente y visible
        elemento_a_verificar = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[5]/div/header/button'))
        )
        # Hacer clic en el elemento
        elemento_a_verificar.click()
    except:
        print("No se encontró el elemento Tour Virtual.")

    return driver        

"""if __name__ == "__main__":
    loginSVEMutual(driver)
    time.sleep(5)
    driver.quit()"""








