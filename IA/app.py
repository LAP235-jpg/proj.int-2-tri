
from IA import classificar
from flask import Flask, request, jsonify
from flask_cors import CORS

from banco import (
    criar_tabela,
    salvar_classificacao,
    buscar_classificacoes
)

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

@app.route("/historico", methods=["GET"])
def historico():

    resultados = buscar_classificacoes()

    dados = []

    for resultado in resultados:
        dados.append({
            "id": resultado[0],
            "temperatura": resultado[1],
            "moagem": resultado[2],
            "torra": resultado[3],
            "qualidade": resultado[4],
            "data": resultado[5]
        })

    return jsonify(dados)