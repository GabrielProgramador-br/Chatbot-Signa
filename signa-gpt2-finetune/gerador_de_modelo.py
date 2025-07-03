#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install virtualenv --quiet')
get_ipython().system('virtualenv hf_env')
get_ipython().system('source hf_env/bin/activate && pip install numpy==1.26.4 transformers datasets ipykernel --quiet')
get_ipython().system('python -m ipykernel install --user --name=hf_env --display-name "Python (HF no NumPy 1.26)"')


# In[ ]:


get_ipython().system('pip install transformers datasets')


# In[ ]:


corpus = """
Pergunta: O que é a Signa?
Resposta: A Signa é uma empresa portuguesa especializada na concepção, instalação e manutenção de soluções integradas de segurança eletrónica e tecnológica.

Pergunta: Quais serviços a Signa oferece?
Resposta: A Signa oferece serviços como consultoria, projeto e implementação de sistemas integrados de segurança eletrónica, incluindo videovigilância (CCTV), controlo de acessos, deteção de intrusão, deteção de incêndio e soluções integradas personalizadas.

Pergunta: Quais tipos de sistemas integrados a Signa implementa?
Resposta: A Signa implementa sistemas como CCTV (videovigilância), deteção de intrusão, deteção de incêndio, controlo de acessos e intercomunicação, de forma integrada e personalizada conforme as necessidades do cliente.

Pergunta: A Signa oferece serviços de consultoria?
Resposta: Sim. A Signa presta consultoria especializada para análise de risco, definição de requisitos técnicos e escolha das melhores soluções de segurança adaptadas ao contexto de cada cliente.

Pergunta: A Signa realiza manutenção dos sistemas?
Resposta: Sim. A empresa oferece manutenção preventiva e corretiva dos sistemas instalados, com planos de suporte técnico adequados às necessidades de cada projeto.

Pergunta: Quem são os clientes da Signa?
Resposta: A Signa atua em diversos setores como banca, retalho, indústria, saúde, logística e instituições públicas, com soluções ajustadas para diferentes exigências.

Pergunta: Como posso entrar em contato com a Signa?
Resposta: Você pode entrar em contato através do e-mail signa@signa.pt ou pelo telefone +351 214 127 780.

Pergunta: Onde a Signa está localizada?
Resposta: A sede da Signa está localizada em Carnaxide, Portugal: Rua António Correia, 15B - 2790-049 Carnaxide.

Pergunta: O que é a Signa?
Resposta: A Signa é uma empresa portuguesa especializada em segurança eletrónica. Atua na concepção, instalação e manutenção de soluções tecnológicas integradas para proteger pessoas, património e informação.

Pergunta: Quais são os valores da Signa?
Resposta: A Signa tem como pilares a inovação, confiança, compromisso com o cliente e a excelência na entrega de soluções de segurança sob medida.

Pergunta: Quais setores a Signa atende?
Resposta: A Signa presta serviços para os setores de banca, saúde, retalho, logística, indústria e organismos públicos.

Pergunta: Quais serviços a Signa oferece?
Resposta: A Signa oferece consultoria técnica, desenvolvimento de projeto, instalação de sistemas, integração de tecnologias e serviços de manutenção preventiva e corretiva.

Pergunta: Quais sistemas de segurança a Signa implementa?
Resposta: A Signa trabalha com sistemas de videovigilância (CCTV), deteção de intrusão, deteção de incêndio, controlo de acessos, intercomunicação e soluções integradas.

Pergunta: O que é uma solução integrada de segurança?
Resposta: É a integração de diferentes sistemas (como CCTV, alarme, controlo de acessos) num único ambiente de gestão, proporcionando mais eficiência, automatização e segurança.

Pergunta: Como funciona a consultoria da Signa?
Resposta: A Signa realiza análise de risco, levantamento de necessidades, e propõe soluções técnicas de segurança adaptadas ao ambiente do cliente.

Pergunta: Quais soluções de controlo de acessos são oferecidas?
Resposta: A Signa fornece soluções de controlo de acessos para pessoas e veículos, com autenticação por cartões, biometria ou credenciais digitais.

Pergunta: A Signa instala câmaras de segurança (CCTV)?
Resposta: Sim. A Signa instala sistemas de videovigilância com gravação local ou remota, gestão por software e integração com outros sistemas.

Pergunta: A Signa oferece manutenção técnica?
Resposta: Sim. A manutenção pode ser preventiva ou corretiva, com planos de suporte personalizados e assistência técnica permanente.

Pergunta: A Signa desenvolve projetos personalizados?
Resposta: Sim. A Signa adapta soluções técnicas às necessidades específicas de cada cliente, realizando projeto técnico detalhado e execução completa.

Pergunta: A Signa atua em projetos de grande porte?
Resposta: Sim. A empresa já implementou soluções integradas em hospitais, bancos, cadeias de retalho, centros logísticos e instituições públicas.

Pergunta: Posso contratar apenas a manutenção da Signa, sem instalar o sistema com eles?
Resposta: Sim. A Signa pode assumir a manutenção de sistemas já existentes, mesmo que tenham sido instalados por outras empresas.

Pergunta: A Signa faz integração com sistemas de incêndio?
Resposta: Sim. A empresa integra sistemas de alarme de incêndio com demais sistemas de segurança para respostas automáticas e gestão centralizada.

Pergunta: Qual é o diferencial da Signa?
Resposta: A Signa se destaca pela abordagem consultiva, uso de tecnologia de ponta, integração de sistemas e atendimento personalizado ao cliente.

Pergunta: A Signa realiza formação ou treinamento?
Resposta: Sim. A empresa orienta os utilizadores sobre o funcionamento dos sistemas instalados, garantindo uso correto e seguro das tecnologias.

Pergunta: A Signa faz orçamentos gratuitos?
Resposta: O site informa que é possível solicitar orçamento ou contacto através do formulário da página de 'Contactos'.

Pergunta: Como posso entrar em contato com a Signa?
Resposta: Através do telefone +351 214 127 780 ou e-mail signa@signa.pt. Também é possível usar o formulário do site.

Pergunta: Qual é o endereço da Signa?
Resposta: Rua António Correia, 15B - 2790-049 Carnaxide, Portugal.

Pergunta: A Signa atua apenas em Portugal?
Resposta: O site não especifica atuação fora de Portugal, portanto presume-se que a operação principal é nacional.

Pergunta: Quais marcas de equipamentos a Signa utiliza?
Resposta: A Signa trabalha com fabricantes reconhecidos internacionalmente, oferecendo equipamentos certificados e compatíveis com normas de segurança eletrónica.

Pergunta: A Signa realiza vistorias técnicas?
Resposta: Sim. A Signa pode realizar vistorias técnicas no local para avaliar o ambiente e indicar as soluções mais adequadas de segurança.

Pergunta: O que é segurança eletrónica?
Resposta: Segurança eletrónica é o conjunto de tecnologias e sistemas que protegem pessoas, bens e informações por meio de equipamentos como alarmes, câmaras, sensores e sistemas de acesso.

Pergunta: A Signa oferece sistemas de alarme para residências?
Resposta: Embora o foco seja soluções corporativas e institucionais, a Signa pode desenvolver projetos sob medida para diferentes tipos de cliente, conforme o escopo.

Pergunta: A Signa possui certificações?
Resposta: A empresa destaca o compromisso com a qualidade e a conformidade normativa, embora as certificações específicas não sejam listadas no site.

Pergunta: Quais são os benefícios de contratar a Signa?
Resposta: A Signa oferece soluções integradas, atendimento consultivo, suporte técnico contínuo e ampla experiência em projetos complexos de segurança.

Pergunta: A Signa trabalha com reconhecimento facial?
Resposta: Sim. A Signa pode integrar sistemas de reconhecimento facial a soluções de controlo de acessos, conforme o projeto.

Pergunta: Qual é a experiência da Signa no mercado?
Resposta: A Signa atua há mais de 20 anos no mercado de segurança eletrónica, com histórico de projetos realizados em clientes de grande porte.

Pergunta: A Signa oferece soluções escaláveis?
Resposta: Sim. As soluções são desenhadas de forma modular e escalável, podendo crescer conforme a necessidade do cliente.

Pergunta: É possível integrar os sistemas da Signa com outras plataformas?
Resposta: Sim. A Signa trabalha com integração de sistemas via protocolos padrão ou APIs, conforme a necessidade do projeto.

Pergunta: A Signa realiza auditoria de segurança?
Resposta: Sim. A consultoria da Signa pode incluir auditorias técnicas para identificar vulnerabilidades e propor melhorias.

Pergunta: Qual é o processo de implementação da Signa?
Resposta: O processo passa por diagnóstico técnico, proposta de solução, projeto detalhado, instalação, testes e manutenção pós-entrega.

Pergunta: Quais diferenciais a Signa oferece em relação a outras empresas?
Resposta: Diferenciais como atendimento consultivo, integração de múltiplas tecnologias, suporte técnico dedicado e experiência em diversos setores.

Pergunta: Quais tecnologias modernas a Signa utiliza?
Resposta: A Signa utiliza tecnologias de inteligência artificial, análise de vídeo, sensores inteligentes e software de monitoramento em tempo real.

Pergunta: Como solicitar um orçamento na Signa?
Resposta: Você pode preencher o formulário de contacto no site ou enviar um e-mail para signa@signa.pt solicitando um orçamento personalizado.

Pergunta: A Signa oferece suporte 24 horas?
Resposta: O site informa que a Signa oferece suporte técnico contínuo, mas recomenda-se confirmar com o atendimento sobre disponibilidade 24/7.

Pergunta: Quais empresas já contrataram a Signa?
Resposta: O site não lista nomes específicos de clientes, mas menciona setores como banca, saúde, retalho e logística.

Pergunta: A Signa fornece equipamentos ou apenas instala?
Resposta: A Signa fornece, instala e integra os equipamentos de segurança, garantindo compatibilidade e eficiência dos sistemas.

Pergunta: A Signa vende equipamentos separadamente?
Resposta: A abordagem da Signa é consultiva e orientada a projetos. A venda de equipamentos geralmente está atrelada a uma solução completa.

Pergunta: Posso visitar a Signa presencialmente?
Resposta: Sim. A sede da Signa está localizada em Carnaxide, Portugal, e o atendimento pode ser agendado previamente via telefone ou e-mail.

"""
with open("signa.txt", "w", encoding="utf-8") as f:
    f.write(corpus)


# In[ ]:


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

