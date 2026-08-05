
from IA import classificar
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Coffee Quality Monitor API"

@app.route("/predict", methods=["POST"])
def predict():

    dados = request.json

    moagem = dados["moagem"]
    torra = dados["torra"]

    # Temperatura fixa apenas para teste
    temperatura = 70

    resultado = classificar(
        temperatura,
        moagem,
        torra
    )

    return jsonify({

        "temperatura": temperatura,
        "moagem": moagem,
        "torra": torra,
        "resultado": resultado

    })
if __name__ == "__main__":
    app.run(debug=True)