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
elements_file = os.path.join(PROJECTPATH, 'input_data', 'elements_formularioSCR.json')
with open(elements_file, 'r') as f:
    elements_formSCR = json.load(f)

"""# Llamar a la función gotoMutual y obtener el driver
from utils.gotoMutual import gotoMutual
driver = gotoMutual(urlCertCloud)"""

def LlenarFormularioSCR(driver):
    try:# Ingresa los riesgos laborales y cargos
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        # Navegar al menu de Solicitudes, columnas y Reclamos
        xpath_menu_centro_ayuda = elements_Menu['menu_centro_ayuda']['xpath']
        menu_centro_ayuda = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_menu_centro_ayuda)))
        menu_centro_ayuda.click()

        xpath = elements_Menu['menu_solicitudes_consultas_reclamos']['xpath']
        btn_menu_solicitudes_consultas_reclamos = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        btn_menu_solicitudes_consultas_reclamos.click()
        
        # Formulario Solicitudes, Consultas y Reclamos

        # Seleccionar Tipo de Caso
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Tipo_Caso']['xpath']
        combo_tipo_caso = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        combo_tipo_caso.click()

        #xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Tipo_Caso']['options']['Consulta']
        #xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Tipo_Caso']['options']['Reclamo']
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Tipo_Caso']['options']['Solicitud']

        option_solicitud = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        option_solicitud.click()
        # wait 3 seconds
        time.sleep(5)

        # Seleccionar Tema
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Tema']['xpath']
        combo_tema = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        combo_tema.click()

        #xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Tema']['options']['Administracion_de_Siniestros']
        #xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Tema']['options']['Beneficios_Economicos']
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Tema']['options']['Relaciones_Comerciales']


        option_xpath = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        option_xpath.click()
        # wait 3 seconds
        time.sleep(3)

        # Seleccionar Categoria
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Categoria']['xpath']
        combo_categoria = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        combo_categoria.click()

        #xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Categoria']['options']['Pago_de_beneficios_economicos']
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Categoria']['options']['Relaciones_con_adherentes']

        option_xpath = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        option_xpath.click()
        # wait 3 seconds
        time.sleep(3)

        # Seleccionar Motivo
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Motivo']['xpath']
        combo_motivo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        combo_motivo.click()

        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Motivo']['options']['Suspension_o_no_Pago_de_Subsidio']
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Motivo']['options']['Cambio_Representante_Legal']
        
        option_xpath = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        option_xpath.click()
        # wait 3 seconds
        time.sleep(3)

        # Requiere respuesta
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Requiere_Respuesta']['xpath']
        combo_requiere_respuesta = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        combo_requiere_respuesta.click()

        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Requiere_Respuesta']['options']['Si']
        option_si = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        option_si.click()

        # Canal de respuesta
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Canal_de_Respuesta']['xpath']
        combo_canal_respuesta = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        combo_canal_respuesta.click()

        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Canal_de_Respuesta']['options']['Correo_Electronico']
        option_correo_electronico = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        option_correo_electronico.click()
        # wait 3 seconds
        time.sleep(3)

        """# Scroll hasta el elemento
        actions = ActionChains(driver)
        # Simular la tecla "TAB" 1 veces
        actions.send_keys(u'\ue004')
        # Enter
        actions.send_keys(u'\ue007')
        # Simular flecha abajo
        actions.send_keys(u'\ue015')
        actions.perform()"""

        # Datos de Contacto  
        # bajar hasta el elemento
        driver.execute_script("arguments[0].scrollIntoView();", combo_canal_respuesta)
        # wait 3 seconds
        time.sleep(3)

        # Tipo de Solicitante
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Tipo_de_Solicitante']['xpath']
        combo_tipo_solicitante = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        combo_tipo_solicitante.click()

        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Tipo_de_Solicitante']['options']['Trabajador_dependiente_protegido']
        option_asegurado = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        option_asegurado.click()
        # wait 3 seconds
        time.sleep(3)

        # Rut Empresa
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Rut_Empresa']
        input_rut_empresa = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        rut_empresa = data['rutEmpresaMutual']
        input_rut_empresa.send_keys(rut_empresa)

        # Razon Social
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Razon_Social']
        input_razon_social = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_razon_social.click()
        # wait 3 seconds
        time.sleep(9)

        # Rut de Contacto
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Rut_de_Contacto']
        input_rut_contacto = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        rut_contacto = data['rutContactoMutual']
        input_rut_contacto.send_keys(rut_contacto)

        # Nombre
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Nombre']
        input_nombre = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_nombre.click()
        # wait 3 seconds
        time.sleep(5)
        """nombre = data['nombreSolicitanteMutual']
        input_nombre.send_keys(nombre)
        # wait 3 seconds
        time.sleep(3)

        # Apellido Paterno
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Apellido_Paterno']
        input_apellido_paterno = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        apellido_paterno = data['apellidoPaterno']
        input_apellido_paterno.send_keys(apellido_paterno)

        # Apellido Materno
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Apellido_Materno']
        input_apellido_materno = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        apellido_materno = data['apellidoMaterno']
        input_apellido_materno.send_keys(apellido_materno)"""

        # Email
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Email']
        input_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_email.click()
        email = data['correoElectronico']
        input_email.send_keys(email)

        # Telefono
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Telefono']
        input_telefono = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_telefono.click()
        telefono = data['telefonoContacto']
        input_telefono.send_keys(telefono)

        # Calle
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Calle']
        input_calle = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_calle.click()
        calle = data['calle']
        input_calle.send_keys(calle)

        # Número
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Numero']
        input_numero = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_numero.click()
        numero = data['numero']
        input_numero.send_keys(numero)

        # Seleccionar Comuna
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Comuna']['xpath']
        combo_comuna = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        combo_comuna.click()

        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Comuna']['options']['PRUEBA']
        option_santiago = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        option_santiago.click()

        # Seleccionar Cargo
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Cargo']['xpath']
        combo_cargo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        combo_cargo.click()

        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Cargo']['options']['ADMINISTRATIVO']
        #xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Cargo']['options']['ANALISTA']

        option_xpath = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        option_xpath.click()
        time.sleep(3)

        # Bajar hasta el elemento
        driver.execute_script("arguments[0].scrollIntoView();", input_numero)
        # wait 3 seconds
        time.sleep(3)

        # Seleccionar Genero
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Genero']['xpath']
        combo_genero = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        combo_genero.click()

        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Datos_de_Contacto']['Genero']['options']['Hombre']
        option_masculino = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        option_masculino.click()

        # ingresar Motivo del requerimiento
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Motivo_del_requerimiento']
        input_motivo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        input_motivo.click()
        motivo = data['descripcionMotivoSCR']
        input_motivo.send_keys(motivo)

        # Bajar hasta el elemento
        driver.execute_script("arguments[0].scrollIntoView();", input_motivo)
        # wait 3 seconds
        time.sleep(3)

        # Logica para adjuntar archivo

        """# Click Recatcha
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Recaptcha']
        recaptcha = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        recaptcha.click()
        # wait 3 seconds
        time.sleep(3)

        # Click Enviar
        xpath = elements_formSCR['Solicitudes_Consultas_Reclamos']['Enviar']
        btn_enviar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btn_enviar.click()
        # wait 3 seconds
        time.sleep(3)"""
       
    except Exception as e:
        print(f"Error: {e}")    

    return driver    

"""if __name__ == "__main__":
    LlenarFormularioSCR(driver)
    time.sleep(5)
    driver.quit()"""
