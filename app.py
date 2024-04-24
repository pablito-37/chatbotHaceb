from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv, find_dotenv
from langchain.embeddings import OpenAIEmbeddings
from pinecone import Pinecone as pcn
from langchain.vectorstores import Pinecone
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from memoria import consulta_con_memoria
import uuid

app = Flask(__name__)

# Cargar archivo .env fuera de la función
load_dotenv(find_dotenv(), override=True)


# Traer datos del archivo .env
open_ai_key = os.environ.get('OPENAI_API_KEY')
pinecone_key = os.environ.get('PINECONE_API_KEY')
environment_pinecone = os.environ.get('PINECONE_ENV')

embeddings = OpenAIEmbeddings()

pc = pcn(api_key=os.environ.get('PINECONE_API_KEY'))
index_name = 'prueba'
indexes = pc.list_indexes()

vector_store = Pinecone.from_existing_index(index_name, embeddings)

llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=1)

retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k': 3})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    pregunta = request.json.get("pregunta")
    print("entrando al backend")


    # Obtener respuesta del chatbot con memoria
    respuesta, _ = consulta_con_memoria(retriever, pregunta)

    # Accede al atributo específico de la respuesta que deseas mostrar
    respuesta_texto = respuesta.get('answer', 'No se encontró una respuesta.')

    return jsonify({"respuesta": respuesta_texto})


@app.route("/submit_report", methods=["POST"])
def submit_report():
    report_text = request.json.get("report")

    # Procesar el reporte y almacenarlo en Pinecone
    report_embeddings = embeddings.embed_query(report_text)

    print(report_embeddings)
    print(report_text)

    metadata = {"text": report_text}

    print(metadata)

    # Obtener el índice
    index = pc.Index(index_name)

    # Almacenar el reporte
    index.upsert(vectors=[{
        'id': str(uuid.uuid4()),  # Generar un UUID único
        'values': report_embeddings,
        'metadata': metadata
    }])

    return jsonify({"message": "Report submitted successfully"})



if __name__ == "__main__":
    app.run(debug=True)
