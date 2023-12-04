from Pessoa import Pessoa

class Principal:
    pessoa1 = Pessoa(altura=1.80, idade=20, nome="Eduardo", peso=80, etnia="indígena")

    pessoa1.cumprimentar()
    pessoa1.cozinhar('pizza')
    pessoa1.andar(20)