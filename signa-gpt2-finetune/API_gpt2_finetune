from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

app = FastAPI()

model = AutoModelForCausalLM.from_pretrained("./model_treinado")
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
tokenizer.pad_token = tokenizer.eos_token

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

class Entrada(BaseModel):
    prompt: str
    max_length: int = 100

@app.post("/gerar")
async def gerar_texto(data: Entrada):
    try:
        saida = generator(data.prompt, max_length=data.max_length, num_return_sequences=1)
        texto_gerado = saida[0]['generated_text'].strip()
        return {"resposta": texto_gerado}
    except Exception as e:
        return {"erro": str(e)}
