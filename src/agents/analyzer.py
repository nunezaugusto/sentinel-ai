from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.database.vector_db import get_relevant_docs # Tu función de búsqueda

class CyberAnalyzer:
    def __init__(self):
        # 1. Configuramos el modelo (el cerebro)
        self.llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)
        
        # 2. Definimos cómo debe pensar la IA (el Prompt)
        self.prompt = ChatPromptTemplate.from_template("""
        Eres un experto en ciberseguridad de élite (Nivel L3). 
        Analiza el siguiente evento detectado por un sensor en Rust:
        
        EVENTO: {event_data}
        
        CONOCIMIENTO PREVIO (RAG): {context}
        
        Basado en el contexto y los datos, responde:
        1. ¿Es un ataque real o un falso positivo?
        2. Nivel de peligrosidad (1-10).
        3. Recomendación técnica para el administrador.
        """)
        
        self.parser = StrOutputParser()

    async def analyze_event(self, event_json):
        # 3. RAG: Buscamos en ChromaDB ataques parecidos para dar contexto
        context_docs = get_relevant_docs(event_json["raw_payload"])
        
        # 4. Creamos la "Cadena" (Chain)
        chain = self.prompt | self.llm | self.parser
        
        # 5. Ejecutamos la IA
        # response = await chain.ainvoke({
            #"event_data": event_json,             #esta parte es provisional
           # "context": context_docs
        #})
        
        #return response
        return "MODO PRUEBA: Simulación de análisis para el evento de IP " + event_json["source_ip"]