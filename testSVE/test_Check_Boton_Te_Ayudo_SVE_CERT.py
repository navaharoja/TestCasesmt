import csv
import os
import sys
import time
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define el directorio base del proyecto
SCRIP_PATH = os.path.dirname(__file__)
PROJECTPATH = os.path.dirname(SCRIP_PATH)

# Agrega la ruta de 'utils' al sys.path
utils_path = os.path.join(PROJECTPATH, 'utils')
sys.path.append(utils_path)

# Nombre del Test
test_name = "Smoke Test Recorrido Web SV Empresa - Mutual.cl"

# Cargar datos desde JSON
data_file = os.path.join(PROJECTPATH, 'utils/input_data', 'data.json')
with open(data_file, 'r') as f:
    data = json.load(f)

urlCertCloud = data['urlCertCloud']

# Definir credenciales
usuario = 'Dennys'  # Puedes cambiar el usuario aquí
usuario = 'Cristian'

rutEmpresa = data['rutEmpresaCert'][usuario]
claveEmpresa = data['claveEmpresaCert'][usuario]

# Seleccionar empresa
empresa = "MUTUAL"
empresaid = data['empresaid'][empresa]

# Cargar XPATH del botón desde JSON
elements_file = os.path.join(PROJECTPATH, 'utils/input_data', 'elements.json')
with open(elements_file, 'r') as f:
    data = json.load(f)

btnTeAyudo = data['xpathbtnTeAyudo']  # XPATH del botón

# Cargar URLs desde Excel
archivo_excel = os.path.join(PROJECTPATH, 'utils', 'URLs.xlsx')
df = pd.read_excel(archivo_excel, sheet_name="EMPcertCloud")
lista_urls = df['URL'].tolist()

# Listas para guardar resultados
resultados = []

# Archivo de salida CSV
archivo_salida = os.path.join(PROJECTPATH, 'utils', 'output_data', 'Verif_Boton_TeAyudo_SVE_Cert.csv')


# Función para verificar si el modal de contingencia está presente y cerrarlo
def cerrar_modal_contingencia(driver):
    try:
        modal_cierre = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btnCierreModalPersonalizado"))
        )
        if modal_cierre.is_displayed():
            modal_cierre.click()
            print("🔴 Modal de contingencia detectado y cerrado.")
            time.sleep(2)  # Esperar un poco para que el modal desaparezca
    except:
        print("✅ No se detectó ningún modal de contingencia.")


# Función para verificar si el botón 'Te Ayudo' está presente
def verificar_boton_visible(driver, url):
    """Verifica si el botón está visible en la página dada."""
    try:
        # Intentar cerrar modal antes de buscar el botón
        cerrar_modal_contingencia(driver)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "QSIFeedbackButton-btn"))
        )
        print(f"✔ El botón está visible en: {url}")
        return "Si"
    except:
        print(f"✘ El botón NO está visible en: {url}")
        return "No"


if __name__ == "__main__":
    print(f"Iniciando el test: {test_name}")

    # 1 - Llamar a la función gotoMutual para iniciar WebDriver
    from gotoMutual import gotoMutual
    driver = gotoMutual(urlCertCloud)

    # 2 - Llamar a la función loginSVEMutual para autenticarse
    from loginSVEMutual import loginSVEMutual
    driver = loginSVEMutual(driver, rutEmpresa, claveEmpresa, empresaid)

    # Guardar la pestaña principal
    main_window = driver.current_window_handle

    # 3 - Recorrer las URLs
    for url in lista_urls:
        # Abrir nueva pestaña y cambiar a ella
        driver.execute_script("window.open('', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(url)
        time.sleep(5)  # Dar tiempo para cargar la página

        # Verificar si el botón está visible
        resultado = verificar_boton_visible(driver, url)
        titulo = driver.title
        resultados.append([url, titulo, resultado])

        # Cerrar la pestaña actual y volver a la pestaña principal
        driver.close()
        driver.switch_to.window(main_window)

    # 4 - Guardar resultados en el archivo CSV (fuera del loop)
    os.makedirs(os.path.dirname(archivo_salida), exist_ok=True)

    with open(archivo_salida, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["URL", "Titulo", "Btn Visible"])
        writer.writerows(resultados)

    print(f"\n📄 Resultados guardados en '{archivo_salida}'")

    # 5 - Cerrar navegador
    time.sleep(5)
    driver.quit()
    print(f"Test finalizado: {test_name}")


