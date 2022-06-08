function msg(){
            let valornome=document.getElementById("nome").value;
            alert("Bem-vindo "+ valornome);
            document.getElementById("nome_d").value=document.getElementById("nome").value;
            document.getElementById("ok").innerHTML="Muito bem "+ valornome +" !";
        }
