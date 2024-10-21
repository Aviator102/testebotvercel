import requests

# URL que você deseja acessar
url = "https://replicabot.vercel.app/"

# Faz uma solicitação GET
response = requests.get(url)

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Tenta decodificar o conteúdo como JSON
    try:
        data = response.json()
        print("Dados recebidos:")
        print(data)
    except ValueError:
        print("Erro ao decodificar JSON.")
else:
    print(f"Código de Status: {response.status_code}")
