from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer

# Lê seu corpus manualmente
with open("signa.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()

# Cria o dataset
dataset = Dataset.from_dict({"text": linhas})

# Tokenizer + modelo base
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained("distilgpt2")

# Tokenizar
def tokenize_function(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=128)

def add_labels(example):
    example["labels"] = example["input_ids"].copy()
    return example

tokenized_dataset = dataset.map(tokenize_function, batched=True)
tokenized_dataset = tokenized_dataset.map(add_labels)
tokenized_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])

# Parâmetros de treino
training_args = TrainingArguments(
    output_dir="./model_treinado",
    per_device_train_batch_size=2,
    num_train_epochs=3,
    logging_dir="./logs",
    report_to="none"
)

# Treinador
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset
)

# 🚀 Iniciar treino
trainer.train()


# In[ ]:


model.save_pretrained("meu_modelo")
tokenizer.save_pretrained("meu_modelo")

