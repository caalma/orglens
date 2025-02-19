# OrgLens

OrgLens es una herramienta de línea de comandos diseñada para analizar, buscar y convertir archivos `.org` (formato utilizado por **Org-mode** en Emacs). Es ideal para usuarios que necesitan gestionar grandes cantidades de notas, documentos o proyectos estructurados en formato `.org`.

Con OrgLens, puedes:
- Buscar términos específicos dentro de archivos `.org`.
- Filtrar secciones basadas en criterios positivos (`si`) y negativos (`no`).
- Exportar los resultados en múltiples formatos: `JSON`, `TXT`, `ORG`, `Markdown` y `CSV`.
- Procesar archivos comprimidos (`.zip`, `.tar.gz`) automáticamente.
- Usar un modo interactivo para realizar búsquedas repetidas sin reiniciar la herramienta.

---

## Tabla de Contenidos

1. [Requisitos](#requisitos)
2. [Instalación](#instalación)
3. [Uso](#uso)
   - [Modo directo](#modo-directo)
   - [Modo interactivo](#modo-interactivo)
4. [Ejemplos](#ejemplos)
5. [Características destacadas](#características-destacadas)
6. [Contribuciones](#contribuciones)
7. [Licencia](#licencia)

---

## Requisitos

- Python 3.6 o superior.
- Las siguientes bibliotecas de Python (se instalan automáticamente si usas `pip`):
  - `argparse`
  - `json`
  - `zipfile`
  - `tarfile`
  - `glob`
  - `shutil`

---

## Instalación

### Desde el repositorio

1. Clona el repositorio:
   ```bash
   git clone https://github.com/caalma/orglens.git
   cd orglens
   ```

2. (Opcional) Crea un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución directa

Si no deseas instalar el proyecto, puedes ejecutarlo directamente:
```bash
python orglens.py [argumentos]
```

---

## Uso

### Modo directo

El modo directo se utiliza para realizar búsquedas y exportaciones rápidas desde la línea de comandos.

#### Sintaxis
```bash
orglens [opciones] -i archivos_de_entrada
```

#### Opciones principales
| Opción       | Descripción                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `-s`         | Términos a buscar (`si`). Separados por espacios.                           |
| `-n`         | Términos a excluir (`no`). Separados por espacios.                          |
| `-f`         | Formato de salida en consola: `json`, `txt`, `org`, `md`, `csv`.             |
| `-o`         | Archivos de salida. El formato se determina por la extensión del archivo.    |
| `-i`         | Archivos `.org` de entrada (pueden ser patrones como `*.org` o comprimidos). |
| `-r`         | Usar expresiones regulares en la búsqueda.                                  |

#### Ejemplo
```bash
orglens -s "horno" -n "manteca" -f txt -o resultado.txt -i test/*.org
```

---

### Modo interactivo

El modo interactivo permite realizar múltiples búsquedas sin reiniciar la herramienta.

#### Ejecución
```bash
python orglens_interactive.py
```

#### Flujo interactivo
1. Ingresa los archivos `.org` a procesar (puedes usar patrones como `test/*.org` o archivos comprimidos).
2. Realiza búsquedas repetidas ingresando términos `si` y `no`.
3. Los resultados se muestran en la consola en formato `txt`.

---

## Ejemplos

### Búsqueda básica
Buscar "horno" en todos los archivos `.org` del directorio `test/`:
```bash
orglens -s "horno" -f txt -i test/*.org
```

### Filtrado con exclusión
Buscar "horno" pero excluir secciones que contengan "manteca":
```bash
orglens -s "horno" -n "manteca" -f org -i test/example.org
```

### Exportación a múltiples formatos
Exportar resultados en diferentes formatos:
```bash
orglens -s "horno" -o resultado.json resultado.txt resultado.org -i test/example.org
```

### Procesar archivos comprimidos
Procesar un archivo `.zip` que contiene archivos `.org`:
```bash
orglens -s "tipografia" -f md -o resultado.md -i test.zip
```

---

## Características destacadas

- **Soporte para archivos comprimidos**: Procesa archivos `.zip` y `.tar.gz` automáticamente.
- **Búsquedas avanzadas**: Usa expresiones regulares para búsquedas más flexibles.
- **Formatos de salida múltiples**: Exporta resultados en `JSON`, `TXT`, `ORG`, `Markdown` y `CSV`.
- **Modo interactivo**: Ideal para realizar búsquedas repetidas sin reiniciar la herramienta.
- **Optimización de rendimiento**: Procesa archivos grandes y múltiples archivos de manera eficiente.

---

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras un error o tienes una sugerencia, por favor abre un issue o envía un pull request en el repositorio.

Para contribuir:
1. Fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube los cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un pull request.

---

## Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.
