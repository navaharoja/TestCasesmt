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

# Llamar a la función gotoMutual y obtener el driver
#from utils.gotoMutual import gotoMutual
#driver = gotoMutual(urlCertCloud)

def LlenarFormularioCET_SolicitudHoraCet_ExOc(driver):
    try:
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)
        
        # Navegar a la página de Solicitud de horas CET a traves del menu
        xpath_menu_centro_ayuda = elements_Menu['menu_centro_ayuda']['xpath']
        menu_centro_ayuda = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_menu_centro_ayuda)))
        menu_centro_ayuda.click()

        xpath_menu_solicitud_cet = elements_Menu['menu_solicitud_cet']['xpath']
        menu_solicitud_cet = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_menu_solicitud_cet)))
        menu_solicitud_cet.click()

        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        try:# Completar formulario 1 de solicitud de horas CET
            # Seleccion Motivo de Evaluacion //*[@id="motivo"]
            xpathmotivo = elements_formCET['motivo']['selectmotivo']
            # Esperar a que el campo Motivo de evaluación sea visible y pueda ser interactuado
            motivo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathmotivo)))
            # Clic en el campo Motivo de evaluación
            motivo.click()

            # Seleccionar Examen Ocupacional
            xpathexamenocupacional = elements_formCET['motivo']['examenocupacional']
            # Esperar a que el campo Motivo de evaluación sea visible y pueda ser interactuado
            examenocupacional = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathexamenocupacional)))
            # Clic en el campo Motivo de evaluación
            examenocupacional.click()

            # Wait 3 seconds
            time.sleep(3)

            # Scroll hasta el elemento
            xpathelement = '//*[@id="viewns_Z7_JAA62IG0LO55D0Q3QIHBBN10K1_:superFormulario:divDatosContactoFacturacion"]/div/div/div/div[1]/div/div'
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathelement)))   
            driver.execute_script("arguments[0].scrollIntoView(true);", element)

            # Formulario CET Ocupacional
            # Selección de Tipo de solicitante
            xpathtipo_solicitante = elements_formCET['tipoSolicitante']['tipoSolicitante']
            tipo_solicitante = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathtipo_solicitante)))
            tipo_solicitante.click()
            xpathtiposolicitante = elements_formCET['tipoSolicitante']['trabajador_dependiente_protegido']
            tiposolicitante = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathtiposolicitante)))
            tiposolicitante.click()
            # Wait 5 seconds
            time.sleep(3)

            # Formulario Informacion del solicitante
            # Ingresar Rut Empresa
            xpathrutempresa = elements_formCET['informacion_solicitante']['rut_empresa']
            rut_empresa = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathrutempresa)))
            rut_empresa.click()
            rutEmpresa = data['rutEmpresaMutual']
            rut_empresa.send_keys(rutEmpresa)
            rut_empresa.send_keys(u'\ue004') # Simular la tecla "TAB"
            
            
            # Ingresar Razon Social
            xpathrazonsocial = elements_formCET['informacion_solicitante']['razon_social']
            razon_social = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathrazonsocial)))
            # Hacer clic en el campo Razón Social
            razon_social.click()
            # Wait 5 seconds
            time.sleep(5)

            # Ingresar RUT Contacto
            xpathrutcontacto = elements_formCET['informacion_solicitante']['rut_contacto']
            # Esperar a que el campo Motivo de evaluación sea visible y pueda ser interactuado
            rut_contacto = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathrutcontacto)))
            rut_contacto.click()
            rutContacto = data['rutContactoMutual']
            rut_contacto.send_keys(rutContacto)
            
            # Hacer click fuera del campo rut_contacto
            clickout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
            clickout.click()
            # Wait 5 seconds
            time.sleep(5)

            # Ingresar Nombre
            xpathnombre = elements_formCET['informacion_solicitante']['nombre']
            nombre = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathnombre)))
            nombre.click()
            nombreSolicitante = data['nombreSolicitanteMutual']
            nombre.send_keys(nombreSolicitante)

            # Ingresar Apellido Paterno
            xpathapellidopaterno = elements_formCET['informacion_solicitante']['apellido_paterno']
            apellido_paterno = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathapellidopaterno)))
            apellido_paterno.click()
            apellidoPaterno = data['apellidoPaterno']
            apellido_paterno.send_keys(apellidoPaterno)

            # Ingresar Apellido Materno
            xpathapellidomaterno = elements_formCET['informacion_solicitante']['apellido_materno']
            apellido_materno = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathapellidomaterno)))
            apellido_materno.click()
            apellidoMaterno = data['apellidoMaterno']
            apellido_materno.send_keys(apellidoMaterno)

            # Ingresar Correo electrónico
            xpathcorreo = elements_formCET['informacion_solicitante']['correo_electronico']
            correo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathcorreo)))
            correo.click()
            correoElectronico = data['correoElectronico']
            correo.send_keys(correoElectronico)

            # Ingresar Téléfono de contacto
            xpathtelefono = elements_formCET['informacion_solicitante']['telefono_contacto']
            telefono = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathtelefono)))
            telefono.click()
            telefonoContacto = data['telefonoContacto']
            telefono.send_keys(telefonoContacto)

            # Ingresar Calle //*[@id="domicilio"]
            xpathcalle = elements_formCET['informacion_solicitante']['calle']
            calle = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathcalle)))
            calle.click()
            calleSolicitante = data['calle']
            calle.send_keys(calleSolicitante)

            # Ingresar Numero //*[@id="numeroCalle"]
            xpathnumero = elements_formCET['informacion_solicitante']['numero']
            numero = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathnumero)))
            numero.click()
            numeroSolicitante = data['numero']
            numero.send_keys(numeroSolicitante)

            # Seleccionar Comuna //*[@id="comuna"]
            xpathcomuna = elements_formCET['informacion_solicitante']['comuna']
            comuna = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathcomuna)))
            comuna.click()
            xpathcomunapru = elements_formCET['informacion_solicitante']['comuna_prueba']    
            comuna_prueba = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathcomunapru)))
            comuna_prueba.click()  
            # Wait 3 seconds
            time.sleep(3)

            # Seleccionar Cargo
            xpathcargo = elements_formCET['cargo']['cargo']
            cargo = driver.find_element(By.XPATH, xpathcargo)
            cargo.click()
            xpathcargoanalista = elements_formCET['cargo']['cargo_analista']
            cargo_analista = driver.find_element(By.XPATH, xpathcargoanalista)
            cargo_analista.click()
            # Wait 3 seconds
            time.sleep(3)

            # Seleccionar Genero //*[@id="genero"]
            xpathgenero = elements_formCET['genero']['genero']
            genero = driver.find_element(By.XPATH, xpathgenero)
            genero.click()
            xpathgenerohombre = elements_formCET['genero']['hombre']
            genero_hombre = driver.find_element(By.XPATH, xpathgenerohombre)
            genero_hombre.click()

            # Datos de facturación '//*[@id="datosContactoFacturacion"]/div/div[3]'
            xpathelement = xpathnumero
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathelement)))
            element.click()
            actions = ActionChains(driver)
            # Simular la tecla "TAB" 4 veces
            for _ in range(4):
                actions.send_keys(u'\ue004')
                actions.perform()
                
            # Ingresa Direccion de facturacion
            xpathdireccionfacturacion = elements_formCET['datos_facturacion']['direccion_facturacion']
            direccion_facturacion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathdireccionfacturacion)))
            direccionFacturacion = data['direccionFacturacion']
            direccion_facturacion.send_keys(direccionFacturacion)

            # Seleccionar Comuna de facturación
            # Seleccionar Comuna
            xpathcomunafacturacion = elements_formCET['datos_facturacion']['comuna_facturacion']
            comuna_facturacion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathcomunafacturacion)))
            comuna_facturacion.click()
            xpathcomunapru = elements_formCET['datos_facturacion']['comuna_facturacion_prueba']
            comuna_prueba = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathcomunapru)))
            comuna_prueba.click()

            # Centro de evaluación del trabajo (CET)
            # Seleccionar Región
            xpathregion = elements_formCET['centro_evaluacion_trabajo']['region']
            region = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathregion)))
            region.click()
            xpathregionmetropolitana = elements_formCET['centro_evaluacion_trabajo']['region_metropolitana']
            region_metropolitana = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathregionmetropolitana)))
            region_metropolitana.click()
            # Wait 3 seconds
            time.sleep(3)

            # Seleccionar Agencia
            # Agencia //*[@id="agencia"]
            xpathagencia = elements_formCET['centro_evaluacion_trabajo']['agencia']['CET_Providencia']
            agencia = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathagencia)))
            agencia.click()
            """xpathagenciapru = elements_formCET['centro_evaluacion_trabajo']['agencia_prueba']
            agencia_prueba = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathagenciapru)))
            agencia_prueba.click()"""
            # Wait 3 seconds
            time.sleep(3)

            # Click en agencia 
            agencia.click()

            # Simular la tecla "TAB" 1 veces
            actions.send_keys(u'\ue004')
            actions.perform()

            # Motivo del requerimiento //*[@id="datosContactoFacturacion"]/div/div[7]/div/div/textarea
            xpathmotivorequerimiento = elements_formCET['motivo_requerimiento']['motivo_desc']
            motivorequerimiento = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathmotivorequerimiento)))
            motivorequerimiento.click()
            descripcionMotivo = data['descripcionMotivoCET']
            motivorequerimiento.send_keys(descripcionMotivo)

            # Click en agencia 
            for _ in range(2):
                agencia.click()

            # Simular la tecla "TAB" 2 veces
            for _ in range(2):
                actions.send_keys(u'\ue004')
                actions.perform()

            # Click en el boton de Enviar solicitud //*[@id="datosContactoFacturacion"]/div/div[8]/div/button
            xpathenviarsolicitud = elements_formCET['boton_enviar']['enviar']
            enviarsolicitud = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathenviarsolicitud)))
            enviarsolicitud.click()
            # Wait 3 seconds
            time.sleep(5)    

        except Exception as e:
            print(f"Error: {e}")

    except Exception as e:
        print(f"Error: {e}")    

    return driver    

