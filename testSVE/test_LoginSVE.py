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
test_name = "Iniciar sesion en la Sucursal Virtual Empresa Mutual"

#urlCertCloud = 'https://172.177.177.139/portal/publico/mutual/inicio/home'

# Load from data.json file
data_file = os.path.join(PROJECTPATH, 'utils/input_data', 'data.json')
with open(data_file, 'r') as f:
    data = json.load(f)

#urlPrdCloud = data['urlPrdCloud']    
urlCertCloud = data['urlCertCloud']

# Credenciales para conectarse a la Sucursal Virtual Empresa Mutual Cert
#usuario = 'AndresValdes'
#usuario = 'Cristian'
usuario = 'Dennys'
#usuario = 'PruebaClaro'
#usuario = 'HernanNava'
#usuario = 'CristianTestIBM'


rutEmpresa = data['rutEmpresaCert'][usuario]
claveEmpresa = data['claveEmpresaCert'][usuario]

#uservoid
#rutEmpresa = data['rutEmpresaCert']['uservoid']
#userwrong
#rutEmpresa = data['rutEmpresaCert']['userwrong']
#passvoid
#claveEmpresa = data['claveEmpresaCert']['passvoid']
#passwrong
#claveEmpresa = data['claveEmpresaCert']['passwrong']

# Si tiene mas de una empresa hay que seleccionar la empresa
empresa = "MUTUAL"
#empresa = "WALMART"
empresaid = data['empresaid'][empresa]   

if __name__ == "__main__":
    print(f"Iniciando el test: {test_name}")
    # 1 - Llamar a la función gotoMutual y obtener el driver
    from gotoMutual import gotoMutual
    driver = gotoMutual(urlCertCloud)
    # 2 - Llamar a la funcion LoginSVE
    from loginSVEMutual import loginSVEMutual
    driver = loginSVEMutual(driver, rutEmpresa, claveEmpresa, empresaid)
    time.sleep(5)
    
    driver.quit()
    print(f"Test finalizado: {test_name}")
    
