from fastapi import FastAPI, Request
from pydantic import BaseModel
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
with open("embeddings.pt.pkl", "rb") as f:
    perguntas, respostas, embeddings = pickle.load(f)

app = FastAPI()

class Pergunta(BaseModel):
    question: str
  
@app.post("/ask")
async def ask(data: Pergunta):
    pergunta_usuario = data.question
    vetor_usuario = model.encode([pergunta_usuario])
    similaridades = cosine_similarity(vetor_usuario, embeddings)
    idx = np.argmax(similaridades)
    score = similaridades[0][idx]

    if score >= 0.65:
        resposta = respostas[idx]
    else:
        resposta = "Desculpe, não encontrei uma resposta ideal. Pode reformular sua pergunta?"

    return {"resposta": resposta, "score": float(score)}
