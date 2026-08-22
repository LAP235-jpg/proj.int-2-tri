import math
from collections import Counter

# ====================================================
# DATASET
# temperatura | moagem | torra | qualidade
#
# moagem:
# 0 = Fina
# 1 = Média
# 2 = Grossa
#
# torra:
# 0 = Clara
# 1 = Média
# 2 = Escura
# ====================================================

dados = [

    [8.2, 2, 0, "Ruim"],
    [8.5, 2, 0, "Ruim"],
    [8.7, 1, 0, "Boa"],
    [8.9, 1, 1, "Boa"],
    [9.0, 1, 1, "Excelente"],
    [9.1, 1, 1, "Excelente"],
    [9.2, 1, 1, "Excelente"],
    [9.3, 1, 2, "Boa"],
    [9.5, 0, 2, "Boa"],
    [9.7, 0, 2, "Ruim"]

]

# -------------------------------
# Conversão de texto para número
# -------------------------------

moagem_map = {

    "Fina":0,
    "Media":1,
    "Média":1,
    "Grossa":2

}

torra_map = {

    "Clara":0,
    "Media":1,
    "Média":1,
    "Escura":2

}



def distancia_euclidiana(p1, p2):

    return math.sqrt(sum((a-b)**2 for a,b in zip(p1,p2)))



def knn(ponto, dados, k):

    distancias = []

    for registro in dados:

        features = registro[:3]

        classe = registro[3]

        distancia = distancia_euclidiana(ponto,features)

        distancias.append((distancia,classe))

    distancias.sort(key=lambda x:x[0])

    vizinhos = distancias[:k]

    votos = [classe for _,classe in vizinhos]

    resultado = Counter(votos).most_common(1)[0][0]

    return resultado



def classificar(temperatura, moagem, torra, k=3):

    temperatura = temperatura / 10

    moagem = moagem_map[moagem]
    torra = torra_map[torra]

    ponto = [
        temperatura,
        moagem,
        torra
    ]

    resultado = knn(ponto, dados, k)

    return resultado
