from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurações do Chrome em modo headless (invisível)
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inicia o ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL da página que você deseja abrir
url = "https://replicabot.vercel.app/"
driver.get(url)

# Aguarda alguns segundos para o carregamento da página
time.sleep(5)  # Ajuste o tempo conforme necessário

# Mantém o navegador aberto
try:
    while True:
        # Aqui você pode adicionar lógica para verificar elementos ou interagir com a página
        # Por exemplo, você pode pegar mensagens ou qualquer outra informação que deseja monitorar
        time.sleep(5)  # Ajuste o tempo conforme necessário
except KeyboardInterrupt:
    print("Saindo...")

# Fecha o navegador ao final (não será alcançado até que o loop seja interrompido)
driver.quit()
