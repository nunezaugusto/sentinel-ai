from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from src.agents.analyzer import CyberAnalyzer

# Inicializamos FastAPI y tu Cerebro de IA
app = FastAPI(title="Kyros Sentinel Ingestor")
analyzer = CyberAnalyzer()

# Definimos el formato que Joaquín DEBE cumplir (El Contrato)
class AttackEvent(BaseModel):
    node_id: str
    timestamp: datetime
    source_ip: str
    target_port: int
    protocol: str
    raw_payload: str
    severity_guess: str

@app.get("/")
async def root():
    return {"status": "online", "message": "Sentinel API is running"}

@app.post("/ingest")
async def ingest_event(event: AttackEvent):
    try:
        # 1. Recibimos los datos del sensor de Rust
        data = event.model_dump() # Convertimos a diccionario de Python
        
        # 2. Se lo pasamos al Analyzer (tu código de LangChain)
        report = await analyzer.analyze_event(data)
        
        # 3. Respondemos al sensor que todo OK y le damos el veredicto de la IA
        return {
            "status": "success",
            "node": event.node_id,
            "ai_verdict": report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analizando el evento: {str(e)}")