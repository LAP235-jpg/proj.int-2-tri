async function avaliarCafe() {

    const moagem = document.getElementById("moagem").value;
    const torra = document.getElementById("torra").value;

    const resposta = await fetch("http://127.0.0.1:5000/predict", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            moagem: moagem,
            torra: torra
        })

    });

    const dados = await resposta.json();

    console.log(dados);

    document.getElementById("resultado").innerHTML = dados.resultado
}

document
    .getElementById("avaliar")
    .addEventListener("click", avaliarCafe);

    async function tempCafe() {
        try {
        const resposta = await fetch("http://127.0.0.1:5000/temperatura");
        const dados = await resposta.json();

        document.getElementById("temperatura").innerText =
            dados.temperatura + " °C";
    } catch (erro) {
        console.log(erro);
    }
}

  
tempCafe();
setInterval(tempCafe, 1000);