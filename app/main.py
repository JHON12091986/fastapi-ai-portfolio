from fastapi import FastAPI

app = FastAPI()  # <-- Esta línea es la que falta o está mal

@app.get("/")
def read_root():
    return {"message": "Hola, soy Jhon"}

@app.post("/generate")
def generate_text(text: str):
    # Tu lógica aquí
    return {"generated_text": text.upper()}
