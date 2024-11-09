from PIL import Image
import pytesseract

# Carga la imagen
image_path = 'image.png'
image = Image.open(image_path)

# Extrae el texto usando pytesseract
extracted_text = pytesseract.image_to_string(image)

# Formatea el texto para LaTeX (agrega encabezados, secciones, etc.)
latex_content = r"""\documentclass{article}
\usepackage{amsmath, amssymb}
\begin{document}

\section*{Extracted Text}
""" + extracted_text + r"""
\end{document}
"""

# Guarda el contenido en un archivo .tex
with open('output.tex', 'w', encoding='utf-8') as file:
    file.write(latex_content)

print("Archivo .tex generado con éxito.")