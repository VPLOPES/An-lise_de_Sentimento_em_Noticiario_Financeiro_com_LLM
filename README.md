# 📊 IA com LLM para Análise de Sentimento em Noticiário Financeiro  

Este projeto implementa uma **API de Análise de Sentimento** em notícias financeiras utilizando **LLMs (Large Language Models)**, construída com **FastAPI**, **Transformers** e **PyTorch**.  

A aplicação recebe como entrada o **título e o texto** de uma notícia e retorna o sentimento previsto (**Negativo, Neutro ou Positivo**) junto com as probabilidades associadas.  

---

## 🚀 Funcionalidades  

- API desenvolvida em **FastAPI**  
- Uso de modelo **pré-treinado** para classificação de sentimento  
- Retorna sentimento previsto e probabilidades de cada classe  
- Endpoint `POST /vpl_analisa_sentimento/` para análise de texto  
- Endpoint raiz `GET /` para checar se a API está ativa  

---

## 📂 Estrutura do Projeto  

app.py # Arquivo principal da aplicação

markdown
Copiar código

---

## ⚙️ Requisitos  

- Python 3.8+  
- [FastAPI](https://fastapi.tiangolo.com/)  
- [Uvicorn](https://www.uvicorn.org/)  
- [Transformers](https://huggingface.co/transformers/)  
- [PyTorch](https://pytorch.org/)  
- [Pydantic](https://docs.pydantic.dev/)  

Instale as dependências com:  

```bash
pip install fastapi uvicorn torch transformers pydantic
▶️ Como Executar
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Execute a aplicação:

bash
Copiar código
python app.py
A API estará disponível em:

cpp
Copiar código
http://0.0.0.0:8787
📌 Endpoints
1. Checar API
Rota: GET /

Resposta:

json
Copiar código
{"App de IA com LLM Para Analisar o Sentimento de Notícias Financeiras"}
2. Analisar Sentimento
Rota: POST /vpl_analisa_sentimento/

Entrada (JSON):

json
Copiar código
{
  "title": "Mercado financeiro em alta",
  "text": "A bolsa de valores fechou o dia com forte valorização."
}
Saída (JSON):

json
Copiar código
{
  "sentimento_previsto": "Positivo",
  "probabilidades_das_previsoes": {
    "Negativo": 0.05,
    "Neutro": 0.10,
    "Positivo": 0.85
  }
}
📖 Notas
O modelo pré-treinado utilizado deve estar disponível localmente com os nomes:

tokenizador_vpl

modelo_vpl

A aplicação está configurada para rodar na porta 8787

👨‍💻 Autor
Desenvolvido por Vinícius Lopes
