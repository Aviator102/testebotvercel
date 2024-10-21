import requests
from bs4 import BeautifulSoup
import time

# URL da página que você deseja acessar
url = "https://replicabot.vercel.app/"

# Função para buscar e analisar a página
def buscar_mensagens():
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Localiza os elementos que contêm as mensagens (substitua o seletor abaixo conforme necessário)
        mensagens = soup.select('.classe-mensagem')  # Substitua '.classe-mensagem' pelo seletor apropriado
        return [mensagem.text for mensagem in mensagens]
    else:
        print(f"Erro ao acessar a página: {response.status_code}")
        return []

# Simula a leitura das mensagens em um loop
try:
    while True:
        mensagens = buscar_mensagens()
        for mensagem in mensagens:
            if mensagem:  # Verifica se a mensagem não está vazia
                print(mensagem)  # Imprime o texto da mensagem

        # Espera um tempo antes de verificar novamente
        time.sleep(5)  # Ajuste o tempo conforme necessário

except KeyboardInterrupt:
    print("Saindo...")
