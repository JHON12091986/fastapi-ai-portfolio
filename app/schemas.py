from pydantic import BaseModel

class PromptRequest(BaseModel):
    text: str
    # Aquí podrías añadir más campos, como el modelo de IA a usar

class AIResponse(BaseModel):
    original_text: str
    generated_text: str
    id: int

    class Config:
        from_attributes = True