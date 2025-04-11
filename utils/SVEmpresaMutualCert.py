from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import TimeoutException
import time
import pyautogui
import pandas as pd
import os
import requests
from comparar_tiempos_de_carga import comparar_tiempos_carga
from comparar_tiempos_de_carga import enviar_alerta
from comparar_tiempos_de_carga import eliminar_archivo_alertas
from analizar_archivos import eliminar_archivos_mas_antiguos

# Configurar la pausa entre interacciones (ajusta según tus necesidades)
PAUSE_INTERVAL_SECONDS = 150  # 2.5 minutos
# Función para mover el mouse ligeramente y mantener la pantalla activa
def keep_screen_awake():
    pyautogui.moveRel(1, 1)
    pyautogui.moveRel(-1, -1)

# Ruta al controlador de Chrome (ajusta la ruta según donde hayas descargado el controlador)
#chrome_driver_path = 'C:\\Users\\001089655\\Desktop\\Katalon_Studio_Windows_64-8.6.5\\configuration\\resources\\update\\8.6.8\\extract\\resources\\drivers\\chromedriver_win32\\chromedriver.exe'

# Especifica la ruta al ejecutable de geckodriver
#geckodriver_path = "C:\\Users\\001089655\\Desktop\\Pythons\\AutoCheckWeb\\geckodriver.exe"  # Reemplaza con la ruta real

# Configura las opciones de Firefox (puedes agregar más opciones según sea necesario)
#firefox_options = webdriver.FirefoxOptions()

# Crea la instancia del driver de Firefox
#driver = webdriver.Firefox(options=firefox_options)

# Configurar opciones de Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--headless')

# Inicializar el controlador de Chrome
driver = webdriver.Chrome(options=chrome_options)

# Guardar el tiempo de inicio
start_time = time.time()

#urlCloud = 'https://unix.dnsup.net/portal/publico/mutual/inicio/home'
#urlCloud = 'https://20.12.61.45/portal/publico/mutual/inicio/home'
urlCloud = 'https://ww3.mutual.cl/'
urlOp = 'https://www.mutual.cl/portal/publico/mutual/inicio/home'
urlCertCloud = 'https://172.177.177.139/portal/publico/mutual/inicio/home'

# Credenciales Kevin
#rutEmpresa = '172844758'
#claveEmpresa = '29Junio.'

# Credeciales Cristian
#rutEmpresa = '109121762'
#claveEmpresa = 'Mutual$194'

# Credenciales Dennys ARANGUIZ
#rutEmpresa = "190536262"
#claveEmpresa = "Mutual2024"

# Credenciales PRUEBA Cloud
#rutEmpresa = "16082254-6"
#claveEmpresa = "Mutual2024"

#user = os.getenv('VAR1')  # '172921000'
#rutEmpresa = '172921000'
#passw = os.getenv('VAR2')  # 'MUTUAL2023'
#claveEmpresa = 'MUTUAL2023'

# Credenciales Hernan
#rutEmpresa = '267068194'
#claveEmpresa = 'Mutual2024'

#Credenciales Cert
#rutTrabajadorCert = "109121762"
#claveTrabajadorCert = "Clave.4848"

# Credenciales Kevin
#rutTrabajadorCert = '172844758'
#claveTrabajadorCert = '29Junio.'

# Credenciales Cristian
rutTrabajadorCert = '109121762'
claveTrabajadorCert = 'Clave.4848'

#rutTrabajadorCert = 88029372
#claveTrabajadorCert = Abcd1234

# Si tiene mas de una empresa hay que seleccionar la empresa
empresaid = "70285100_2" # MUTUAL DE SEGURIDAD C.CH.C [2] Cristian
#empresaid =  "76498260_84321" # COMERCIAL DEXIM LTDA [84321]  Cristian Deuda Cotizaciones
#empresaid = "81458500_1" # CAMARA CHILENA DE LA CONSTRUCCION [1] Cristian
#empresaid = "69110400_68651" # ILUSTRE MUNICIPALIDAD DE TALCA [68651] Cristian
#empresaid = "97030000_15400" # BANCO DEL ESTADO DE CHILE [15400] Cristian

global file_time # Definir time para el nombre del archivo

print(f"Inciando proceso - Sucursal Virtual Empresa Mutual...")

# Obtener la ruta del directorio del script actual
global script_directory
script_directory = os.path.dirname(os.path.realpath(__file__))

