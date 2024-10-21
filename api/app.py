from flask import Flask, render_template
import requests
import threading
import time

app = Flask(__name__)

# Configurações do bot do Telegram
TOKEN_BOT_ORIGEM = '6837412955:AAEb5dH8PECn5oX8t5VcArRyejLMLys-pXg'
TOKEN_BOT_DESTINO = '7348520195:AAGN8xkJXATY1OmyhLkGxu2Kv4z-lR5BtB0'
CHAT_ID_ORIGEM = '-1002029148099'
CHAT_ID_DESTINO = '-1002422442915'
last_message_id = None

def replicate_messages():
    global last_message_id
    while True:
        response = requests.get(f'https://api.telegram.org/bot{TOKEN_BOT_ORIGEM}/getUpdates?offset=-1')
        update_data = response.json()

        if update_data.get("ok") and update_data.get("result"):
            message = update_data["result"][0].get("channel_post")
            if message and message["chat"]["id"] == CHAT_ID_ORIGEM and message["message_id"] != last_message_id:
                # Envia a mensagem para o destino
                requests.post(f'https://api.telegram.org/bot{TOKEN_BOT_DESTINO}/sendMessage', json={
                    "chat_id": CHAT_ID_DESTINO,
                    "text": message["text"]
                })
                last_message_id = message["message_id"]  # Atualiza o ID da última mensagem
        time.sleep(5)  # Espera 5 segundos antes de verificar novamente

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Thread(target=replicate_messages, daemon=True).start()
    app.run(debug=True)
