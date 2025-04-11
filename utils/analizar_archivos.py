import pandas as pd
import glob
import os
import logging

file_map = {
            "PUBLICO": 'Tiempo Promedio de Carga Urls PUB.csv',
            "EMPRESA": 'Tiempo Promedio de Carga Urls SVE.csv',
            "TRABAJADOR": 'Tiempo Promedio de Carga Urls SVT.csv'
        }
script_directory = os.path.dirname(os.path.realpath(__file__))

def analizar_archivos_csv(ruta, keyword):
    try:
        # Leer los archivos CSV con los tiempos de carga cuyo comienzo sea igual a keyword
        archivos_csv = glob.glob(os.path.join(ruta, f"*{keyword}_*.csv"))[:10]
        df_completo = pd.DataFrame()

        for i, archivo in enumerate(archivos_csv):
            df = pd.read_csv(archivo)
            if i == 0:
                urls = df['URL'].tolist()
                df_completo = pd.DataFrame({'URL': urls})

            df_completo[f'Load Time {i+1}'] = df['Load Time']

        # Agregar columna con el promedio de tiempo de carga de las urls
        df_completo['Promedio Load Time'] = df_completo.iloc[:, 1:].mean(axis=1)

        if keyword in file_map:
            df_completo.to_csv(file_map[keyword], index=False, header=True)
            print(f"Archivo: {file_map[keyword]} Generado Satisfactoriamente")

        # Si los archivos en file_map existen en la ruta, generar un archivo con el promedio de tiempo de carga de las urls de todos los archivos
        #if all([os.path.exists(os.path.join(ruta, file_map[key])) for key, file_map[key] in file_map.items()]):
        #    df_completo.to_csv('Tiempo Promedio de Carga Urls COMPLETO.csv', index=False, header=True)
        #    print("Archivo Tiempo Promedio de Carga Urls COMPLETO.csv Generado Satisfactoriamente")

    except Exception as e:
        logging.error(f"Error al analizar archivos CSV: {e}")

def combinar_archivos_generados(ruta):
    # Si los archivos en file_map existen en la ruta, generar un archivo con el promedio de tiempo de carga de las urls de todos los archivos
    if all([os.path.exists(os.path.join(ruta, file_map[key])) for key, file_map[key] in file_map.items()]):
        # Combinar archivos de tiempo de carga de urls 
        archivos_csv = glob.glob(os.path.join(ruta, "Tiempo Promedio de Carga Urls*.csv"))
        df_completo = pd.DataFrame()

        # Crear un DataFrame que contenga todos los archivos CSV dejando solo las columnas URL y Promedio Load Time
        df_completo = pd.concat([pd.read_csv(archivo)[['URL', 'Promedio Load Time']] for archivo in archivos_csv], ignore_index=True)

        # Generar archivo con el promedio de tiempo de carga de las urls de todos los archivos
        df_completo.to_csv('Tiempo Promedio de Carga Urls COMPLETO.csv', index=False, header=True)
        print("Archivo: Tiempo Promedio de Carga Urls COMPLETO.csv Generado Satisfactoriamente")

# Eliminar archivos generados mas antiguos si existen mas de 10 para cada keyword
def eliminar_archivos_mas_antiguos(ruta, keyword):
    archivos_csv = glob.glob(os.path.join(ruta, f"*{keyword}*.csv"))
    if len(archivos_csv) > 10:
        archivos_csv.sort(key=os.path.getmtime)
        for archivo in archivos_csv[:-10]:
            os.remove(archivo)
            print(f"Archivo {archivo} eliminado satisfactoriamente") 
        
# Eliminar archivos generados mas antiguos si existen mas de 10 para cada keyword
#eliminar_archivos_mas_antiguos(script_directory, "PUBLICO")
#eliminar_archivos_mas_antiguos(script_directory, "EMPRESA")
#eliminar_archivos_mas_antiguos(script_directory, "TRABAJADOR")

# Analizar archivos CSV
#analizar_archivos_csv(script_directory, "PUBLICO")
#analizar_archivos_csv(script_directory, "EMPRESA")
#analizar_archivos_csv(script_directory, "TRABAJADOR")

# Combinar archivos generados
#combinar_archivos_generados(script_directory)


