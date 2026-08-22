from IA import classificar
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Guarda a última temperatura recebida pelo STM32
ultima_temperatura = 0

historico = []
proximo_id = 1


@app.route("/")
def home():
    return "Coffee Quality Monitor API"


# Recebe os dados da temperatura vindos do C#
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


# Faz a previsão da qualidade
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
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    # Adiciona ao histórico
    historico.append(medicao)

    # Prepara o próximo ID
    proximo_id += 1

    return jsonify({
        "temperatura": ultima_temperatura,
        "moagem": moagem,
        "torra": torra,
        "resultado": resultado
    })

#gerencia o histórico de previsões
@app.route("/historico", methods=["GET"])
def obter_historico():
    return jsonify(historico)


# Consulta a temperatura atual
@app.route("/temperatura", methods=["GET"])
def temperatura():

    return jsonify({
        "temperatura": ultima_temperatura
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )