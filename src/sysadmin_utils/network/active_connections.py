import psutil  # Importa la librería `psutil` para interactuar con procesos y conexiones del sistema.
import socket  # Importa la librería `socket` para trabajar con direcciones de red y puertos.

def get_remote_connections():  # Define una función para obtener las conexiones remotas activas.
    remote_connections = []  # Inicializa una lista para almacenar las conexiones remotas.
    for conn in psutil.net_connections(kind='inet'):  # Itera sobre todas las conexiones de red activas (tipo 'inet').
        if conn.status == psutil.CONN_ESTABLISHED:  # Filtra las conexiones que están establecidas (en uso).
            local_address, local_port = conn.laddr  # Obtiene la dirección local y el puerto.
            remote_address, remote_port = conn.raddr  # Obtiene la dirección remota y el puerto.
            process = psutil.Process(conn.pid)  # Obtiene el proceso que está utilizando la conexión.
            remote_connections.append({  # Agrega la información de la conexión a la lista.
                'Local Address': f"{local_address}:{local_port}",
                'Remote Address': f"{remote_address}:{remote_port}",
                'Process Name': process.name(),
                'Process ID': conn.pid,
            })
    return remote_connections  # Devuelve la lista de conexiones remotas activas.

def main():  # Función principal que maneja la ejecución del script.
    remote_connections = get_remote_connections()  # Obtiene la lista de conexiones remotas activas.
    if remote_connections:  # Si existen conexiones remotas activas.
        for conn in remote_connections:  # Itera sobre cada conexión remota.
            print("Local Address:", conn['Local Address'])  # Muestra la dirección local.
            print("Remote Address:", conn['Remote Address'])  # Muestra la dirección remota.
            print("Process Name:", conn['Process Name'])  # Muestra el nombre del proceso que usa la conexión.
            print("Process ID:", conn['Process ID'])  # Muestra el ID del proceso.
            print("-" * 40)  # Imprime una línea separadora entre las conexiones.
    else:  # Si no hay conexiones remotas activas.
        print("No remote connections found.")  # Muestra un mensaje indicando que no se encontraron conexiones.

if __name__ == "__main__":  # Verifica si el script está siendo ejecutado directamente.
    main()  # Llama a la función principal para ejecutar el script.