def loginMutualSVEmpresa(urlMutual, rutEmpresa, claveEmpresa):

    # Verificar si la ventana del navegador ya esta abierta
    if driver.current_url != "data:,":
        # abrir nueva pestaña
        driver.execute_script("window.open('', '_blank');")
        # Cambiar a la nueva pestaña
        driver.switch_to.window(driver.window_handles[1])

    # Maximizar la ventana del navegador
    driver.maximize_window()
    # Navegar a la URL especificada
    driver.get(urlMutual)

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
try:
    # Iniciar sesión en la Sucursal Virtual Empresa Mutual
    #loginMutualSVEmpresa(urlCloud, rutEmpresa, claveEmpresa)
    #loginMutualSVEmpresa(urlOp, rutEmpresa, claveEmpresa)
    loginMutualSVEmpresa(urlCertCloud, rutTrabajadorCert, claveTrabajadorCert)

    # Aqui comienzan las acciones en la Sucursal Virtual Empresa Mutual

    # Unir la ruta del directorio con el nombre del archivo
    archivo_excel = os.path.join(script_directory, "URLs.xlsx")

    prdCloud = "EMPprdCloud" # Nombre de la hoja de Excel
    prdOp = "EMPprdOp" # Nombre de la hoja de Excel
    prdCertCloud = "EMPcertCloud" # Nombre de la hoja de Excel

    # Lista para almacenar URLs que muestran el modal
    urls_con_modal = []

    # Lee las urls del archivo Excel
    #df = pd.read_excel(archivo_excel, sheet_name=prdCloud)
    #df = pd.read_excel(archivo_excel, sheet_name=prdOp)
    df = pd.read_excel(archivo_excel, sheet_name=prdCertCloud)

    # Obtiene la columna 'URL' como una lista de Python
    lista_urls = df['URL'].tolist()

    # lista de URLs y tiempo de carga
    tiempos_carga = []

    # Recorrer la lista de URLs
    for url in lista_urls:
        # Mantener la pantalla activa
        keep_screen_awake()
        # Abrir nueva pestaña
        driver.execute_script("window.open('', '_blank');")
        # Obtener identificadores de ventanas abiertas
        handles = driver.window_handles
        # Contar el número de pestañas abiertas
        num_pestañas = len(handles)-1
        # Cambiar a la nueva pestaña
        driver.switch_to.window(driver.window_handles[num_pestañas])

        # Obtener el tiempo de carga
        start_load = time.time()
        # Navegar a la URL en la nueva pestaña
        driver.get(url)
        end_load = time.time()
        load_time_url = end_load - start_load
        #print(f"URL: {url}, Load Time: {load_time_url} seconds")
        #tiempos_carga.append([url, load_time_url])

        # Establecer el nivel de zoom al XX% (puedes ajustar el valor según tus necesidades)
        zoom_level = "document.body.style.zoom='70%'"
        driver.execute_script(zoom_level)
        time.sleep(3)  # Esperar 3 segundos

        response = requests.get(url, verify=False)
        response.raise_for_status()  # Genera una excepción si hay un error HTTP


        # Imprimir el título de la página, la URL actual y el código de estado
        print(f"URL: {url}" + " - " + "Titulo: " + driver.title + " - " + "Status: " + str(response.status_code) + " - " + "Load Time: " + str(load_time_url) + " seconds")

        # Puedes realizar más verificaciones en la nueva pestaña si es necesario

        # Agregar la URL y el tiempo de carga a la lista
        tiempos_carga.append([url, load_time_url, driver.title, response.status_code])

        # Cerrar la nueva pestaña
        driver.close()

        # Cambiar de nuevo a la primera pestaña
        driver.switch_to.window(driver.window_handles[0])

    # mostrar cantidad de urls revisadas
    print("------------------------------------------------------------------------")
    print(f"URLs revisadas: {len(tiempos_carga)}")
    # urls con status 200
    urls_200 = [url for url, load_time, title, status in tiempos_carga if status == 200]
    print(f"URLs con status 200: {len(urls_200)}")
    # urls con status diferente a 200
    urls_no_200 = [url for url, load_time, title, status in tiempos_carga if status != 200]
    print(f"URLs con status diferente a 200: {len(urls_no_200)}")
    # imprimir urls con status diferente a 200
    print(f"{urls_no_200}")
    print("------------------------------------------------------------------------")      
        
    # Crear un DataFrame a partir de los resultados
    #df = pd.DataFrame(tiempos_carga, columns=["URL", "Load Time", "Title", "Status"])

    # Escribir el DataFrame a un archivo Excel
    print(f"Writing results to navigation_load_times.xlsx")    
    #df.to_excel("EMPRESA_navigation_load_times.xlsx", index=False)      

    #Definir time para el nombre del archivo
    file_time = str(time.strftime("%Y%m%d%H%M"))

    # Crear un DataFrame a partir de los resultados
    df = pd.DataFrame(tiempos_carga, columns=["URL", "Load Time", "Title", "Status"])
    print(f"Generating .CSV File: EMPRESA_navigation_load_times {file_time}.csv")
    df.to_csv(f"EMPRESACERT_navigation_load_times {file_time}.csv", index=False)   
    #df.to_excel("EMPRESA_navigation_load_times.csv", index=False)      

    # Eliminar archivos generados mas antiguos si existen mas de 10 para cada keyword
    eliminar_archivos_mas_antiguos(script_directory, "EMPRESACERT")
    # Eliminar el archivo Alertas Tiempos de Carga si existe
    eliminar_archivo_alertas()
    # comparar tiempos de carga
    #comparar_tiempos_carga(f"EMPRESACERT_navigation_load_times {file_time}.csv", 'Tiempo Promedio de Carga Urls COMPLETO.csv')
    # Enviar alerta por correo electrónico si hay diferencias en los tiempos de carga
    #enviar_alerta()  

except Exception as e:
    print(f"Error: {e}")

finally:
    # Cerrar el navegador al finalizar
    driver.quit()

# Guardar el tiempo de finalización
end_time = time.time()

# Calcular y mostrar el tiempo total de ejecución
total_time = end_time - start_time
hours, remainder = divmod(total_time, 3600)
minutes, seconds = divmod(remainder, 60)
formatted_time = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
print("------------------------------------------------------------------------") 
print(f"Tiempo total de ejecución -  Sucursal Virtual Empresa Mutual: {formatted_time}")
print(f"Fecha y Hora de Finalización - Sucursal Virtual Empresa Mutual: {time.strftime('%Y-%m-%d %H:%M:%S')}")
print("------------------------------------------------------------------------") 

