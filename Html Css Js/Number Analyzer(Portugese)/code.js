//função para alertar caso algo dê errado
function alert(){
    var alerta = document.getElementById("alerta")
    return alerta.innerText = "Algum número inválido/repetido ou a caixa está vazia!"
}

//função para checar se o número já foi colocado
function numRepetido(num){
    v = numerosFila.includes(num)
    return v
}

//Variáveis para guardar os números que passam
var i = 0
i = Number(i)
var numerosFila = []
var fila = document.getElementById("nfila")

//função para adicionar os números um a um na section
function adicionar(){
    let numInput = document.getElementById("ntxt")
    var num = Number(numInput.value)
    alerta.innerText = ""

    if(num == ''|| num < 0 || num > 100|| numRepetido(num) == true){
        alert()
    }
    else{
        //para aaprecer os valores na section
        let item = document.createElement("option")
        item.text = `Número ${num}`
        item.id = `item${i}`
        fila.appendChild(item)

        //agora para guardar numa array os números
        numerosFila[i] = num
        i++
    }
}

//função para trazer os resultados finais
function finalizar(){
    if(numerosFila.length <= 1){
        alert()
    }
    else{
        let res = document.getElementById("res")
        res.innerHTML = ""

        
        //tamanho da array
        let tamanho = numerosFila.length
        
        //soma de todos os números
        let soma = Number()
        for(cont in numerosFila){
            soma += numerosFila[cont]
        }
        
        //média dos números
        let media = soma / tamanho
        
        //maior número
        let maior = Math.max.apply(null, numerosFila)

        res.innerHTML = `Os números foram: ${numerosFila}<br>
        Em ordem crescente fica ${numerosFila.sort()}<br>
        Foram ${tamanho} números<br>
        A soma dos números deu: ${soma}<br>
        A média dos números foi de ${media}<br>
        O maior número digitado foi: ${maior}`

        //limpando os campos anteriores
        fila.innerText = ""
        numerosFila = []
        i = 0
    }
}

