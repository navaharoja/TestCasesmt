import os
import requests
import zipfile
import shutil
import subprocess
import sys

# Ruta donde se almacenará chromedriver
PROJECTPATH = os.path.dirname(__file__)
#CHROMEDRIVER_DIR = os.path.join(PROJECTPATH, "settings/drivers")
CHROMEDRIVER_ZIP_PATH = os.path.join(PROJECTPATH, "chromedriver.zip")
CHROMEDRIVER_EXEC_PATH = os.path.join(PROJECTPATH, "chromedriver.exe")

def get_chrome_version():
    """Obtiene la versión de Google Chrome instalada."""
    try:
        # Comando para obtener la versión de Chrome en Windows
        output = subprocess.check_output(
            r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version /value',
            shell=True
        )
        version = output.decode('utf-8').strip().split('=')[1]
        return version
    except Exception as e:
        print(f"Error al obtener la versión de Chrome: {e}")
        sys.exit(1)

def get_chromedriver_url(version):
    """Obtiene la URL de descarga de chromedriver correspondiente a la versión de Chrome."""
    #major_version = version.split('.')[0]
    #url = f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{major_version}"
    url = f"https://storage.googleapis.com/chrome-for-testing-public/{version}/win32/chromedriver-win32.zip"
    try:
        response = requests.get(url)
        response.raise_for_status()
        latest_version = response.text.strip()
        download_url = url
        return download_url
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la URL de chromedriver: {e}")
        sys.exit(1)

def download_and_extract_chromedriver(url):
    """Descarga y extrae chromedriver."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(CHROMEDRIVER_ZIP_PATH, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        with zipfile.ZipFile(CHROMEDRIVER_ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(PROJECTPATH)
        print(f"chromedriver actualizado en: {CHROMEDRIVER_EXEC_PATH}")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar chromedriver: {e}")
        sys.exit(1)

def clean_up():
    """Elimina archivos temporales utilizados durante la actualización."""
    if os.path.exists(CHROMEDRIVER_ZIP_PATH):
        os.remove(CHROMEDRIVER_ZIP_PATH)

def main():
    if not os.path.exists(PROJECTPATH):
        os.makedirs(PROJECTPATH)

    chrome_version = get_chrome_version()
    print(f"Versión de Google Chrome instalada: {chrome_version}")

    chromedriver_url = get_chromedriver_url(chrome_version)
    print(f"Descargando chromedriver desde: {chromedriver_url}")

    download_and_extract_chromedriver(chromedriver_url)
    clean_up()

if __name__ == "__main__":
    main()
