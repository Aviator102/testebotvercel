import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/check_page', methods=['GET'])
def check_page():
    # URL da página que você deseja acessar
    url = "https://testebotvercel.vercel.app/"
    
    # Faz uma solicitação para a URL
    response = requests.get(url)

    if response.ok:
        # Retorna o conteúdo da página
        return jsonify({
            "status": "success",
            "content": response.text[:1000]  # Retorna os primeiros 1000 caracteres
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Não foi possível acessar a página."
        })

if __name__ == "__main__":
    app.run()
