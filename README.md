# OrgLens

OrgLens es una herramienta de línea de comandos diseñada para analizar, buscar y convertir archivos `.org` (formato utilizado por **Org-mode** en Emacs). Es ideal para usuarios que necesitan gestionar grandes cantidades de notas, documentos o proyectos estructurados en formato `.org`.

Con OrgLens, puedes:
- Buscar términos específicos dentro de archivos `.org`.
- Filtrar secciones basadas en criterios positivos (`si`) y negativos (`no`).
- Exportar los resultados en múltiples formatos: `JSON`, `TXT`, `ORG`, `Markdown`, `HTML` y `CSV`.
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

- Python 3.8 o superior.
- Las siguientes bibliotecas de Python (se instalan automáticamente si usas `pip`):
  - `argparse`
  - `json`
  - `zipfile`
  - `tarfile`
  - `glob`
  - `shutil`

---

## Instalación

### Descarga repositorio

1. Clona el repositorio:
   ```bash
   git clone https://github.com/caalma/orglens.git
   cd orglens
   ```

2. Ejecución directa
   ```bash
   orglens-direct [argumentos]
   ```

---

## Uso

### Modo directo

El modo directo se utiliza para realizar búsquedas y exportaciones rápidas desde la línea de comandos.

#### Sintaxis
```bash
orglens-direct [opciones] -i archivos_de_entrada
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
orglens-direct -s "horno" -n "manteca" -f txt -o resultado.txt -i test/*.org
```

---

### Modo interactivo

El modo interactivo permite realizar múltiples búsquedas sin reiniciar la herramienta.

#### Ejecución
```bash
orglens-interactive
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
orglens-direct -s "horno" -f txt -i test/*.org
```

### Filtrado con exclusión
Buscar "horno" pero excluir secciones que contengan "manteca":
```bash
orglens-direct -s "horno" -n "manteca" -f org -i test/example.org
```

### Exportación a múltiples formatos
Exportar resultados en diferentes formatos:
```bash
orglens-direct -s "horno" -o resultado.json resultado.txt resultado.org -i test/example.org
```

### Procesar archivos comprimidos
Procesar un archivo `.zip` que contiene archivos `.org`:
```bash
orglens-direct -s "tipografia" -f md -o resultado.md -i test.zip
```

---

## Características destacadas

- **Soporte para archivos comprimidos**: Procesa archivos `.zip` y `.tar.gz` automáticamente.
- **Búsquedas avanzadas**: Usa expresiones regulares para búsquedas más flexibles.
- **Formatos de salida múltiples**: Exporta resultados en `JSON`, `TXT`, `ORG`, `Markdown`, `HTML` y `CSV`.
- **Modo interactivo**: Ideal para realizar búsquedas repetidas sin reiniciar la herramienta.
- **Optimización de rendimiento**: Procesa archivos grandes y múltiples archivos de manera eficiente.


---

## Utilidades complementarias


### Autocompletado para Bash

OrgLens incluye soporte para autocompletado en la terminal Bash. Esto permite sugerir opciones, formatos de salida y archivos `.org` mientras usas el comando `orglens-direct`.

#### Instalación del autocompletado
Para habilitar el autocompletado, asegúrate de que el archivo `orglens-completion.bash` esté en tu sistema y ejecuta el siguiente comando:

```bash
source /ruta/al/archivo/orglens-completion.bash
```

También puedes agregar esta línea a tu archivo `~/.bashrc` para que el autocompletado esté disponible automáticamente en todas tus sesiones:

```bash
echo "source /ruta/al/archivo/orglens-completion.bash" >> ~/.bashrc
source ~/.bashrc
```

#### Funcionalidades del autocompletado
- Sugerencias para opciones como `-s`, `-n`, `-f`, `-o`, `-i`, etc.
- Completado automático de formatos de salida (`json`, `txt`, `org`, `md`, `csv`, `html`).
- Completado automático de archivos `.org` y patrones como `*.org`.



### Instalador en Bash

OrgLens incluye un instalador en Bash que simplifica la configuración inicial. Este instalador realiza las siguientes tareas:
- Configura el autocompletado para Bash.
- Crea enlaces simbólicos para `orglens-direct` y `orglens-interactive` en el directorio `~/.local/bin/`.

#### Uso del instalador
1. Haz el script ejecutable:
   ```bash
   chmod +x install-orglens.sh
   ```

2. Ejecuta el instalador:
   ```bash
   ./install-orglens.sh
   ```

3. Recarga tu shell para aplicar los cambios:
   ```bash
   source ~/.bashrc
   ```

#### Qué hace el instalador
- Agrega el autocompletado al archivo `~/.bashrc`.
- Aplica permisos de ejecución a `orglens-direct` y a `orglens-interactive`.
- Crea enlaces simbólicos para los scripts principales:
  - `orglens-direct` → `~/.local/bin/orglens-direct`
  - `orglens-interactive` → `~/.local/bin/orglens-interactive`

Con el instalador, tendrás acceso rápido a OrgLens desde cualquier ubicación en tu terminal.



### Módulo para Emacs

OrgLens incluye un módulo para Emacs que permite interactuar con `orglens-direct` directamente desde el editor. Este módulo facilita la ejecución de búsquedas y la visualización de resultados en un buffer dedicado.

#### Instalación del módulo
1. Guarda el archivo `orglens.el` en tu directorio de configuración de Emacs (por ejemplo, `~/.emacs.d/lisp/`).

2. Añade las siguientes líneas a tu archivo de configuración de Emacs (`~/.emacs` o `~/.emacs.d/init.el`):
   ```elisp
   (add-to-list 'load-path "~/.emacs.d/lisp/")
   (require 'orglens)
   ```

3. Reinicia Emacs o evalúa el archivo de configuración:
   ```elisp
   M-x eval-buffer
   ```

#### Uso del módulo
- Ejecuta el comando interactivo:
  ```elisp
  M-x orglens-search
  ```

- Ingresa los parámetros solicitados:
  - Términos a buscar (`si`).
  - Términos a excluir (`no`) (opcional).
  - Formato de salida (`txt`, `json`, `org`, etc.).
  - Archivos/patrones de entrada (por ejemplo, `*.org test/*.org`).
  - Archivos de salida (por ejemplo, `resultado.html`).

Los resultados se mostrarán en un buffer llamado `*OrgLens Results*`.

#### Características del módulo
- Soporte para múltiples archivos o patrones de entrada.
- Interpretación de rutas relativas al directorio actual.
- Visualización de resultados en un buffer de solo lectura.
- Soporte para indicar archivos de salida.


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
