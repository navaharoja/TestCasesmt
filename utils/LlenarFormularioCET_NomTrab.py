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

def LlenarFormularioCET_NomTrab(driver):
    try:# Ingresa los riesgos laborales y cargos
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        # Scroll hasta el elemento
        actions = ActionChains(driver)
        # Simular la tecla "TAB" 1 veces
        actions.send_keys(u'\ue004')
        actions.perform()
        
        # Nómina de trabajadores

        # Centro de Trabajo 1
        
        # Nombre
        xpath = elements_formCET['Centro_de_Trabajo_1']['txtf_nombre']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        nombre = elements_formCET['Centro_de_Trabajo_1']['nombre']
        input_element.send_keys(nombre)

        # Direccion
        xpath = elements_formCET['Centro_de_Trabajo_1']['txtf_direccion']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        direccion = elements_formCET['Centro_de_Trabajo_1']['direccion']    
        input_element.send_keys(direccion)

        # Seleccionar region
        xpath = elements_formCET['Centro_de_Trabajo_1']['slct_region']
        select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        select_element.click()
        xpath = elements_formCET['Centro_de_Trabajo_1']['metropolitana']
        select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        select_element.click()
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        # Seleccionar provincia
        xpath = elements_formCET['Centro_de_Trabajo_1']['slct_provincia']
        select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        select_element.click()
        xpath = elements_formCET['Centro_de_Trabajo_1']['santiago']
        select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        select_element.click()
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        # Seleccionar comuna
        xpath = elements_formCET['Centro_de_Trabajo_1']['slct_comuna']
        select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        select_element.click()
        xpath = elements_formCET['Centro_de_Trabajo_1']['providencia']
        select_element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        select_element.click()
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        # Cantidad de trabajadores
        xpath = elements_formCET['Centro_de_Trabajo_1']['txtf_cantidad_trabajadores']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        cantidad_trabajadores = elements_formCET['Centro_de_Trabajo_1']['cant_trabajadores']
        input_element.send_keys(cantidad_trabajadores)

        # Click boton ingresar nomina
        xpath = elements_formCET['Centro_de_Trabajo_1']['btn_ingresar_nomina']
        btn_ingresar_nomina = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btn_ingresar_nomina.click()
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        # formulario de nomina de trabajadores
        # RUT
        xpath = elements_formCET['formulario_nomina_trabajadores']['selfRUT']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        xpath = elements_formCET['formulario_nomina_trabajadores']['opcRUT']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        xpath = elements_formCET['formulario_nomina_trabajadores']['txtfRUT']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        rut = elements_formCET['formulario_nomina_trabajadores']['RUT']
        input_element.send_keys(rut)

        # Nombre
        xpath = elements_formCET['formulario_nomina_trabajadores']['txtfNombres']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        nombre = elements_formCET['formulario_nomina_trabajadores']['Nombres']
        input_element.send_keys(nombre)

        # Apellido Paterno
        xpath = elements_formCET['formulario_nomina_trabajadores']['txtfApellido_Paterno']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        apellido_paterno = elements_formCET['formulario_nomina_trabajadores']['Apellido_Paterno']
        input_element.send_keys(apellido_paterno)

        # Apellido Materno
        xpath = elements_formCET['formulario_nomina_trabajadores']['txtfApellido_Materno']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        apellido_materno = elements_formCET['formulario_nomina_trabajadores']['Apellido_Materno']
        input_element.send_keys(apellido_materno)

        # Cargo //*[@id="viewns_Z7_JAA62IG0LO55D0Q3QIHBBN10K1_:superFormulario:j_id_g_4_8_m_1_0_2_0_a"]
        xpath = elements_formCET['formulario_nomina_trabajadores']['txtfCargo']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        cargo = elements_formCET['formulario_nomina_trabajadores']['Cargo']
        input_element.send_keys(cargo)

        # Fecha de Nacimiento //*[@id="tablaNomina0"]/div/div[2]/div[2]/div/table/tbody/tr/td[6]/input[2]
        # Encuentra el input de tipo date por su clase CSS
        input_fecha_nacimiento_front = driver.find_element(By.CLASS_NAME, 'input-fechaNacimiento-front')
        input_fecha_nacimiento_front.click()
        # Setear fecha de nacimiento
        fecha_nac = elements_formCET['formulario_nomina_trabajadores']['Fecha_de_Nacimiento']
        # Separar fecha en una lista
        list_fecha_nac = fecha_nac.split('-') # ['1990', '01', '02']      
        # Ingresar fecha de nacimiento
        for fec in list_fecha_nac:
            input_fecha_nacimiento_front.send_keys(fec)
            #presionar tecla flecha izquierda
            input_fecha_nacimiento_front.send_keys(u'\ue012')
        
        # Genero //*[@id="viewns_Z7_JAA62IG0LO55D0Q3QIHBBN10K1_:superFormulario:j_id_g_4_8_m_1_0_2_0_e"]
        xpath = elements_formCET['formulario_nomina_trabajadores']['txtfGenero']
        select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        select_element.click()
        genero = elements_formCET['formulario_nomina_trabajadores']['Genero_M']
        select_element.send_keys(genero)

        # Centro_de_Costos //*[@id="viewns_Z7_JAA62IG0LO55D0Q3QIHBBN10K1_:superFormulario:j_id_g_4_8_m_1_0_2_0_g"]
        xpath = elements_formCET['formulario_nomina_trabajadores']['txtfCentro_de_Costos']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        centro_costos = elements_formCET['formulario_nomina_trabajadores']['Centro_de_Costos']
        input_element.send_keys(centro_costos)

        # Fecha_Sugerida_Agendamiento
        # Encuentra el input de tipo date por su clase CSS
        input_fecha_agendamiento_front = driver.find_element(By.CLASS_NAME, 'input-fechaAgendamiento-front')
        input_fecha_agendamiento_front.click()
        # Setear fecha de agendamiento
        # calcular fecha para 7 días después de la fecha actual
        fecha_actual = time.strftime('%Y-%m-%d')
        fecha_actual = fecha_actual.split('-')
        dia = int(fecha_actual[2]) + 7
        fecha_agendamiento = fecha_actual[0] + '-' + fecha_actual[1] + '-' + str(dia)
        # Separar fecha en una lista
        list_fecha_agendamiento = fecha_agendamiento.split('-') # ['1990', '01', '02']
        # Ingresar fecha de agendamiento
        for fec in list_fecha_agendamiento:
            input_fecha_agendamiento_front.send_keys(fec)
            #presionar tecla flecha izquierda
            input_fecha_agendamiento_front.send_keys(u'\ue012')

        # Telefono_de_Contacto
        xpath = elements_formCET['formulario_nomina_trabajadores']['txtfTelefono_de_Contacto']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        telefono_contacto = elements_formCET['formulario_nomina_trabajadores']['Telefono_de_Contacto']
        input_element.send_keys(telefono_contacto)

        # Simular la tecla "TAB" 5 veces
        for i in range(5):
            actions.send_keys(u'\ue004')
            actions.perform()
        
        # Click en Boton_Guardar_Nomina 
        xpath = elements_formCET['formulario_nomina_trabajadores']['Boton_Guardar_Nomina']
        btn_guardar_nomina = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btn_guardar_nomina.click()

        # Pantalla de Confirmacion de nomina
        # boton Siguiente //*[@id="viewns_Z7_JAA62IG0LO55D0Q3QIHBBN10K1_:superFormulario:panelTipoMotivo"]/div[2]/div/div/div/div[1]/div/div[3]/div[2]/button
        xpath = elements_formCET['formulario_nomina_trabajadores']['Boton_Siguiente']
        btn_siguiente = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btn_siguiente.click()
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

    except Exception as e:
        print(f"Error: {e}")    

    return driver    

