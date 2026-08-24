from IA import classificar
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# ====================================================
# SIMULAÇÃO DO STM32
# ====================================================

TEMPERATURA_SIMULADA = 30

ultima_temperatura = 30

# ====================================================
# HISTÓRICO
# ====================================================

historico = []
proximo_id = 1


@app.route("/")
def home():
    return "Coffee Quality Monitor API"


# ====================================================
# RECEBE TEMPERATURA
# ====================================================

@app.route("/temperatura", methods=["POST"])
def receber_temperatura():

    global ultima_temperatura

    dados = request.get_json()

    temperatura = dados["temperatura"]

    ultima_temperatura = temperatura

    print(f"Temperatura recebida: {temperatura}")

    return jsonify({
        "mensagem": "Temperatura recebida com sucesso!",
        "temperatura": temperatura
    })


# ====================================================
# PREVISÃO DA QUALIDADE
# ====================================================

@app.route("/predict", methods=["POST"])
def predict():

    global proximo_id

    dados = request.get_json()

    moagem = dados["moagem"]
    torra = dados["torra"]

    resultado = classificar(
        ultima_temperatura,
        moagem,
        torra
    )

    # Cria o registro da medição
    medicao = {
        "id": proximo_id,
        "temperatura": ultima_temperatura,
        "moagem": moagem,
        "torra": torra,
        "qualidade": resultado,
        "data": "17/08/2026 18:33:23"
    }

    historico.append(medicao)

    proximo_id += 1

    return jsonify({
        "temperatura": ultima_temperatura,
        "moagem": moagem,
        "torra": torra,
        "resultado": resultado
    })


# ====================================================
# HISTÓRICO
# ====================================================

@app.route("/historico", methods=["GET"])
def obter_historico():

    return jsonify(historico)


# ====================================================
# CONSULTA TEMPERATURA
# ====================================================

@app.route("/temperatura", methods=["GET"])
def temperatura():

    return jsonify({
        "temperatura": ultima_temperatura
    })


if __name__ == "__main__":

    print(
        f"🌡️ MODO SIMULAÇÃO ATIVO | "
        f"Temperatura: {TEMPERATURA_SIMULADA}°C"
    )

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )