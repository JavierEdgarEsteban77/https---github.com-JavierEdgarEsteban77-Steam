{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Vamos a crear un sistema de recomendación sentimientos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.metrics.pairwise import cosine_similarity\n",
    "from textblob import TextBlob\n",
    "\n",
    "def cargar_datos():\n",
    "    df_steam_games = pd.read_csv('ruta_al_archivo_steam_games.csv')  # Reemplaza con la ruta correcta\n",
    "    df_user_reviews = pd.read_csv('ruta_al_archivo_user_reviews.csv')  # Reemplaza con la ruta correcta\n",
    "    df_users_items = pd.read_csv('ruta_al_archivo_users_items.csv')  # Reemplaza con la ruta correcta\n",
    "    return df_steam_games, df_user_reviews, df_users_items\n",
    "\n",
    "def crear_columna_sentimiento(df_user_reviews):\n",
    "    df_user_reviews['recommend'] = df_user_reviews['reviews'].apply(\n",
    "        lambda x: 1 if (isinstance(x, str) and TextBlob(x).sentiment.polarity > 0) else 0\n",
    "    )\n",
    "    return df_user_reviews\n",
    "\n",
    "def obtener_matriz_caracteristicas(df_users_items):\n",
    "    user_item_matrix = df_users_items.pivot_table(index='user_id', columns='title', values='playtime_forever', fill_value=0)\n",
    "    return user_item_matrix\n",
    "\n",
    "def calcular_similitud_coseno(user_item_matrix):\n",
    "    item_similarity = cosine_similarity(user_item_matrix.T)\n",
    "    return item_similarity\n",
    "\n",
    "def recomendacion_juego(title, user_item_matrix, item_similarity):\n",
    "    if title in user_item_matrix.columns:\n",
    "        juego_seleccionado = user_item_matrix[title]\n",
    "        sim_scores = list(enumerate(item_similarity[user_item_matrix.columns.get_loc(title)]))\n",
    "        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)\n",
    "        juegos_similares = sim_scores[1:6]  \n",
    "        titulos_recomendados = [user_item_matrix.columns[i[0]] for i in juegos_similares]\n",
    "        return {\"recomendaciones\": titulos_recomendados}\n",
    "    else:\n",
    "        raise HTTPException(status_code=404, detail=\"Juego no encontrado\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
