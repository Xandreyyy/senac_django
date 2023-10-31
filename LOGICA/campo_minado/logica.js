const main = document.getElementById("field")

const column = 10

function createSquares(){
    let quadrado = document.createElement("div")
    quadrado.classList.add("square")
    return main.append(quadrado)
}

//
function insertElements(width){
    for (let i = 0; i <= width; i++){

        for (let j = 0; j < i; j++){
            createSquares()
        }

    }
}

insertElements(column)