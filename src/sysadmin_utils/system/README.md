# System Utils

Herramientas para automatización y control del Sistema Operativo.

## Módulos

### `formatting.py` (File Organizer)
Organizador automático de archivos según su extensión.
- Mueve archivos a carpetas como `images/`, `documents/`, `programs/`, etc.
- Modo "Watch" para monitorear una carpeta en tiempo real.

**Uso desde CLI:**
```bash
# Organizar una vez
python src/sysadmin_utils/main.py organize "C:/Downloads"

# Monitorear carpeta continuamente
python src/sysadmin_utils/main.py organize "C:/Downloads" --watch
```

### `automation.py`
Scripts de automatización de tareas varias (ej. menús interactivos, simulación de teclas).

### `power_control.py`
Utilidades para gestión de energía (Apagar, Reiniciar).
*Nota: Requiere permisos de administrador.*

### `time_utils.py`
Utilidades relacionadas con fechas y horas del sistema.

### `diff_checker.py`
Herramienta para detectar cambios en archivos o directorios.

