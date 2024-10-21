from flask import Flask
import requests
import time

app = Flask(__name__)

# Tokens e IDs dos bots
TOKEN_BOT_ORIGEM = '6837412955:AAEb5dH8PECn5oX8t5VcArRyejLMLys-pXg'  # Token do bot origem
TOKEN_BOT_DESTINO = '7348520195:AAGN8xkJXATY1OmyhLkGxu2Kv4z-lR5BtB0'  # Token do bot destino
CHAT_ID_ORIGEM = '-1002029148099'  # ID do grupo/canal de origem
CHAT_ID_DESTINO = '-1002422442915'  # ID do grupo/canal de destino
LAST_MESSAGE_ID_FILE = 'last_message_id.txt'  # Arquivo para armazenar o último ID de mensagem replicada

def get_last_message_id():
    try:
        with open(LAST_MESSAGE_ID_FILE, 'r') as f:
            return int(f.read())
    except FileNotFoundError:
        return None

def set_last_message_id(message_id):
    with open(LAST_MESSAGE_ID_FILE, 'w') as f:
        f.write(str(message_id))

@app.route('/replicate', methods=['GET'])
def replicate_messages():
    last_message_id = get_last_message_id()

    response = requests.get(f'https://api.telegram.org/bot{TOKEN_BOT_ORIGEM}/getUpdates?offset=-1')
    update_data = response.json()

    if update_data.get('ok') and update_data['result']:
        message = update_data['result'][0].get('channel_post')
        if message and message['chat']['id'] == CHAT_ID_ORIGEM:
            if last_message_id != message['message_id']:
                # Enviar mensagem para o chat de destino
                requests.post(f'https://api.telegram.org/bot{TOKEN_BOT_DESTINO}/sendMessage', json={
                    'chat_id': CHAT_ID_DESTINO,
                    'text': message['text']
                })
                set_last_message_id(message['message_id'])  # Atualiza o ID da última mensagem replicada
                return 'Mensagem replicada com sucesso!', 200

    return 'Nenhuma nova mensagem para replicar.', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
