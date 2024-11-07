import os
from PyPDF2 import PdfMerger

def merge_pdfs_from_folder(folder_path, output_path):
    # Crear un objeto PdfMerger
    merger = PdfMerger()

    # Obtener la lista de archivos PDF en la carpeta
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    # Asegurarse de que los archivos estén en orden alfabético
    pdf_files.sort()

    # Mostrar el orden de los archivos a combinar
    print("Orden de los archivos PDF a combinar:")
    for pdf in pdf_files:
        print(pdf)

    # Añadir cada archivo PDF a la fusión
    for pdf in pdf_files:
        pdf_path = os.path.join(folder_path, pdf)
        merger.append(pdf_path)

    # Escribir el archivo PDF combinado
    merger.write(output_path)
    merger.close()
    print(f"Archivos PDF combinados guardados en {output_path}")

# Usar la función con un ejemplo
merge_pdfs_from_folder('.', 'archivo_combinado.pdf')