import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob

def cargar_datos():
    df_steam_games = pd.read_csv(r'C:\Users\Esteban García\OneDrive\Escritorio\LABs\PI MLOps - STEAM 01\Df procesados en csv\steam_games.csv')
    df_user_reviews = pd.read_csv(r'C:\Users\Esteban García\OneDrive\Escritorio\LABs\PI MLOps - STEAM 01\Df procesados en csv\user_reviews.csv')
    df_users_items = pd.read_csv(r'C:\Users\Esteban García\OneDrive\Escritorio\LABs\PI MLOps - STEAM 01\Df procesados en csv\users_items.csv')
    return df_steam_games, df_user_reviews, df_users_items

def crear_columna_sentimiento(df_user_reviews):
    df_user_reviews['recommend'] = df_user_reviews['reviews'].apply(
        lambda x: 1 if (isinstance(x, str) and TextBlob(x).sentiment.polarity > 0) else 0
    )
    return df_user_reviews

def obtener_matriz_caracteristicas(df_users_items):
    user_item_matrix = df_users_items.pivot_table(index='user_id', columns='title', values='playtime_forever', fill_value=0)
    return user_item_matrix

def calcular_similitud_coseno(user_item_matrix):
    item_similarity = cosine_similarity(user_item_matrix.T)
    return item_similarity

def recomendacion_juego(title, user_item_matrix, item_similarity):
    if title in user_item_matrix.columns:
        juego_seleccionado = user_item_matrix[title]
        sim_scores = list(enumerate(item_similarity[user_item_matrix.columns.get_loc(title)]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        juegos_similares = sim_scores[1:6]
        titulos_recomendados = [user_item_matrix.columns[i[0]] for i in juegos_similares]
        return {"recomendaciones": titulos_recomendados}
    else:
        raise HTTPException(status_code=404, detail="Juego no encontrado")
