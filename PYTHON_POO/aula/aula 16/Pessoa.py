class Pessoa:
    def __init__(self, nome: str, altura: float, idade: int, etnia: str, peso: int) -> None:
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.etnia = etnia
        self.peso = peso

    #precisamos de métodos para acessar esses valores
    def cumprimentar(self) -> None:
        print(f"\nOlá, meu nome é {self.nome}")

    def andar(self, distancia: int) -> None:
        print(f"\nSaí para caminhar, volto quando terminar de caminhar {distancia} metros!")
        for i in range(1, distancia + 1):
            print(f"Caminhei {i} metros!")
        print("\nCheguei!")
        
    def cozinhar(self, receita: str) -> None:
        print(f"\nEstou cozinhando um(a) {receita}!")