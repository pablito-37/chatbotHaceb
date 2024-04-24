Explicación para Ejecutar el Proyecto

1. Instalar Dependencias:
Antes de ejecutar el proyecto, asegúrate de tener Python instalado en tu sistema. Luego, sigue estos pasos:
# Instala las dependencias desde requirements.txt
pip install -r requirements.txt

2. Crear el Archivo .env:
Antes de ejecutar el proyecto, es necesario crear un archivo .env en el directorio raíz del proyecto. Este archivo contendrá las variables de entorno necesarias, como las claves de API.
OPENAI_API_KEY= "tu_clave_de_openai_aqui"
PINECONE_API_KEY= "tu_clave_de_pinecone_aqui"
PINECONE_ENV= "gcp-starter"

3. Ejecutar el Proyecto:
Después de instalar las dependencias y crear el archivo .env, ejecuta el proyecto usando el siguiente comando:
python app.py


Tecnologías Utilizadas:
Este proyecto está hecho con las siguientes tecnologías:
HTML
CSS
JavaScript
Python
Modelo de Lenguaje NLP de OpenAI (gpt-turbo-3.5)
Base de Datos de Vectores Pinecone
