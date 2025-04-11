import time
import json
import os
import sys

# Define the project path
SCRIP_PATH = os.path.dirname(__file__)
PROJECTPATH = os.path.dirname(SCRIP_PATH)

# Agrega la ruta de 'utils' al sys.path
utils_path = os.path.join(PROJECTPATH, 'utils')
sys.path.append(utils_path)

# Test_Name
test_name = "Iniciar sesion en la Sucursal Virtual Trabajador Mutual"

#urlCertCloud = 'https://172.177.177.139/portal/publico/mutual/inicio/home'

# Load from data.json file
data_file = os.path.join(PROJECTPATH, 'utils/input_data', 'data.json')
with open(data_file, 'r') as f:
    data = json.load(f)

urlCertCloud = data['urlCertCloud']
urlProdCloud = data['urlProdCloud']

#Load elements from elements.json file
elements_file = os.path.join(PROJECTPATH, 'utils/input_data', 'elements.json')
with open(elements_file, 'r') as f:
    elements_Menu = json.load(f) 
# Credenciales para conectarse a la Sucursal Virtual Mutual
#usuario = 'AndresValdes'
#usuario = 'Cristian'
#usuario = 'CSalas'
#usuario = 'Dennys'
#usuario = 'KevinCortes'
#usuario = 'PruebaPruebaPrueba'
#usuario = 'TestTest'
usuario = 'CesarAgurto'
#usuario = 'CarlaMarina'

#usuario = 'IreneQuevedo'

rutTrabajador = data['rutTrabajadorCert'][usuario]
claveTrabajador = data['claveTrabajadorCert'][usuario]

#uservoid
#rutTrabajador = data['rutTrabajadorCert']['uservoid']
#userwrong
#rutTrabajador = data['rutTrabajadorCert']['userwrong']
#passvoid
#claveTrabajador = data['claveTrabajadorCert']['passvoid']
#passwrong
#claveTrabajador = data['claveTrabajadorCert']['passwrong']

# Si tiene mas de una empresa hay que seleccionar la empresa
empresa = "MUTUAL"
#empresa = "WALMART"
empresaid = data['empresaid'][empresa]

if __name__ == "__main__":
    print(f"Iniciando el test: {test_name}")
    # 1 - Llamar a la función gotoMutual y obtener el driver
    from gotoMutual import gotoMutual
    driver = gotoMutual(urlCertCloud)
    #driver = gotoMutual(urlProdCloud)
    # 2 - Llama a la funcion LoginSVTMutual
    from loginSVTMutual import loginSVTMutual
    driver = loginSVTMutual(driver, rutTrabajador, claveTrabajador)

    time.sleep(5)
    driver.quit()
    print(f"Test finalizado: {test_name}")
