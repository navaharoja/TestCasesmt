from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os

urlOp = 'https://www.mutual.cl/portal/publico/mutual/inicio/home'
urlCertCloud = 'https://172.177.177.139/portal/publico/mutual/inicio/home'

def gotoMutual(url):
    # Configurar opciones de Firefox
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--no-sandbox')
    #firefox_options.add_argument('--headless')

    # Inicializar el controlador de Firefox
    driver = webdriver.Firefox(options=firefox_options)

    try:
        driver.maximize_window()
        driver.get(url)

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="details-button"]')))
            driver.find_element(By.ID, 'details-button').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="proceed-link"]')))
            driver.find_element(By.ID, 'proceed-link').click()
        except TimeoutException:
            pass

        try:
            WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        except TimeoutException:
            print(f"La página no se ha cargado completamente en {url}. Continuando con el siguiente URL.")
            driver.close()
            if len(driver.window_handles) > 0:
                driver.switch_to.window(driver.window_handles[0])

    except Exception as e:
        print(f"Error: {e}")  
    
    return driver

"""if __name__ == "__main__":
    gotoMutual(urlCertCloud)
    time.sleep(5)
    driver.quit()
"""







