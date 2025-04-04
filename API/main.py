from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os
from services.cisterciense_service import gerar_numero_cisterciense

app = Flask(__name__)
CORS(app)

DIRETORIO_OUTPUT = os.path.join(os.getcwd(), "static", "output")

@app.route("/gerar/<int:numero>")
def gerar(numero):
    try:
        caminho_imagem, imagens_aux = gerar_numero_cisterciense(numero)
        return jsonify({
            "imagem_principal": "numero_gerado.png",
            "imagens_auxiliares": imagens_aux
        })
    except Exception as e:
        print(f"Erro na API: {str(e)}")  
        return jsonify({"erro": str(e)}), 500

@app.route("/imagem/<nome>")
def obter_imagem(nome):
    return send_from_directory(DIRETORIO_OUTPUT, nome)

if __name__ == "__main__":
    app.run(debug=True)
