let usernameExiste = false;
let emailExiste = false;

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

function verificarUsername() {
    const username = document.getElementById('username').value;

    if (!username) return;

    fetch('/usuario/verificar-username/?username=' + username)
        .then(response => response.json())
        .then(data => {
            const msg = document.getElementById('mensagem');

            if (data.existe) {
                msg.innerHTML = "❌ Username já existe";
                msg.style.color = "red";
                usernameExiste = true;
            } else {
                msg.innerHTML = "✅ Username disponível";
                msg.style.color = "green";
                usernameExiste = false;
            }

            controlarBotao(); 
        })
        .catch(error => console.error('Erro:', error));
}

function verificarEmail() {
    const email = document.getElementById('email').value;
    const msg = document.getElementById('mensagem_email');

    if (email.length < 5 || !email.includes('@')) {
        msg.innerHTML = "";
        emailExiste = false;
        controlarBotao();
        return;
    }

    fetch('/usuario/verificar-email/?email=' + email)
        .then(response => response.json())
        .then(data => {
            if (data.existe) {
                msg.innerHTML = "❌ Email já cadastrado";
                msg.style.color = "red";
                emailExiste = true;
            } else {
                msg.innerHTML = "✅ Email disponível";
                msg.style.color = "green";
                emailExiste = false;
            }

            controlarBotao(); 
        })
        .catch(error => console.error('Erro:', error));
}

function controlarBotao() {
    const botao = document.getElementById('btnSalvar');

    if (usernameExiste || emailExiste) {
        botao.disabled = true;
    } else {
        botao.disabled = false;
    }
}