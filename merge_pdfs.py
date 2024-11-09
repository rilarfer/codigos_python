from PyPDF2 import PdfMerger
import os

def merge_pdfs(pdf_list, output_path):
    # Crear un objeto PdfMerger
    merger = PdfMerger()

    try:
        # Añadir cada archivo PDF a la fusión
        for pdf in pdf_list:
            if os.path.exists(pdf):
                merger.append(pdf)
            else:
                print(f"Advertencia: El archivo '{pdf}' no existe y será omitido.")
        
        # Escribir el archivo PDF combinado
        merger.write(output_path)
        print(f"Archivos PDF combinados guardados en {output_path}")
    except Exception as e:
        print(f"Error al combinar los archivos PDF: {e}")
    finally:
        merger.close()

# Usar la función con un ejemplo
merge_pdfs(['00_Portada.pdf', '01_Portada Interna MII.pdf', '02_Presentación.pdf', '03_Índice.pdf', '04_INTEGRAL INDEFINIDA.pdf', '05_LA INTEGRAL DEFINIDA.pdf', '06_EL SISTEMA DE COORDENADAS POLARES.pdf', '07_APLICACIONESDE LA INTEGRAL DEFINIDA.pdf', '08_SUCESIONES y SERIES F.pdf', '09_FORMULARIO.pdf'], 'archivo_combinado.pdf')