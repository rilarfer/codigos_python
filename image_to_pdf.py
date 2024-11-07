from PIL import Image, ImageOps

def image_to_pdf(image_path, pdf_path):
    try:
        # Tamaño carta en píxeles (8.5 x 11 pulgadas a 100 ppi)
        carta_width = int(8.5 * 100)
        carta_height = int(11 * 100)
        
        # Abre la imagen
        image = Image.open(image_path)
        
        # Convierte la imagen a modo RGB si es necesario
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Redimensiona la imagen manteniendo la proporción
        image.thumbnail((carta_width, carta_height))
        
        # Crea un fondo blanco del tamaño de una hoja carta
        background = Image.new('RGB', (carta_width, carta_height), (255, 255, 255))
        
        # Calcula la posición para centrar la imagen
        offset = ((carta_width - image.width) // 2, (carta_height - image.height) // 2)
        
        # Pega la imagen en el fondo
        background.paste(image, offset)
        
        # Guarda la imagen como un archivo PDF
        background.save(pdf_path, "PDF", resolution=100.0)
        print(f"Imagen convertida y guardada exitosamente en {pdf_path}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
image_path = 'imagen_recortada_carta.png'  # Reemplaza con la ruta de tu imagen
pdf_path = 'salida.pdf'    # Reemplaza con la ruta de salida del PDF
image_to_pdf(image_path, pdf_path)