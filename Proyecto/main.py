import sys
from fastapi import FastAPI, Query, HTTPException
from sis_recomendacion import cargar_datos, crear_columna_sentimiento, obtener_matriz_caracteristicas, calcular_similitud_coseno, recomendacion_juego

sys.path.append(r'C:\Users\Esteban García\OneDrive\Escritorio\LABs\PI MLOps - STEAM 01\Proyecto')

app = FastAPI()

df_steam_games, df_user_reviews, df_users_items = cargar_datos()
df_user_reviews = crear_columna_sentimiento(df_user_reviews)
user_item_matrix = obtener_matriz_caracteristicas(df_users_items)
item_similarity = calcular_similitud_coseno(user_item_matrix)

@app.get("/recomendacion_juego")
def recomendacion_juego_endpoint(title: str = Query(..., description="ID del juego")):
    return recomendacion_juego(title, user_item_matrix, item_similarity)
