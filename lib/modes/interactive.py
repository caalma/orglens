import sys
import os
import glob
import readline
from lib.orgparser import OrgParser
from lib.utils import *

def interactive_mode():
    """
    Modo interactivo: Permite realizar búsquedas repetidas en archivos .org.
    """
    show_init()

    # Carpeta temporal para archivos comprimidos
    temp_dir = "./--tmp_zip_files--/"
    valid_files = []

    try:
        # Solicitar archivos de entrada
        input_pattern = input("Ingrese los archivos .org a procesar (puedes usar patrones como 'ruta/*.org' o archivos comprimidos): ").strip()
        if input_pattern.lower() == "salir":
            print("Saliendo...")
            sys.exit(0)

        # Expandir patrones
        input_files = glob.glob(input_pattern)
        if not input_files:
            print(f"No se encontraron archivos que coincidan con el patrón '{input_pattern}'. Saliendo...")
            sys.exit(0)

        # Procesar cada archivo de entrada
        for file in input_files:
            if file.endswith('.zip') or file.endswith('.tar.gz'):
                # Extraer archivos comprimidos
                extracted_files = extract_files_from_archive(file, temp_dir)
                valid_files.extend(extracted_files)
            elif os.path.exists(file):
                # Archivos individuales
                valid_files.append(file)
            else:
                print(f"El archivo '{file}' no existe y será ignorado.")

        if not valid_files:
            print("No se encontraron archivos válidos. Saliendo...")
            sys.exit(0)

        # Bucle interactivo
        while True:
            try:
                print("\n___________ NUEVA BÚSQUEDA ___________")
                search_terms = input("Ingrese términos a buscar ('si') separados por comas (o 'salir'): ").strip()
                if search_terms.lower() == "salir":
                    print("Saliendo...")
                    break

                negative_terms = input("Ingrese términos a excluir ('no') separados por comas (opcional): ").strip()
                use_regex = input("¿Usar expresiones regulares? (s/n): ").strip().lower() == "s"

                # Parsear términos
                search_terms = [term.strip() for term in search_terms.split(",") if term.strip()]
                negative_terms = [term.strip() for term in negative_terms.split(",") if term.strip()]

                # Procesar archivos
                all_results = []
                for file in valid_files:
                    parser = OrgParser()
                    try:
                        tree = parser.parse(file)
                        results = parser.search(search_terms, negative_terms, use_regex)
                        all_results.extend(results)
                    except Exception as e:
                        print(f"Error al procesar el archivo '{file}': {e}")

                # Mostrar resultados
                if all_results:
                    print("\n___________ RESULTADOS ___________")
                    output = export_results(all_results, "txt")
                    print(output)
                else:
                    print("No se encontraron coincidencias.")

            except KeyboardInterrupt:
                print("\nInterrupción detectada. Volviendo al menú principal...")

    except KeyboardInterrupt:
        print("\nInterrupción detectada. Saliendo limpiamente...")
        clear_env(temp_dir)
        show_bye()
        exit()

    finally:
        clear_env(temp_dir)

    show_bye()
