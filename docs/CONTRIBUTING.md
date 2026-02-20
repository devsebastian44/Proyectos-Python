# Guía de Contribución

¡Gracias por tu interés en contribuir a **PySysTools**!

para asegurar la calidad del código, por favor sigue estos lineamientos:

## Estándares de Código

*   **Python Version**: El código debe ser compatible con Python 3.8+.
*   **Estilo**: Seguimos **PEP 8**. Usa nombres descriptivos para variables y funciones (en inglés, `snake_case`).
*   **Type Hits**: Usa `typing` para especificar tipos de argumentos y retorno.
    ```python
    def my_function(name: str, count: int) -> bool:
        ...
    ```

## Estructura de Módulos

*   Si añades una nueva utilidad, colócala en el sub-paquete apropiado (`security`, `network`, etc.).
*   Crea un archivo `__init__.py` si creas un nuevo directorio.
*   Actualiza `main.py` para exponer la nueva funcionalidad en el CLI.

## Tests

*   Añade tests unitarios en la carpeta `tests/`.
*   Ejecuta los tests antes de enviar tu cambio:
    ```bash
    python -m unittest discover tests
    ```

## Documentación

*   Si cambias funcionalidad, actualiza el `README.md` del módulo correspondiente.
*   documenta tus funciones usando docstrings.
