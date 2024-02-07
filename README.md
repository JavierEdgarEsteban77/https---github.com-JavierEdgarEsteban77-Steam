![ETL & EDA\Logo PI MLOps STEAM.png](https://github.com/JavierEdgarEsteban77/https---github.com-JavierEdgarEsteban77-Steam/blob/9b7089e67f148e122f3aa2d8a6712ccee762bb4f/ETL%20EDA%20NLP%20%26%20Feature%20Engineering%20STEAM/Logo%20PI%20MLOps%20STEAM.png)

# **Descripción del Proyecto**

Este proyecto consiste en un análisis de datos de juegos de la empresa Steam, con reseñas de usuarios y datos de usuarios.

El objetivo es realizar ingeniería de características, análisis de sentimientos y desarrollo de una API para disponibilizar los datos cuya finalidad es obtener el Producto Mínimo Viable (MVP) y brindar todas las recomendaciones necesarias para brindar información para la toma de decisiones.

# **Requisitos**

- annotated-types==0.6.0
anyio==3.7.1
asttokens==2.4.1
attrs==23.2.0
beautifulsoup4==4.12.2
branca==0.7.0
certifi==2023.11.17
cffi==1.16.0
charset-normalizer==3.3.2
click==8.1.7
click-plugins==1.1.1
cligj==0.7.2
colorama==0.4.6
comm==0.2.0
contourpy==1.2.0
cryptography==41.0.7
cycler==0.12.1
debugpy==1.8.0
decorator==5.1.1
et-xmlfile==1.1.0
executing==2.0.1
fastapi==0.105.0
fiona==1.9.5
folium==0.15.1
fonttools==4.47.0
geojson==3.1.0
geopandas==0.14.2
github3.py==4.0.1
h11==0.14.0
idna==3.6
install==1.3.5
ipykernel==6.27.1
ipython==8.18.1
jedi==0.19.1
Jinja2==3.1.2
joblib==1.3.2
jupyter_client==8.6.0
jupyter_core==5.5.1
kiwisolver==1.4.5
MarkupSafe==2.1.3
matplotlib==3.8.2
matplotlib-inline==0.1.6
nest-asyncio==1.5.8
nltk==3.8.1
numpy==1.26.2
openpyxl==3.1.2
packaging==23.2
pandas==2.1.4
parso==0.8.3
Pillow==10.1.0
platformdirs==4.1.0
polars==0.20.1
prompt-toolkit==3.0.43
psutil==5.9.7
pure-eval==0.2.2
pyarrow==15.0.0
pycparser==2.21
pydantic==2.5.2
pydantic_core==2.14.5
Pygments==2.17.2
PyJWT==2.8.0
pyparsing==3.1.1
pyproj==3.6.1
python-dateutil==2.8.2
pytz==2023.3.post1
pywin32==306
pyzmq==25.1.2
regex==2023.10.3
requests==2.31.0
scikit-learn==1.3.2
scipy==1.11.4
seaborn==0.13.0
shapely==2.0.2
six==1.16.0
sniffio==1.3.0
soupsieve==2.5
stack-data==0.6.3
starlette==0.27.0
textblob==0.17.1
threadpoolctl==3.2.0
tornado==6.4
tqdm==4.66.1
traitlets==5.14.0
typing_extensions==4.9.0
tzdata==2023.3
uritemplate==4.1.1
urllib3==2.1.0
utils==1.0.1
uvicorn==0.24.0.post1
wcwidth==0.2.12
wordcloud==1.9.3
xyzservices==2023.10.1


# **Descripción del Proyecto**
Este proyecto tiene como objetivo realizar un análisis de datos de juegos de la empresa Steam, incluyendo reseñas de usuarios y datos de usuarios. El propósito final es desarrollar un Producto Mínimo Viable (MVP) que incluya ingeniería de características, análisis de sentimientos y una API para facilitar la toma de decisiones a través de recomendaciones.

# **Requisitos**
Los archivos JSON originales con los que trabajaremos para construir nuestros DataFrames de Steam son:

steam_games.json
user_reviews.json.gz
users_items.json.gz
Además, se han creado y proporcionado los siguientes archivos CSV a partir de los DataFrames trabajados:

steam_games.csv
user_reviews.csv
users_items.csv

Los archivos JSON originales estarán disponibles para lectura en el siguiente enlace: Enlace a los archivos JSON originales

# **Proceso a ejecutar el código en este orden:**

Trabajé normalizando los datasets, en el caso de los que contenían una lista o diccionario, los desanide, cree variables ficticias y volví a recrear la columna nueva y la original la elimine.

Utilizé analyze columns para analizar todas las columnas y guardé los notebooks en la carpeta llamda ETL EDA PNL e Feature Engineering Steam.

Respecto a FastAPI uvicorn pandas cree la carpeta Proyectos donde guardé las funciones y ejecuté el código cada endpoints respetando las directivas y la salida 'Ejemplo de retorno'

En EDA busqué realizar un desarrollo en donde busco concoer un poco más cada dato procesado, un enfoque más cercano a STEAM para poder brindar asesoramiento y conocer el PMV

# **Modelo de aprendizaje automático**
Se ha elegido implementar un sistema de recomendación basado en el filtro user-item. Esto implica tomar un usuario, encontrar usuarios similares y recomendar ítems que a esos usuarios similares les gustaron. La API resultante deberá incluir dos funciones principales:

# **Recomendación de Juego por Usuario:**

python
Copy code
def recomendacion_usuario(id_de_usuario):
    # Retorna una lista con 5 juegos recomendados para el usuario ingresado
Recomendación de Usuario por Juego:

python
Copy code
def recomendacion_juego(id_de_juego):
    # Retorna una lista con 5 juegos recomendados similares al ingresado

# **Desarrollo de una API utilizando FastAPI con los siguientes endpoints:**

PlayTimeGenre(genero: str)
UserForGenre(genero: str)
UsersRecommend(año: int)
UsersNotRecommend(año: int)
sentiment_analysis(año: int)
Ejecución de la API

La API desarrollada con FastAPI está disponible en el siguiente enlace: Enlace a la API

Video Explicativo
Un video explicativo del proyecto, incluyendo demostraciones de las consultas desde la API y una breve explicación del modelo utilizado para el sistema de recomendación, se encuentra disponible en el siguiente enlace: Enlace al Video Explicativo al siguiente enlace: https://us04web.zoom.us/clips/share/rLL1SHzsF_ayYv1A6k_uhDaBrKtI-DIA1OwyzmZRsp7p5j5nYSBb4vv2wYtL-TcPwisWMRoQqMa7niWYu374HacJdQ.11MayMbfhPu0pnBX
