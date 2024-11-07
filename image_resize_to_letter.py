from PIL import Image

def resize_to_letter_size(image_path, output_path):
    # Cargar la imagen
    image = Image.open(image_path)

    # Redimensionar la imagen al tamaño de una hoja carta (8.5 x 11 pulgadas a 300 DPI)
    carta_width, carta_height = int(8.5 * 300), int(11 * 300)
    resized_image = image.resize((carta_width, carta_height), Image.LANCZOS)

    # Guardar la imagen con la resolución DPI especificada
    resized_image.save(output_path, dpi=(300, 300))
    print(f"Imagen redimensionada a tamaño carta guardada en {output_path}")

resize_to_letter_size('imagen_recortada.png', 'imagen_recortada_carta.png')