# IA com LLM (e Construção de API) Para Análise de Sentimento em Noticiário Financeiro
# Cliente

# Import
import requests

# Define o endpoint da API
url = "http://127.0.0.1:8787/vpl_analisa_sentimento/"

# Define o payload (texto e título)
vpl_payload = {
    "text": "Bank of Japan Reports Record Stock Gains for Last Financial Year.",
    "title": "Economy"
}

# Envia uma solicitação POST para o endpoint da API
response = requests.post(url, json = vpl_payload)

# Verifica se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:

    # Obtém o conteúdo da resposta (sentimentos e probabilidades previstos)
    dados_resposta = response.json()
    
    # Extrai o sentimento e as probabilidades previstos
    sentimento_previsto = dados_resposta.get('sentimento_previsto')
    probabilidades = dados_resposta.get('probabilidades_das_previsoes', {})
    
    # Print 
    print("\nIA com LLM (e Construção de API) Para Análise de Sentimento em Noticiário Financeiro\n")
    
    # Imprime o texto do payload
    print(f"Texto Analisado: {vpl_payload['text']}\n")
    
    print(f"Sentimento Previsto: {sentimento_previsto}")
    print("\nProbabilidades das Previsões:")

    for sentimento, probabilidade in probabilidades.items():
        
        # Converte para percentual
        percentual = probabilidade * 100
        print(f"  {sentimento}: {percentual:.2f}%")

    print("\nObrigado Por Usar Este Analisador de Sentimento de Noticiário Financeiro, Baseado em IA e LLM.")
    print("Data Science Academy\n")

else:
    # Print do erro
    print("Erro:", response.text)


    