def LlenarFormularioCET_NomTrab_ExPreOc(driver):
    try:# Ingresa los riesgos laborales y cargos
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        # Scroll hasta el elemento
        actions = ActionChains(driver)
        # Simular la tecla "TAB" 1 veces
        actions.send_keys(u'\ue004')
        actions.perform()
        
        # Nómina de trabajadores

        """# Nombre
        xpath = elements_formCET['Centro_de_Trabajo_1']['txtf_nombre']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        nombre = elements_formCET['Centro_de_Trabajo_1']['nombre']
        input_element.send_keys(nombre)

        # Direccion
        xpath = elements_formCET['Centro_de_Trabajo_1']['txtf_direccion']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        direccion = elements_formCET['Centro_de_Trabajo_1']['direccion']    
        input_element.send_keys(direccion)

        # Seleccionar region
        xpath = elements_formCET['Centro_de_Trabajo_1']['slct_region']
        select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        select_element.click()
        xpath = elements_formCET['Centro_de_Trabajo_1']['metropolitana']
        select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        select_element.click()
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        # Seleccionar provincia
        xpath = elements_formCET['Centro_de_Trabajo_1']['slct_provincia']
        select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        select_element.click()
        xpath = elements_formCET['Centro_de_Trabajo_1']['santiago']
        select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        select_element.click()
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        # Seleccionar comuna
        xpath = elements_formCET['Centro_de_Trabajo_1']['slct_comuna']
        select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        select_element.click()
        xpath = elements_formCET['Centro_de_Trabajo_1']['providencia']
        select_element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        select_element.click()
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)"""

        # Cantidad de trabajadores
        xpath = elements_formCET['Centro_de_Trabajo_1']['txtf_cantidad_trabajadores']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        cantidad_trabajadores = elements_formCET['Centro_de_Trabajo_1']['cant_trabajadores']
        input_element.send_keys(cantidad_trabajadores)

        # Click boton ingresar nomina
        xpath = elements_formCET['Centro_de_Trabajo_1']['btn_ingresar_nomina']
        btn_ingresar_nomina = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btn_ingresar_nomina.click()
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        # formulario de nomina de trabajadores
        # RUT
        """xpath = elements_formCET['formulario_nomina_trabajadores']['selfRUT']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        xpath = elements_formCET['formulario_nomina_trabajadores']['opcRUT']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()"""
        xpath = elements_formCET['form_nomina_trab_preocupacional']['txtfRUT']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        rut = elements_formCET['form_nomina_trab_preocupacional']['RUT']
        input_element.send_keys(rut)

        # Nombre
        xpath = elements_formCET['form_nomina_trab_preocupacional']['txtfNombres']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        nombre = elements_formCET['form_nomina_trab_preocupacional']['Nombres']
        input_element.send_keys(nombre)

        # Apellido Paterno
        xpath = elements_formCET['form_nomina_trab_preocupacional']['txtfApellido_Paterno']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        apellido_paterno = elements_formCET['form_nomina_trab_preocupacional']['Apellido_Paterno']
        input_element.send_keys(apellido_paterno)

        # Apellido Materno
        xpath = elements_formCET['form_nomina_trab_preocupacional']['txtfApellido_Materno']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        apellido_materno = elements_formCET['form_nomina_trab_preocupacional']['Apellido_Materno']
        input_element.send_keys(apellido_materno)

        # Cargo //*[@id="viewns_Z7_JAA62IG0LO55D0Q3QIHBBN10K1_:superFormulario:j_id_g_4_8_m_1_0_2_0_a"]
        xpath = elements_formCET['form_nomina_trab_preocupacional']['txtfCargo']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        cargo = elements_formCET['form_nomina_trab_preocupacional']['Cargo']
        input_element.send_keys(cargo)

        # Fecha de Nacimiento //*[@id="tablaNomina0"]/div/div[2]/div[2]/div/table/tbody/tr/td[6]/input[2]
        # Encuentra el input de tipo date por su clase CSS
        input_fecha_nacimiento_front = driver.find_element(By.CLASS_NAME, 'input-fechaNacimiento-front')
        input_fecha_nacimiento_front.click()
        # Setear fecha de nacimiento
        fecha_nac = elements_formCET['form_nomina_trab_preocupacional']['Fecha_de_Nacimiento']
        # Separar fecha en una lista
        list_fecha_nac = fecha_nac.split('-') # ['1990', '01', '02']      
        # Ingresar fecha de nacimiento
        for fec in list_fecha_nac:
            input_fecha_nacimiento_front.send_keys(fec)
            #presionar tecla flecha izquierda
            input_fecha_nacimiento_front.send_keys(u'\ue012')
        
        # Genero //*[@id="viewns_Z7_JAA62IG0LO55D0Q3QIHBBN10K1_:superFormulario:j_id_g_4_8_m_1_0_2_0_e"]
        xpath = elements_formCET['form_nomina_trab_preocupacional']['txtfGenero']
        select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        select_element.click()
        genero = elements_formCET['form_nomina_trab_preocupacional']['Genero_M']
        select_element.send_keys(genero)

        # Centro_de_Costos //*[@id="viewns_Z7_JAA62IG0LO55D0Q3QIHBBN10K1_:superFormulario:j_id_g_4_8_m_1_0_2_0_g"]
        xpath = elements_formCET['form_nomina_trab_preocupacional']['txtfCentro_de_Costos']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        centro_costos = elements_formCET['form_nomina_trab_preocupacional']['Centro_de_Costos']
        input_element.send_keys(centro_costos)

        # Fecha_Sugerida_Agendamiento
        # Encuentra el input de tipo date por su clase CSS
        input_fecha_agendamiento_front = driver.find_element(By.CLASS_NAME, 'input-fechaAgendamiento-front')
        input_fecha_agendamiento_front.click()
        # Setear fecha de agendamiento
        # calcular fecha para 7 días después de la fecha actual
        fecha_actual = time.strftime('%Y-%m-%d')
        fecha_actual = fecha_actual.split('-')
        dia = int(fecha_actual[2]) + 7
        fecha_agendamiento = fecha_actual[0] + '-' + fecha_actual[1] + '-' + str(dia)
        # Separar fecha en una lista
        list_fecha_agendamiento = fecha_agendamiento.split('-') # ['1990', '01', '02']
        # Ingresar fecha de agendamiento
        for fec in list_fecha_agendamiento:
            input_fecha_agendamiento_front.send_keys(fec)
            #presionar tecla flecha izquierda
            input_fecha_agendamiento_front.send_keys(u'\ue012')

        # Telefono_de_Contacto
        xpath = elements_formCET['form_nomina_trab_preocupacional']['txtfTelefono_de_Contacto']
        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_element.click()
        telefono_contacto = elements_formCET['form_nomina_trab_preocupacional']['Telefono_de_Contacto']
        input_element.send_keys(telefono_contacto)

        # Simular la tecla "TAB" 5 veces
        for i in range(5):
            actions.send_keys(u'\ue004')
            actions.perform()
        
        # Click en Boton_Guardar_Nomina 
        xpath = elements_formCET['form_nomina_trab_preocupacional']['Boton_Guardar_Nomina']
        btn_guardar_nomina = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btn_guardar_nomina.click()

        # Pantalla de Confirmacion de nomina
        # boton Siguiente //*[@id="viewns_Z7_JAA62IG0LO55D0Q3QIHBBN10K1_:superFormulario:panelTipoMotivo"]/div[2]/div/div/div/div[1]/div/div[3]/div[2]/button
        xpath = elements_formCET['form_nomina_trab_preocupacional']['Boton_Siguiente']
        btn_siguiente = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btn_siguiente.click()
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

    except Exception as e:
        print(f"Error: {e}")    

    return driver  

"""if __name__ == "__main__":
    LlenarFormularioSolicitudHoraCet(driver)
    time.sleep(5)
    driver.quit()"""
