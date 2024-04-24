from langchain.text_splitter import RecursiveCharacterTextSplitter as RC
from pinecone import Pinecone as pcn
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

# Leer documento txt sin limpieza
try:
    with open('output.txt', encoding='utf-8') as f:
        documento = f.read().replace('\n', ' ')
except FileNotFoundError:
    documento = "Texto de ejemplo si output.txt no se encuentra"

# Separar texto por subconjuntos de texto
text_splitter = RC(
    chunk_size=500,
    chunk_overlap=100,
    length_function=len
)

textos = text_splitter.create_documents([documento])

# Iterar sobre los textos y mostrar su contenido
for i, texto in enumerate(textos, start=1):
    print(f"Texto {i}:")
    print(texto)
    print("\n")

embeddings = OpenAIEmbeddings()


pregunta = "que paso el 10 de agosto?"

resultado = embeddings.embed_query(pregunta)
# pc = pcn(api_key=os.environ.get('PINECONE_API_KEY'))
# index_name = 'prueba'
# indexes = pc.list_indexes()

# vector_store = Pinecone.from_documents(textos, embeddings, index_name=index_name)
