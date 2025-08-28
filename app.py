# IA com LLM (e Construção de API) Para Análise de Sentimento em Noticiário Financeiro
# App

# Importa a biblioteca FastAPI para criar a aplicação web
from fastapi import FastAPI

# Importa BaseModel do Pydantic para a validação de dados
from pydantic import BaseModel

# Importa o modelo e o tokenizador da biblioteca Transformers
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Importa a biblioteca PyTorch para operações de tensor
import torch

# Importa uvicorn para rodar a aplicação FastAPI em modo servidor
import uvicorn

# Cria uma instância da aplicação FastAPI
app = FastAPI()

# Carrega o tokenizador pré-treinado
tokenizer = AutoTokenizer.from_pretrained("tokenizador_vpl")

# Define o caminho do modelo
id_llm = "modelo_vpl"

# Carrega o modelo pré-treinado para classificação de sequência
modelo_llm = AutoModelForSequenceClassification.from_pretrained(id_llm)

# Define a classe Item usando Pydantic para validação de dados
class Item(BaseModel):
    text: str
    title: str

# Define a função assíncrona para prever o sentimento
# Mais detalhes no videobook do Capítulo 9 do curso
async def vpl_preve_sentimento(input_text):

    # Tokeniza o texto de entrada
    inputs = tokenizer(input_text, 
                       return_tensors = "pt", 
                       truncation = True, 
                       padding = True, 
                       max_length = 512)

     # Realiza a previsão sem calcular os gradientes
    with torch.no_grad():
        outputs = modelo_llm(**inputs)

    # Calcula as probabilidades previstas
    probabilidades_previstas = torch.softmax(outputs.logits, dim=1).squeeze().tolist()

    return probabilidades_previstas

# Define a rota raiz que retorna uma mensagem simples
@app.get("/")
def index():
    return {"App de IA com LLM Para Analisar o Sentimento de Notícias Financeiras"}

# Define a rota para análise de sentimento que aceita requisições POST
@app.post("/vpl_analisa_sentimento/")
async def vpl_analisa_sentimento(item: Item):

    # Concatena o título e o texto do item de entrada
    input_text = item.title + " " + item.text

    # Obtém as probabilidades previstas
    probabilidades_previstas = await vpl_preve_sentimento(input_text)

    # Mapeia os índices das probabilidades para os sentimentos correspondentes
    vpl_sentimento_mapping = {0: "Negativo", 1: "Neutro", 2: "Positivo"}

    # Obtém o sentimento previsto com base na probabilidade máxima
    sentimento_previsto = vpl_sentimento_mapping[probabilidades_previstas.index(max(probabilidades_previstas))]
    
    # Cria o corpo da resposta com o sentimento previsto e as probabilidades
    response_body = {
        "sentimento_previsto": sentimento_previsto,
        "probabilidades_das_previsoes": {
            "Negativo": probabilidades_previstas[0],
            "Neutro": probabilidades_previstas[1],
            "Positivo": probabilidades_previstas[2]
        }
    }
    
    return response_body

# Executa a aplicação FastAPI usando uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8787)
