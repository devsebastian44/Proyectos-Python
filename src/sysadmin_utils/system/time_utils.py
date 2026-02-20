import os  # Importa la biblioteca `os` para interactuar con el sistema operativo.
import time  # Importa la biblioteca `time` para manejar el tiempo.
import datetime  # Importa la biblioteca `datetime` para trabajar con fechas y horas.

def modificar_fecha_carpeta(ruta_carpeta, nueva_fecha):
    # Convierte la nueva fecha en formato de tiempo de época (timestamp).
    nueva_fecha_tiempo = time.mktime(nueva_fecha.timetuple())

    # Modifica la fecha de acceso y modificación de la carpeta o archivo.
    os.utime(ruta_carpeta, (nueva_fecha_tiempo, nueva_fecha_tiempo))
    print("Fecha de creación modificada con éxito.")  # Mensaje para indicar que la operación fue exitosa.

# Ruta de la carpeta o archivo que deseas modificar.
# ruta = 'R:\\Nube\\Copia de Seguridad Completa\\Carpeta'  # Ejemplo de ruta en Windows.
ruta = 'D:\\Descargas\\Carpeta'  # Ruta actual del archivo o carpeta.

# Nueva fecha de creación (ejemplo: 4 de junio de 2023 a las 10:19 PM).
nueva_fecha = datetime.datetime(2023, 6, 4, 22, 19)

# Llama a la función para modificar la fecha de creación.
modificar_fecha_carpeta(ruta, nueva_fecha)
