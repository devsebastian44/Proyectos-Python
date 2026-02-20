# PySysTools (sysadmin_utils)

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**Suite Profesional de Utilidades en Python para Administración de Sistemas, Seguridad y Redes.**

Este repositorio contiene una colección modular de herramientas diseñadas para automatizar tareas comunes de SysAdmins y mejorar la productividad. El código ha sido auditado y refactorizado para seguir principios de arquitectura limpia y escalabilidad.

## 🚀 Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/Proyectos-Python.git
   cd Proyectos-Python
   ```

2. **Crear entorno virtual (Recomendado):**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. **Instalar dependencias y el paquete:**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

## 🛠️ Uso del CLI

El proyecto incluye un CLI unificado (`main.py`) para acceder a todas las herramientas.

### Seguridad

**Generar contraseña segura:**
```bash
python src/sysadmin_utils/main.py gen-pass -l 20
```

**Escanear directorio en busca de malware (por hash):**
```bash
python src/sysadmin_utils/main.py scan-malware "C:/Downloads"
```

**Verificar hash de un archivo:**
```bash
python src/sysadmin_utils/main.py hash-check "archivo.exe"
```

### Redes

**Monitor de tráfico en tiempo real:**
```bash
python src/sysadmin_utils/main.py net-monitor
```

**Listar conexiones activas:**
```bash
python src/sysadmin_utils/main.py list-connections
```

**Probar conectividad a Internet:**
```bash
python src/sysadmin_utils/main.py check-internet
```

### Sistema y Datos

**Organizar archivos por extensión:**
```bash
python src/sysadmin_utils/main.py organize "C:/Users/Usuario/Downloads" --watch
```

**Buscar archivos por extensión:**
```bash
python src/sysadmin_utils/main.py search "C:/Proyectos" "py"
```

## 📂 Estructura del Proyecto

```text
src/
└── sysadmin_utils/
    ├── security/    # Hash utils, Malware scanner, Password manager
    ├── network/     # Traffic monitor, Connectivity, Active connections, FTP
    ├── system/      # Automation, Formatting, Power control
    ├── data/        # File search, DB connector, File manager
    ├── ui/          # Notifications, Windows, Calendar
    ├── utils/       # Config, Logger
    └── main.py      # CLI Entry point
```

## 🤝 Contribución

Si deseas contribuir, por favor sigue los estándares de código (PEP 8) y asegúrate de agregar tests para nuevas funcionalidades.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.