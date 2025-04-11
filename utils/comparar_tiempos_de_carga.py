import pandas as pd
import smtplib
from email.message import EmailMessage
import time
import os

# Obtener la ruta del directorio del script actual
script_directory = os.path.dirname(os.path.realpath(__file__))

# Unir la ruta del directorio con el nombre del archivo URLs.xlsx
#archivo_excel = os.path.join(script_directory, "URLs.xlsx")

file_map = {
            "PUBLICO": 'Alertas Tiempos de Carga PUBLICO.csv',
            "EMPRESA": 'Alertas Tiempos de Carga EMPRESA.csv',
            "TRABAJADOR": 'Alertas Tiempos de Carga TRABAJADOR.csv'
        }

nralertas = 0
df_alert = ""

# Verificar si existe el archivo Alertas Tiempos de Carga
def eliminar_archivo_alertas():
    if os.path.exists(os.path.join(script_directory, "Alertas Tiempos de Carga*.csv")):
        os.remove(os.path.join(script_directory, "Alertas Tiempos de Carga*.csv"))
        print("Archivos previoss: Alertas Tiempos de Carga.csv eliminado.")
        print("--------------------------------------------------------------------------------------")
    else:
        print("No existen archivos previos de alertas.")
        print("--------------------------------------------------------------------------------------")    

# Metodo para comparar los tiempos de carga de las urls en el archivo TRABAJADOR_navigation_load_times {file_time}.csv con el archivoTiempo Promedio de Carga Urls COMPLETO SVT.csv
def comparar_tiempos_carga(df1file, df2file):
    try:
        # Leer los archivos CSV con los tiempos de carga
        df1 = pd.read_csv(df1file)
        df2 = pd.read_csv(df2file)
        nralertas = 0

        # analizar df1 para obtener el keyword para el archivo de alertas
        global keyword
        keyword = df1file.split("_")[0] 

        # Crear una lista para almacenar las filas que cumplen la condición
        alertas = []

        # Recorrer las filas de ambos DataFrames y comparar los tiempos de carga
        print("Revision de registros de Tiempos de carga:")
        for _, row1 in df1.iterrows():
            url1 = row1['URL']
            load_time1 = row1['Load Time']

            for _, row2 in df2.iterrows():
                url2 = row2['URL']
                load_time2 = row2['Promedio Load Time']

                # Si las URLs coinciden, comparar los tiempos de carga
                if url1 == url2:
                    # si el load_time1 es mayor que el load_time2 y la diferencia es mayor a 5 segundos
                    if load_time1 > load_time2 and (load_time1 - load_time2) > 5:
                        print(f"La URL {url1} tiene un tiempo de carga mayor que en COMPLETO")
                        nralertas += 1
                        # Agregar la fila a la lista de alertas
                        alertas.append([url1, load_time1, load_time2, load_time1 - load_time2])

        # Crear un DataFrame a partir de la lista de alertas
        df_alertas = pd.DataFrame(alertas, columns=["URL", "Load Time", "Load Time COMPLETO", "Diferencia"])
        # Guardar el DataFrame como un archivo CSV
        df_alertas.to_csv(f"{file_map[keyword]}", index=False)
        # Guardar el nombre del archivo de alertas para enviar por correo electrónico en una variable global
        global df_alert
        df_alert = f"{file_map[keyword]}"

        print(f"Nro. Alertas encontradas: {nralertas}")
        print(f"Archivo de Alertas: {file_map[keyword]}")
        # Si no se encontraron diferencias en los tiempos de carga, mostrar un mensaje
        if nralertas == 0:
            print("No se encontraron Alertas en los tiempos de carga.")
        print("--------------------------------------------------------------------------------------")
    except Exception as e:
        print(f"Error al comparar tiempos de carga: {e}")


def enviar_alerta():
    try:
        # Verificar si existe algún archivo de alertas
        if os.path.exists(os.path.join(script_directory, f"{df_alert}")):
            #print("Archivo de Alertas encontrado.")
            df = pd.read_csv(os.path.join(script_directory, f"{df_alert}"))
            # Leer el archivo .csv con las alertas
            df = pd.read_csv(f"{df_alert}")
            alertlist = df.values.tolist()
            
            # Si hay alertas, enviar un correo electrónico
            if not df.empty:
                # Preparar el correo electrónico
                remitente = "navaharoja@gmail.com"
                destinatario = "hernan.hernesto.acosta@ibm.com"
                destinatarios = ["hernan.hernesto.acosta@ibm.com"]
                subject = f"Alerta: URLs {keyword} con tiempos de carga incremendados"
                mensaje = f"Se han encontrado {len(alertlist)} alertas de tiempos de carga. \n\n" \
                            f"Adjunto se encuentra el archivo con las alertas.\n\n" \
                            

                email = EmailMessage()
                email["From"] = remitente
                email["To"] = ", ".join(destinatarios)  # Convertir la lista de destinatarios a una cadena separada por comas
                email["Subject"] = subject
                email.set_content(mensaje)
                email.add_attachment(open(f"{df_alert}", "r").read(), filename=f"{df_alert}") # Adjuntar el archivo de alertas
                
            
                # Enviar el correo electrónico
                try:
                    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
                    smtp.login(remitente, "blte qyev zzlz amcb")  # Usar la contraseña de la aplicación
                    smtp.send_message(email)
                    print("Correo electrónico de alerta enviado.")
                    print("--------------------------------------------------------------------------------------")
                except Exception as e:
                    print("--------------------------------------------------------------------------------------")
                    print(f"Error al enviar el correo electrónico: {e}")
                    print("--------------------------------------------------------------------------------------")
                finally:
                    smtp.quit()  # Asegurarse de cerrar la conexión SMTP

        else:
            print("No se encontraron alertas.")
            print("--------------------------------------------------------------------------------------")
            # Si no hay alertas, salir de la función
            return    
        
    except Exception as e:
        if e == "[Errno 2] No such file or directory: 'Alertas Tiempos de Carga TRABAJADOR.csv'":
            print(f"Sin envio de Alertas... Archivo: [{df_alert}] no encontrado")
        else:
            print(f"{e}")    


# main
#if __name__ == "__main__":
    # Guardar el tiempo de inicio
    #start_time = time.time()

    # Eliminar el archivo Alertas Tiempos de Carga TRABAJADOR.csv si existe
    #eliminar_archivo_alertas()
    # comparar tiempos de carga
    #ft = "202405201359"
    #comparar_tiempos_carga(f"TRABAJADOR_navigation_load_times {ft}.csv", 'Tiempo Promedio de Carga Urls COMPLETO.csv')
    #comparar_tiempos_carga(f"EMPRESA_navigation_load_times {ft}.csv", 'Tiempo Promedio de Carga Urls COMPLETO.csv')
    #comparar_tiempos_carga(f"PUBLICO_navigation_load_times {ft}.csv", 'Tiempo Promedio de Carga Urls COMPLETO.csv')
    # Enviar alerta por correo electrónico si hay diferencias en los tiempos de carga
    #enviar_alerta()

    # Guardar el tiempo de finalización
    #end_time = time.time()

    # Calcular y mostrar el tiempo total de ejecución
    #total_time = end_time - start_time
    #hours, remainder = divmod(total_time, 3600)
    #minutes, seconds = divmod(remainder, 60)
    #formatted_time = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
    #print(f"Tiempo total de ejecución: {formatted_time}")
    #print("Fecha y Hora de Finalización: ", time.strftime("%Y-%m-%d %H:%M:%S"))
    #print("--------------------------------------------------------------------------------------")            
    

        
