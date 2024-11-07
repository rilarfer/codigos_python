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
merge_pdfs(['00 Portada.pdf', '01 Portada Interna.pdf', '02 Presentación.pdf', '03 Índice.pdf', '04 Matrices.pdf', '05 Geometria Analitica Vectorial.pdf', '06 Límites.pdf', '07 Teoría de Derivadas.pdf', '08 Aplicaciones de la Derivada.pdf', '09 Apéndice.pdf', '10 Contraportada.pdf'], 'archivo_combinado_2.pdf')