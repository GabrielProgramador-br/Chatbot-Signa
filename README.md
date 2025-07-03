# 🤖 Desafio Técnico NILG.AI — Chatbot Signa

Este projeto foi desenvolvido como resposta ao desafio técnico proposto pela **NILG.AI**, com o objetivo de construir um chatbot inteligente para a empresa **Signa**, especializada em segurança eletrónica.

## 📌 Objetivo

> Desenvolver uma solução conversacional funcional que:

- Utilize o conteúdo do site institucional da Signa como base de conhecimento → 🔗 https://www.signa.pt/
- Seja capaz de responder a perguntas frequentes e genéricas sobre os produtos e serviços da empresa.
- Esteja implementada como um protótipo funcional simples (API, CLI ou interface web).

---

## ✅ Soluções Desenvolvidas

Três abordagens foram implementadas para cobrir diferentes cenários técnicos:

| Abordagem | Descrição | Ideal para |
|----------|-----------|-------------|
| **💬 GPT-3.5 Turbo** (via OpenAI) | Assistente virtual com linguagem natural e prompt estruturado | Atendimento aberto e humanizado |
| **🧪 GPT-2 Finetunado** | Modelo treinado com corpus institucional para funcionar offline | Testes locais e controle total |
| **🧠 IA com Embeddings** | Busca semântica com `sentence-transformers` e vetores salvos | Respostas técnicas e objetivas |

---

## 🌐 Interfaces Disponíveis

| Interface | Link |
|----------|------|
| 🔹 Interface Web (GitHub Pages) | https://gabrielprogramador-br.github.io/Chatbot-Signa/ |
| 🔹 API GPT-3.5 Turbo | `POST /perguntar` → [API_gpt.py](./API_gpt.py) |
| 🔹 API GPT-2 Finetunado | `POST /gerar` → [API_gpt2_finetune.py](./API_gpt2_finetune.py) |
| 🔹 API com Embeddings | `POST /ask` → incluído em [OCR_CNPJ_PDF.py](./apis/OCR_CNPJ_PDF.py) |

---

## 🚀 Como Executar Localmente

### 🔧 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/Chatbot-Signa.git
cd Chatbot-Signa
