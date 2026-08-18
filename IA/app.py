from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/predict", methods=["POST"])
def predict():

    dados = request.get_json()

    temperatura = dados["temperatura"]

    print(f"Temperatura recebida: {temperatura}")

    return jsonify({
        "mensagem": "Dados recebidos com sucesso!",
        "temperatura": temperatura
    })


@app.route("/temperatura", methods=["GET"])
def temperatura():

    return jsonify({
        "temperatura": 30
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)