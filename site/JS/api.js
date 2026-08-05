export async function enviarDados(moagem, torra){

    const resposta = await fetch("http://127.0.0.1:5000/predict",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            moagem,
            torra

        })

    });

    return await resposta.json();

}