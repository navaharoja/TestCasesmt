import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def get_all_xpaths(driver):
    elements = driver.find_elements(By.XPATH, "//*")  # Seleccionar todos los elementos
    xpaths = {}
    for index, element in enumerate(elements):
        try:
            # Obtener XPath único de cada elemento
            xpath = get_xpath(driver, element)
            tag = element.tag_name
            xpaths[f"{tag}_{index}"] = xpath
        except Exception as e:
            print(f"Error al obtener XPath de un elemento: {e}")
    return xpaths

def get_xpath(driver, element):
    components = []
    child = element
    while child != driver.find_element(By.XPATH, "/"):
        parent = driver.execute_script(
            "return arguments[0].parentNode;", child)
        children = parent.find_elements(By.XPATH, "*")
        index = 1
        for i, child_element in enumerate(children):
            if child_element == child:
                components.append(
                    f"{child_element.tag_name}[{index}]")
                break
            if child_element.tag_name == child.tag_name:
                index += 1
        child = parent
    components.reverse()
    return f"/{'/'.join(components)}"

def save_xpaths_to_json(xpaths, filename="xpaths.json"):
    with open(filename, 'w') as file:
        json.dump(xpaths, file, indent=4)
    print(f"XPaths guardados en {filename}")

def main(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)

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
        # Esperar a que la página se cargue completamente
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # Obtener todos los XPaths
        xpaths = get_all_xpaths(driver)

        # Guardar XPaths en un archivo JSON
        save_xpaths_to_json(xpaths)
        """try:
            WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        except TimeoutException:
            print(f"La página no se ha cargado completamente en {url}. Continuando con el siguiente URL.")
            driver.close()
            if len(driver.window_handles) > 0:
                driver.switch_to.window(driver.window_handles[0])"""

    except Exception as e:
        print(f"Error: {e}")  

        

    except TimeoutException:
        print(f"Error: la página no se cargó en el tiempo esperado.")
    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://172.177.177.139/portal/publico/mutual/inicio/centroayuda/solicitudes-horas-cet/"  # Reemplaza con la URL deseada
    main(url)
