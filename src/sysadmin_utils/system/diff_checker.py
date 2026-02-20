import os
import time
from pathlib import Path

def monitor_changes(folder_path: Path, log_file: Path):
    """
    Logs files and directories in a folder to a log file.
    """
    folder_path = Path(folder_path)
    log_file = Path(log_file)
    
    if not folder_path.exists():
        print(f"Folder not found: {folder_path}")
        return

    # Verificar si el archivo de registro existe
    if not log_file.exists():
        log_file.touch()

    # Obtener la fecha y hora actual
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    print(f"Logging changes for {folder_path} to {log_file}...")

    # Abrir el archivo de registro en modo de escritura (append)
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f'--- Estado de carpeta {folder_path} ({current_time}) ---\n')
        
        # Recorrer los archivos y subcarpetas de la carpeta
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(file_path)))
                f.write(f'Archivo: {file_path} ({modified_time})\n')

            for dir in dirs:
                dir_path = os.path.join(root, dir)
                modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(dir_path)))
                f.write(f'Carpeta: {dir_path} ({modified_time})\n')

        f.write('\n')

