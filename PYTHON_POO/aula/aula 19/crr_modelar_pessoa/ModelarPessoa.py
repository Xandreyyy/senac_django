class Pessoa:
    # ao instanciar esta classe, o "def __innit__" recebe o nome da classe, temos: Pessoa(atributos)
    # o sufixo "__" (dunders, double underscores), signfica que esses atributos são privados
    def __init__(self, nome: str, idade: int, peso: float, altura: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
    
    #"property" diz que este método serve para retornar o atributo
    @property
    def nome(self) -> str:
        return self.__nome
    
    #"método.setter" 
    @nome.setter
    def nome(self, nome) -> None:
        self.__nome = nome

    @property
    def idade(self) -> int:
        return self.__idade

    @idade.setter
    def idade(self, idade) -> None:
        self.__idade = idade

    @property
    def peso(self) -> float:
        return self.__peso
    
    @peso.setter
    def peso(self, peso) -> None:
        self.__peso = peso
    
    @property
    def altura(self) -> float:
        return self.__altura
    
    @altura.setter
    def altura(self, altura) -> None:
        self.__altura = altura

    def crescer(self) -> None:
        self.altura += 0.05

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer()
    
    def engordar(self) -> None:
        self.peso += 1

    def emagrecer(self) -> None:
        self.peso -= 1