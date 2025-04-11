import pandas as pd
import os
import re

# Define el directorio del script y del proyecto
SCRIPT_PATH = os.path.dirname(__file__)
PROJECTPATH = os.path.dirname(SCRIPT_PATH)

# Cargar URLs desde Excel
archivo_excel = os.path.join(PROJECTPATH, 'utils', 'URLs.xlsx')
df = pd.read_excel(archivo_excel, sheet_name="Redisenourlsraw")

print(f"Iniciando proceso de modificación de URLs en {archivo_excel}...")

# Verificar si la columna URL existe
df = df[['URL']].dropna()  # Eliminar valores NaN

# Expresión regular para validar URLs
url_pattern = re.compile(r'^(https?://[\w.-]+(?:/[^\s]*)?)$')

def limpiar_url(url):
    if not isinstance(url, str) or not url_pattern.match(url):
        return None  # Ignorar valores no válidos
    return url.split("!")[0]  # Eliminar todo desde "!"

# Aplicar la limpieza y filtrar valores válidos
df["URL_Modificada"] = df["URL"].apply(limpiar_url)
df = df.dropna(subset=["URL_Modificada"])  # Eliminar filas con valores no válidos

# Guardar las URLs modificadas en un archivo CSV
output_dir = os.path.join(PROJECTPATH, 'utils', 'output_data')
os.makedirs(output_dir, exist_ok=True)  # Asegurar que el directorio de salida existe
archivo_salida = "urls_modificadas.csv"
output_file = os.path.join(output_dir, archivo_salida)
df[["URL_Modificada"]].to_csv(output_file, index=False)

print(f"Proceso completado. {len(df)} URLs procesadas correctamente.")
print(f"Archivo guardado como {output_file}")





