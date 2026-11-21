from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, SessionLocal

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Portfolio API", description="API para procesar texto con IA")

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Simulador de IA (luego puedes cambiarlo por una llamada real a Claude/OpenAI)
def simulate_ai_generation(text: str) -> str:
    return f"Respuesta generada por IA para: '{text}'. ¡Este es un proyecto de portafolio!"

@app.get("/")
def read_root():
    return {"message": "Bienvenido a mi API de IA. Ve a /docs para probarla."}

@app.post("/generate", response_model=schemas.AIResponse)
def generate_text(request: schemas.PromptRequest, db: Session = Depends(get_db)):
    # 1. Llamar a la "IA" (simulada)
    generated = simulate_ai_generation(request.text)
    
    # 2. Guardar en la base de datos
    db_item = models.AIRequest(original_text=request.text, generated_text=generated)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    
    # 3. Devolver la respuesta
    return db_item

@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    items = db.query(models.AIRequest).all()
    return items