from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import pickle
import numpy as np

# Carregar base
with open("/content/base_signa_completa_corrigida.json", encoding="utf-8") as f:
    base = json.load(f)

perguntas = [item["pergunta"] for item in base]
respostas = [item["resposta"] for item in base]

# Novo modelo (mais robusto para PT)
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
embeddings = model.encode(perguntas)

# Salvar embeddings
with open("embeddings.pt.pkl", "wb") as f:
    pickle.dump((perguntas, respostas, embeddings), f)
