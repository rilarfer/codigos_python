from PIL import Image
import pytesseract
from googletrans import Translator

# Carga la imagen
image_path = 'image.png'
image = Image.open(image_path)

# Extrae el texto usando pytesseract
extracted_text = pytesseract.image_to_string(image)

# Traduce el texto al español
translator = Translator()
translated_text = translator.translate(extracted_text, src='en', dest='es').text

# Formatea el texto para LaTeX
latex_content = r"""\documentclass{article}
\usepackage{amsmath, amssymb}
\begin{document}

\section*{Texto Extraído (Traducido)}
""" + translated_text + r"""
\end{document}
"""

# Guarda el contenido en un archivo .tex
with open('output_translated.tex', 'w', encoding='utf-8') as file:
    file.write(latex_content)

print("Archivo .tex traducido generado con éxito.")
