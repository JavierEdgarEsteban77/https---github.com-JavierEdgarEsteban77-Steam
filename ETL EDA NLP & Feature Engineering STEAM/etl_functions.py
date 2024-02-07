# etl_functions.py
import json
import pandas as pd
import ast
import gzip
from tqdm import tqdm

def leer_datos(ruta, tipo='json'):
    """
    Esta función lee datos desde cada archivo de mi carpeta y los convierte en un DataFrame de pandas.

    Args:
        ruta (str): La ruta al archivo que se va a leer.
        tipo (str, optional): El formato de los datos en el archivo. Puede ser 'json' o 'literal'. 
                              Si es 'json', los datos se cargarán utilizando json.loads. 
                              Si es 'literal', los datos se cargarán utilizando ast.literal_eval. 
                              Por defecto es 'json'.

    Returns:
        pd.DataFrame: Un DataFrame de pandas que contiene los datos leídos del archivo.
    """
    filas = []  # Será la lista para almacenar cada fila de datos

    # Abro el archivo en modo lectura con codificación utf-8
    with gzip.open(ruta, 'rt', encoding='utf-8') as f:
        # Leo cada línea del archivo
        for line in tqdm(f.readlines(), desc=f"Leyendo {ruta}"):
            # Si el tipo es 'json', carga los datos con json.loads
            if tipo == 'json':
                data = json.loads(line)
            # Si el tipo es 'literal', carga los datos con ast.literal_eval
            elif tipo == 'literal':
                data = ast.literal_eval(line)
            # Añado los datos a la lista de filas
            filas.append(data)

    # Convierto la lista de filas en un DataFrame de pandas y lo devuelve.
    return pd.DataFrame(filas)
