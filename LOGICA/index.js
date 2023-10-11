//necessário para usar o prompt() ⬇
const prompt = require("prompt-sync")()

let salas = [], especificarSala = null, conserto

function main(salas, especificarSala) {
    mostrarMsg("primeira msg")
    for (let i = 0; i < especificarSala; i++){
        salas.push(criarSalas(i+1))
    }

    mostrarMsg("segunda msg")
    for (let i = 0; i < salas.length; i++){
        if(especificarSala === salas[i].n_sala){
            salas[i].defeito = true
        }
    }

    mostrarMsg("terceira msg")
    consertar(conserto)
}

function mostrarMsg(string){
    switch(string){
        case "primeira msg":
            especificarSala = Number(prompt("Insira a quantidade de salas: "))
            break
        case "segunda msg":
            especificarSala = Number(prompt("Agora, por favor, eu te imploro, me diz qual é a sala que deve ter a lâmpada danificada? "))
            break
        case "terceira msg":
            conserto = prompt("Eu que estreguei, eu que conserto. Quer que eu conserte? (s/n): ")
            break
        default:
            console.log("Ao chamar a funcao passse apenas 1 ou 2 como arg..")
    }
    return especificarSala
}

function criarSalas(index){
    return{
        n_sala: index,
        defeito: false
    }
}

function consertar(conserto) {
    if(conserto === "s"){
        for (let i = 0; i < salas.length; i++){
            if(especificarSala === salas[i].n_sala){
                salas[i].defeito = false
                console.log(`Encontrei a sala com defeito! Sala: ${salas[i].n_sala}. Lampada consertada.`)
            }else{
                console.log(`Okay, a sala ${salas[i].n_sala} não está danificada.`)
            }
        }
    }else{
        console.log("Vazei entao")
    }
    return
}

main(salas, especificarSala)





















/*Prompt não é definido?
     https://discuss.codecademy.com/t/prompt-is-not-defined/453608/2
*/

/*const url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

async function pegarCotacao(){
    const response = await fetch(url)
    return response.json()
}

pegarCotacao().then(response =>{
    console.log(response);
})
*/