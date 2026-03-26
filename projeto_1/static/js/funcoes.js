function buscarCep() {
    let cep = document.getElementById("cep").value;

    fetch(`https://viacep.com.br/ws/${cep}/json/`)
        .then(response => response.json())
        .then(data => {
        if (data.erro) {
            alert("CEP não encontrado! Verifique o CEp digitado e tente novamente");
            document.getElementById("bairro").value = "";
            return;
        }

        document.getElementById("bairro").value = data.bairro || "";
        document.getElementById("logradouro").value = data.logradouro || "";
        document.getElementById("localidade").value = data.localidade || "";
        document.getElementById("bairro").value = data.bairro || "";
        document.getElementById("estado").value = data.estado || "";

        })
        .catch(error => console.error("Erro:", error));
}