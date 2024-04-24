from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

def consulta_con_memoria(retriever, pregunta, memoria=[]):
    llm = ChatOpenAI(temperature=1)

    crc = ConversationalRetrievalChain.from_llm(llm, retriever)
    respuesta = crc({'question': pregunta, 'chat_history': memoria})
    memoria.append((pregunta, respuesta['answer']))

    return respuesta, memoria
