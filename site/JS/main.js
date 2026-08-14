async function avaliarCafe() {

    const moagem = document.getElementById("moagem").value;
    const torra = document.getElementById("torra").value;

    const resposta = await fetch(
        "http://127.0.0.1:5000/predict",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                moagem: moagem,
                torra: torra
            })
        }
    );

    const dados = await resposta.json();

    console.log(dados);

    document.getElementById("resultado").innerHTML =
        dados.resultado;

    carregarHistorico();
}


document
    .getElementById("avaliar")
    .addEventListener("click", avaliarCafe);


async function tempCafe() {

    try {

        const resposta =
            await fetch("http://127.0.0.1:5000/temperatura");

        const dados = await resposta.json();

        document.getElementById("temperatura").innerText =
            dados.temperatura + " °C";

    } catch (erro) {

        console.log(erro);

    }

}


tempCafe();

setInterval(tempCafe, 1000);


async function carregarHistorico() {

    try {

        const resposta =
            await fetch("http://127.0.0.1:5000/historico");

        const dados = await resposta.json();

        const historico =
            document.getElementById("historico");

        historico.innerHTML = "";

        dados.forEach(item => {

            historico.innerHTML += `
                <tr>
                    <td>${item.id}</td>
                    <td>${item.temperatura} °C</td>
                    <td>${item.moagem}</td>
                    <td>${item.torra}</td>
                    <td>${item.qualidade}</td>
                    <td>${item.data}</td>
                </tr>
            `;

        });

    } catch (erro) {

        console.error(
            "Erro ao carregar histórico:",
            erro
        );

    }

}


carregarHistorico(); 