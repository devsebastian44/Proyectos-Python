# Network Utils

Herramientas para monitoreo, diagnóstico y gestión de redes.

## Módulos

### `traffic_monitor.py`
Monitor de tráfico de red en tiempo real.
- Muestra velocidad de subida/bajada por interfaz.
- Interfaz de consola que se actualiza automáticamente.

**Uso desde CLI:**
```bash
python src/sysadmin_utils/main.py net-monitor --delay 0.5
```

### `connectivity.py`
Pruebas de conectividad a Internet.
- Realiza peticiones HTTP para verificar acceso a la web.

**Uso desde CLI:**
```bash
python src/sysadmin_utils/main.py check-internet
```

### `active_connections.py`
Listado de conexiones activas del sistema.
- Muestra procesos locales conectados a direcciones remotas.
- Útil para detectar actividad sospechosa o depurar servicios.

**Uso desde CLI:**
```bash
python src/sysadmin_utils/main.py list-connections
```

### `ftp/`
Cliente FTP unificado.
- `ftp_client.py`: Clase `FTPClient` envuelta en el CLI principal.
- Soporta: `list`, `upload`, `download`.

**Uso desde CLI:**
```bash
python src/sysadmin_utils/main.py ftp list --host ftp.example.com --user usuario --password clave
```


### `samba_enum.py`
Enumeración de recursos compartidos SMB/Samba.

### `downloader.py`
Gestor de descargas de archivos desde URLs.

