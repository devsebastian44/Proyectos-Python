# Data Utils

Herramientas para manejo de datos, archivos y bases de datos.

## Módulos

### `file_search.py`
Buscador recursivo de archivos por extensión.
- Rápido y eficiente usando `pathlib`.

**Uso desde CLI:**
```bash
python src/sysadmin_utils/main.py search "C:/Proyectos" "py"
```

### `db_connector.py`
Conector estandarizado para bases de datos MySQL.
- Usa variables de entorno para configuración (`DB_HOST`, `DB_USER`, etc.).
- implementa patrón Singleton para gestión de conexiones.

### `file_manager.py`
Gestor de archivos básico con interfaz gráfica (Tkinter).
- Permite seleccionar archivos y directorios mediante diálogos nativos.
