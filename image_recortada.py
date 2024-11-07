from PIL import Image

def crop_image_to_content(image_path, output_path):
    # Cargar la imagen
    image = Image.open(image_path)

    # Convertir la imagen a modo RGBA si no lo está
    image = image.convert("RGBA")

    # Obtener las dimensiones de la imagen
    width, height = image.size
    pixels = image.load()

    # Encontrar los límites del contenido (no blanco)
    left, top, right, bottom = width, height, 0, 0
    for y in range(height):
        for x in range(width):
            if pixels[x, y] != (255, 255, 255, 255):  # Pixel no es blanco
                left = min(left, x)
                top = min(top, y)
                right = max(right, x)
                bottom = max(bottom, y)

    if left < right and top < bottom:
        # Recortar la imagen utilizando los nuevos límites
        cropped_image = image.crop((left, top, right + 1, bottom + 1))
        cropped_image.save(output_path)
        print(f"Imagen recortada guardada en {output_path}")
    else:
        print("No se encontró contenido en la imagen para recortar.")

# Usar la función con un ejemplo
crop_image_to_content('Portada libro 2011.png', 'imagen_recortada.png')