def LlenarFormularioCET_SolicitudHoraCet_ExPreOc(driver):
    try:
        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)
        
        # Navegar a la página de Solicitud de horas CET a traves del menu
        xpath_menu_centro_ayuda = elements_Menu['menu_centro_ayuda']['xpath']
        menu_centro_ayuda = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_menu_centro_ayuda)))
        menu_centro_ayuda.click()

        xpath_menu_solicitud_cet = elements_Menu['menu_solicitud_cet']['xpath']
        menu_solicitud_cet = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_menu_solicitud_cet)))
        menu_solicitud_cet.click()

        # Esperar 3 segundos para ver si la página se carga
        time.sleep(3)

        try:# Completar formulario 1 de solicitud de horas CET
            # Seleccion Motivo de Evaluacion //*[@id="motivo"]
            xpathmotivo = elements_formCET['motivo']['selectmotivo']
            # Esperar a que el campo Motivo de evaluación sea visible y pueda ser interactuado
            motivo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathmotivo)))
            # Clic en el campo Motivo de evaluación
            motivo.click()

            # Seleccionar Examen Ocupacional
            xpathexamenpreocupacional = elements_formCET['motivo']['examenpreocupacional']
            # Esperar a que el campo Motivo de evaluación sea visible y pueda ser interactuado
            examenocupacional = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathexamenpreocupacional)))
            # Clic en el campo Motivo de evaluación
            examenocupacional.click()

            # Wait 3 seconds
            time.sleep(3)

            # Scroll hasta el elemento
            xpathelement = '//*[@id="viewns_Z7_JAA62IG0LO55D0Q3QIHBBN10K1_:superFormulario:divDatosContactoFacturacion"]/div/div/div/div[1]/div/div'
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathelement)))   
            driver.execute_script("arguments[0].scrollIntoView(true);", element)

            # Formulario CET Ocupacional
            # Selección de Tipo de solicitante
            xpathtipo_solicitante = elements_formCET['tipoSolicitante']['tipoSolicitante']
            tipo_solicitante = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathtipo_solicitante)))
            tipo_solicitante.click()
            xpathtiposolicitante = elements_formCET['tipoSolicitante']['trabajador_dependiente_protegido']
            tiposolicitante = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathtiposolicitante)))
            tiposolicitante.click()
            # Wait 5 seconds
            time.sleep(3)

            # Formulario Informacion del solicitante
            # Ingresar Rut Empresa
            xpathrutempresa = elements_formCET['informacion_solicitante']['rut_empresa']
            rut_empresa = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathrutempresa)))
            rut_empresa.click()
            rutEmpresa = data['rutEmpresaMutual']
            rut_empresa.send_keys(rutEmpresa)
            rut_empresa.send_keys(u'\ue004') # Simular la tecla "TAB"
            
            
            # Ingresar Razon Social
            xpathrazonsocial = elements_formCET['informacion_solicitante']['razon_social']
            razon_social = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathrazonsocial)))
            # Hacer clic en el campo Razón Social
            razon_social.click()
            # Wait 5 seconds
            time.sleep(5)

            # Ingresar RUT Contacto
            xpathrutcontacto = elements_formCET['informacion_solicitante']['rut_contacto']
            # Esperar a que el campo Motivo de evaluación sea visible y pueda ser interactuado
            rut_contacto = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathrutcontacto)))
            rut_contacto.click()
            rutContacto = data['rutContactoMutual']
            rut_contacto.send_keys(rutContacto)
            
            # Hacer click fuera del campo rut_contacto
            clickout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
            clickout.click()
            # Wait 5 seconds
            time.sleep(5)

            # Ingresar Nombre
            xpathnombre = elements_formCET['informacion_solicitante']['nombre']
            nombre = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathnombre)))
            nombre.click()
            nombreSolicitante = data['nombreSolicitanteMutual']
            nombre.send_keys(nombreSolicitante)

            # Ingresar Apellido Paterno
            xpathapellidopaterno = elements_formCET['informacion_solicitante']['apellido_paterno']
            apellido_paterno = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathapellidopaterno)))
            apellido_paterno.click()
            apellidoPaterno = data['apellidoPaterno']
            apellido_paterno.send_keys(apellidoPaterno)

            # Ingresar Apellido Materno
            xpathapellidomaterno = elements_formCET['informacion_solicitante']['apellido_materno']
            apellido_materno = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathapellidomaterno)))
            apellido_materno.click()
            apellidoMaterno = data['apellidoMaterno']
            apellido_materno.send_keys(apellidoMaterno)

            # Ingresar Correo electrónico
            xpathcorreo = elements_formCET['informacion_solicitante']['correo_electronico']
            correo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathcorreo)))
            correo.click()
            correoElectronico = data['correoElectronico']
            correo.send_keys(correoElectronico)

            # Ingresar Téléfono de contacto
            xpathtelefono = elements_formCET['informacion_solicitante']['telefono_contacto']
            telefono = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathtelefono)))
            telefono.click()
            telefonoContacto = data['telefonoContacto']
            telefono.send_keys(telefonoContacto)

            # Ingresar Calle //*[@id="domicilio"]
            xpathcalle = elements_formCET['informacion_solicitante']['calle']
            calle = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathcalle)))
            calle.click()
            calleSolicitante = data['calle']
            calle.send_keys(calleSolicitante)

            # Ingresar Numero //*[@id="numeroCalle"]
            xpathnumero = elements_formCET['informacion_solicitante']['numero']
            numero = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathnumero)))
            numero.click()
            numeroSolicitante = data['numero']
            numero.send_keys(numeroSolicitante)

            # Seleccionar Comuna //*[@id="comuna"]
            xpathcomuna = elements_formCET['informacion_solicitante']['comuna']
            comuna = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathcomuna)))
            comuna.click()
            xpathcomunapru = elements_formCET['informacion_solicitante']['comuna_prueba']    
            comuna_prueba = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathcomunapru)))
            comuna_prueba.click()  
            # Wait 3 seconds
            time.sleep(3)

            # Seleccionar Cargo
            xpathcargo = elements_formCET['cargo']['cargo']
            cargo = driver.find_element(By.XPATH, xpathcargo)
            cargo.click()
            xpathcargoanalista = elements_formCET['cargo']['cargo_analista']
            cargo_analista = driver.find_element(By.XPATH, xpathcargoanalista)
            cargo_analista.click()
            # Wait 3 seconds
            time.sleep(3)

            # Seleccionar Genero //*[@id="genero"]
            xpathgenero = elements_formCET['genero']['genero']
            genero = driver.find_element(By.XPATH, xpathgenero)
            genero.click()
            xpathgenerohombre = elements_formCET['genero']['hombre']
            genero_hombre = driver.find_element(By.XPATH, xpathgenerohombre)
            genero_hombre.click()

            # Datos de facturación '//*[@id="datosContactoFacturacion"]/div/div[3]'
            xpathelement = xpathnumero
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathelement)))
            element.click()
            actions = ActionChains(driver)
            # Simular la tecla "TAB" 4 veces
            for _ in range(4):
                actions.send_keys(u'\ue004')
                actions.perform()
                
            # Ingresa Direccion de facturacion
            xpathdireccionfacturacion = elements_formCET['datos_facturacion']['direccion_facturacion']
            direccion_facturacion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathdireccionfacturacion)))
            direccionFacturacion = data['direccionFacturacion']
            direccion_facturacion.send_keys(direccionFacturacion)

            # Seleccionar Comuna de facturación
            # Seleccionar Comuna
            xpathcomunafacturacion = elements_formCET['datos_facturacion']['comuna_facturacion']
            comuna_facturacion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathcomunafacturacion)))
            comuna_facturacion.click()
            xpathcomunapru = elements_formCET['datos_facturacion']['comuna_facturacion_prueba']
            comuna_prueba = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathcomunapru)))
            comuna_prueba.click()

            # Centro de evaluación del trabajo (CET)
            # Seleccionar Región
            xpathregion = elements_formCET['centro_evaluacion_trabajo']['region']
            region = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathregion)))
            region.click()
            xpathregionmetropolitana = elements_formCET['centro_evaluacion_trabajo']['region_metropolitana']
            region_metropolitana = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathregionmetropolitana)))
            region_metropolitana.click()
            # Wait 3 seconds
            time.sleep(3)

            # Seleccionar Agencia
            # Agencia //*[@id="agencia"]
            xpathAgencia = "//*[@id='agencia']"
            agenciacb = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathAgencia)))
            agenciacb.click()
            xpathagencia = elements_formCET['centro_evaluacion_trabajo']['agencia']['CET_Providencia']
            agencia = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathagencia)))
            agencia.click()
            """xpathagenciapru = elements_formCET['centro_evaluacion_trabajo']['agencia_prueba']
            agencia_prueba = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathagenciapru)))
            agencia_prueba.click()"""
            # Wait 3 seconds
            time.sleep(3)

            # Click en agencia 
            agencia.click()

            # Simular la tecla "TAB" 1 veces
            actions.send_keys(u'\ue004')
            actions.perform()

            # Motivo del requerimiento //*[@id="datosContactoFacturacion"]/div/div[7]/div/div/textarea
            xpathmotivorequerimiento = elements_formCET['motivo_requerimiento']['motivo_desc']
            motivorequerimiento = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathmotivorequerimiento)))
            motivorequerimiento.click()
            descripcionMotivo = data['descripcionMotivoCET']
            motivorequerimiento.send_keys(descripcionMotivo)
            # Wait 3 seconds
            time.sleep(3) 

            # Click en agencia 
            for _ in range(2):
                agencia.click()

            # Simular la tecla "TAB" 2 veces
            for _ in range(2):
                actions.send_keys(u'\ue004')
                actions.perform()

            # Click en el boton de Enviar solicitud //*[@id="datosContactoFacturacion"]/div/div[8]/div/button
            xpathenviarsolicitud = elements_formCET['boton_enviar']['enviar']
            enviarsolicitud = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathenviarsolicitud)))
            enviarsolicitud.click()
            # Wait 3 seconds
            time.sleep(5)    

        except Exception as e:
            print(f"Error: {e}")

    except Exception as e:
        print(f"Error: {e}")    

    return driver   

"""if __name__ == "__main__":
    LlenarFormularioSolicitudHoraCet(driver)
    time.sleep(5)
    driver.quit()"""
