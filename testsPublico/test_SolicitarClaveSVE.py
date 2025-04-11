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

urlCertCloud = data['urlCertCloud']
urlPrdCloud = data['urlPrdCloud']

# Credenciales para conectarse a la Sucursal Virtual Empresa Mutual
usuario = 'AndresValdes'
#usuario = 'Cristian'
#usuario = 'Dennys'
rutEmpresa = data['rutEmpresaCert'][usuario]
claveEmpresa = data['claveEmpresaCert'][usuario]

# Si tiene mas de una empresa hay que seleccionar la empresa
empresaid = data['empresaid'] # MUTUAL DE SEGURIDAD C.CH.C [2] Cristian    

if __name__ == "__main__":
    print(f"Iniciando el test: {test_name}")
    # 1 - Llamar a la función gotoMutual y obtener el driver
    from gotoMutual import gotoMutual
    driver = gotoMutual(urlPrdCloud)
    # 2 - Llamar a la funcion SolicitarClaveSVE
    from SolicitarClaveSVE import SolicitarClaveSVE
    driver = SolicitarClaveSVE(driver)

    # Wait 5 seconds
    time.sleep(5) 
    
    driver.quit()
    print(f"Test finalizado: {test_name}")
