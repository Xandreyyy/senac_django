programa {
  funcao inicio() {
    inteiro numPrimo

    escreva("Informe ate qual numero voce deseja saber a quantidade de numeros primos: ")
    leia(numPrimo)

    //cada numero (de 0 ate numPrimo) e passado pela funcao verifPrimo
    para(inteiro cont = 0; cont <= numPrimo; cont++){
      se(verifPrimo(cont)){
        escreva(cont, " e primo\n")
      }senao{
        escreva(cont, " nao e primo\n")
      }
    }
  }

  //o numero passado pela funcao inicio e analisado de forma que, usando o operador "%", a var. acumulador (acc) armazena quantos
  //divisores o numero passado possui, e com base nisso retorna o valor booleano
  funcao inteiro verifPrimo(inteiro num){
    inteiro acc = 0

    se(num == 2) retorne verdadeiro

    para(inteiro i = 0; i <= num; i++){
      se(num % i == 0){
        acc++
      }
    }

    se(acc == 2) retorne verdadeiro
    senao        retorne falso     //kkkkkkkkkkkkkkkkk olha a organizacao dele
  }
}