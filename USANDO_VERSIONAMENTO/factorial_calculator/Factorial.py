class Factorial:
    def __init__(self, num: int) -> None:
        self.__num = num
    
    @property
    def num(self):
        return self.__num
    
    def get_factorial(self):
        result = 1
        for num in range(self.num, 0, -1): # começa no número inserido, termina quando chegar a 1, incrementador = -1
            result *= num
        return result