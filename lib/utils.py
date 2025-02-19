import os
import shutil
import zipfile
import tarfile
import json

def clear_env(temp_dir):
    # Limpiar la carpeta temporal
    if os.path.exists(temp_dir):
        print(f"Borrando carpeta temporal: {temp_dir}")
        shutil.rmtree(temp_dir)

def show_init():
    print("Bienvenido al modo interactivo de OrgLens!\n")
    print("Puedes buscar términos en archivos .org y ver los resultados en tiempo real.")
    print("Escribe 'salir' en cualquier momento para terminar.\n")


def show_bye():
    print("\nGracias por usar OrgLens!")


def normalize_text(text):
    """
    Normaliza el texto eliminando acentos, convirtiendo a minúsculas y quitando signos raros.
    """
    import unicodedata
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    return text.lower()

def extract_files_from_archive(archive_path, temp_dir):
    """
    Extrae archivos .org de un archivo comprimido (.zip o .tar.gz) en el directorio temporal especificado.
    Devuelve una lista con las rutas absolutas de los archivos .org extraídos.
    """
    extracted_files = []

    # Crear la carpeta temporal si no existe
    os.makedirs(temp_dir, exist_ok=True)

    if archive_path.endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
    elif archive_path.endswith('.tar.gz'):
        with tarfile.open(archive_path, 'r:gz') as tar_ref:
            tar_ref.extractall(temp_dir)

    # Recorrer recursivamente el directorio temporal para encontrar todos los archivos .org
    for root, _, files in os.walk(temp_dir):
        for file in files:
            if file.endswith('.org'):
                full_path = os.path.join(root, file)
                extracted_files.append(full_path)

    # Depuración: Mostrar los archivos extraídos
    print(f"Archivos extraídos en '{temp_dir}':")
    for file in extracted_files:
        print(f" - {file}")

    return extracted_files


def export_results(results, output_format):
    """
    Exporta los resultados en el formato especificado (JSON, TXT, ORG, MD, CSV).
    """
    if output_format == 'json':
        return json.dumps(results, indent=4, ensure_ascii=False)
    elif output_format == 'txt':
        output = []
        for result in results:
            output.append("----------")  # Línea previa al título
            output.append(result['title'])  # Título sin '*'
            output.append("---")  # Línea posterior al título
            for item in result['content']:
                if isinstance(item, str):
                    output.append(item)
        return '\n'.join(output)
    elif output_format == 'org':
        output = []
        for result in results:
            output.append(f"* {result['title']}")
            for item in result['content']:
                if isinstance(item, str):
                    output.append(item)
        return '\n'.join(output)
    elif output_format == 'md':
        output = []
        for result in results:
            output.append(f"## {result['title']}")
            for item in result['content']:
                if isinstance(item, str):
                    output.append(item)
        return '\n'.join(output)
    elif output_format == 'csv':
        import csv
        import io
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Title', 'Content'])
        for result in results:
            content = '\n'.join(
                item if isinstance(item, str) else ''
                for item in result['content']
            )
            writer.writerow([result['title'], content])
        return output.getvalue()
    elif output_format == 'html':
        output = []
        output.append('<!DOCTYPE html>')
        output.append('<html lang="es">')
        output.append('<head>')
        output.append('    <meta charset="UTF-8">')
        output.append('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
        output.append('    <title>OrgLens - Resultados</title>')
        output.append('    <style>')
        output.append('        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }')
        output.append('        h1, h2, h3 { color: #333; }')
        output.append('        pre { background-color: #f4f4f4; padding: 10px; border-radius: 5px; }')
        output.append('        .section { margin-bottom: 30px; }')
        output.append('    </style>')
        output.append('</head>')
        output.append('<body>')
        output.append('    <h1>Resultados de OrgLens</h1>')

        for result in results:
            output.append('    <div class="section">')
            output.append(f'        <h2>{result["title"]}</h2>')
            for item in result['content']:
                if isinstance(item, str):
                    output.append(f'        <pre>{item}</pre>')
            output.append('    </div>')

        output.append('</body>')
        output.append('</html>')
        return '\n'.join(output)
    else:
        raise ValueError("Formato de salida no soportado.")
