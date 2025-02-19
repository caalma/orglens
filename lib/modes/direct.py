import os
import sys
import glob
from argparse import ArgumentParser
from lib.utils import *
from lib.orgparser import OrgParser

def direct_mode():
    """
    Modo directo: Procesa archivos según los argumentos de línea de comandos.
    """
    parser = ArgumentParser(description="Analizador y buscador de archivos .org")
    parser.add_argument('-s', nargs='+', help="Texto(s) a buscar ('si')")
    parser.add_argument('-n', nargs='+', help="Texto(s) que NO deben contenerse ('no')")
    parser.add_argument('-f', choices=['json', 'txt', 'org', 'md', 'csv', 'html'], default='txt', help="Formato de salida en consola")
    parser.add_argument('-o', nargs='+', help="Archivo(s) de salida (formato determinado por la extensión)")
    parser.add_argument('-i', nargs='+', required=True, help="Archivos .org de entrada")
    parser.add_argument('-r', action='store_true', help="Usar expresiones regulares en la búsqueda")
    args = parser.parse_args()

    # Validaciones
    if not args.i:
        print("Debe proporcionar al menos un archivo .org de entrada usando -i.")
        sys.exit(1)

    # Procesamiento
    all_results = []
    files_to_process = []

    # Carpeta temporal
    temp_dir = "./--tmp_zip_files--/"

    try:
        # Expandir archivos comprimidos
        for input_file in args.i:
            if input_file.endswith('.zip') or input_file.endswith('.tar.gz'):
                extracted_files = extract_files_from_archive(input_file, temp_dir)
                files_to_process.extend(extracted_files)
            else:
                files_to_process.append(input_file)

        # Validar que los archivos existan antes de procesarlos
        valid_files = []
        for file in files_to_process:
            if os.path.exists(file):
                valid_files.append(file)
            else:
                print(f"Archivo no encontrado: {file}")

        if not valid_files:
            print("No se encontraron archivos válidos para procesar. Saliendo...")
            sys.exit(1)

        # Procesar archivos
        for file in valid_files:
            parser = OrgParser()
            try:
                tree = parser.parse(file)
                results = parser.search(args.s, args.n, args.r)
                all_results.extend(results)
            except Exception as e:
                print(f"Error al procesar el archivo '{file}': {e}")

        # Salida en consola
        console_output = export_results(all_results, args.f)
        print(console_output)

        # Salida en archivos
        if args.o:
            for output_file in args.o:
                _, ext = os.path.splitext(output_file)
                if ext not in ['.json', '.txt', '.org', '.md', '.csv', '.html']:
                    print(f"Extensión no soportada para el archivo: {output_file}")
                    continue

                output_format = ext[1:]  # Eliminar el punto (e.g., '.json' -> 'json')
                file_output = export_results(all_results, output_format)

                with open(output_file, 'w', encoding='utf-8') as outfile:
                    outfile.write(file_output)

    finally:
        clear_env(temp_dir)
