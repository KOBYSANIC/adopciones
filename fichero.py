import re
import unicodedata

def eliminar_tildes(texto):
    texto_sin_tildes = ''.join(
        (c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    )
    return texto_sin_tildes.lower()
def contar_articulo_el(texto):
    return len(re.findall(r'\bel\b', texto, re.IGNORECASE))

def procesar_fichero(nombre_fichero):
   
    with open(nombre_fichero, 'r', encoding='latin-1') as f:
        contenido = f.read()

    lineas = contenido.splitlines()
    num_lineas = len(lineas)

    num_eles = contar_articulo_el(contenido)

    contenido_procesado = eliminar_tildes(contenido)

    with open('C:/Users/marv_/OneDrive/Documentos/IA Proyecto2/resultado.txt', 'w', encoding='utf-8') as f:
        f.write(f"Número de líneas: {num_lineas}\n")
        f.write(f"Número de El es: {num_eles}\n")
        f.write(contenido_procesado)

nombre_fichero = 'C:/Users/marv_/OneDrive/Documentos/IA Proyecto2/FicheroALeer.txt' 
procesar_fichero(nombre_fichero)
