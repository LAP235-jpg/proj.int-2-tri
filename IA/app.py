
from IA import classificar
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

temperatura_atual = 69

@app.route("/")
def home():
    return "Coffee Quality Monitor API"

@app.route("/predict", methods=["POST"])
def predict():

    dados = request.json

    resultado = classificar(

        temperatura_atual,
        dados["moagem"],
        dados["torra"]

    )

    return jsonify({

        "temperatura": temperatura_atual,
        "resultado": resultado

    })

@app.route("/temperatura")
def temperatura():
    temperatura = temperatura_atual
    return jsonify({
        "temperatura": temperatura
    })

if __name__ == "__main__":
    app.run(debug=True)
