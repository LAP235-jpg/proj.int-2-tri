# ☕ Coffee Quality Monitor

> Sistema Inteligente de Avaliação da Qualidade do Café utilizando IoT e Machine Learning.

![Status](https://img.shields.io/badge/Status-Finalizado-brightgreen)
![STM32](https://img.shields.io/badge/STM32-Embedded-blue)
![Python](https://img.shields.io/badge/Python-ML-green)
![HTML](https://img.shields.io/badge/Frontend-Web-orange)

---

## 📖 Sobre o Projeto

O **Coffee Quality Monitor** é um sistema IoT desenvolvido para avaliar a qualidade de uma bebida de café utilizando técnicas de **Machine Learning**.

O projeto integra um sistema embarcado baseado em **STM32**, uma API desenvolvida em **Python**, um algoritmo de classificação **K-Nearest Neighbors (KNN)** e uma interface Web para interação com o usuário.

A classificação da bebida é realizada a partir de três parâmetros:

* 🌡️ Temperatura da água (STM32 + Potenciômetro)
* 🌱 Tipo de moagem
* 🔥 Nível de torra

Após receber essas informações, o modelo de Machine Learning realiza a classificação da qualidade da bebida.

---

# 🎯 Objetivo

Desenvolver um sistema capaz de integrar:

* Sistemas Embarcados
* Comunicação Serial
* APIs REST
* Machine Learning
* Desenvolvimento Web

em uma única aplicação funcional.

---

# 🏗 Arquitetura

```text
                     STM32
            (Leitura do Potenciômetro)
                      │
                  USB Serial
                      │
                      ▼
                  Aplicação C#
          Comunicação com o embarcado
                      │
               HTTP / JSON
                      │
                      ▼
                 API Python
      ┌─────────────────────────────┐
      │ Recebe temperatura          │
      │ Recebe dados do usuário     │
      │ Executa algoritmo KNN       │
      │ Retorna classificação       │
      └─────────────────────────────┘
                      ▲
                      │
          HTML • CSS • JavaScript
```

---

# ⚙️ Tecnologias

## Sistemas Embarcados

* STM32
* STM32CubeIDE
* ADC
* USB CDC (Serial)

## Backend

* Python
* Flask/FastAPI
* Scikit-Learn
* NumPy
* Pandas

## Desktop

* C#
* .NET

## Front-end

* HTML5
* CSS3
* JavaScript

---

# 🤖 Machine Learning

O projeto utiliza o algoritmo **K-Nearest Neighbors (KNN)** para realizar a classificação da qualidade da bebida.

## Entradas

| Variável    | Origem        |
| ----------- | ------------- |
| Temperatura | STM32         |
| Moagem      | Interface Web |
| Torra       | Interface Web |

## Saída

A IA classifica a bebida como:

* 🔴 Ruim
* 🟡 Boa
* 🟢 Excelente

---

# 🌐 Funcionamento

## 1️⃣ STM32

O microcontrolador realiza a leitura do potenciômetro e converte o valor para uma temperatura simulada.

↓

## 2️⃣ Aplicação C#

Recebe os dados enviados pela porta serial e encaminha a temperatura para a API.

↓

## 3️⃣ Interface Web

O usuário informa:

* Tipo de moagem
* Nível de torra

↓

## 4️⃣ API Python

Recebe:

* Temperatura
* Moagem
* Torra

Executa o modelo KNN.

↓

## 5️⃣ Resultado

A classificação é enviada para a interface Web.

---
# 🚀 Funcionalidades

* Leitura de temperatura em tempo real
* Comunicação Serial
* API REST
* Classificação por Machine Learning
* Interface Web responsiva
* Histórico de classificações
* Visualização dos resultados

---

# 👥 Equipe

Luigi & Murilo

---


