class Person:
    def __init__(self, name:str, years_old: int, weight: float, hight: float, sex: str) -> None:
        self.__name = name
        self.__years_old = years_old
        self.__weight = weight
        self.__hight = hight
        self.__sex = sex
        self.__refer = 'a' if sex.startswith("f") else 'o'

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name) -> None:
        self.__name = name
    
    @property
    def years_old(self) -> int:
        return self.__years_old
    
    @years_old.setter
    def years_old(self, year) -> None:
        self.__years_old = year
    
    @property
    def weight(self) -> float:
        return self.__weight
    
    @weight.setter
    def weight(self, weight) -> None:
        self.__weight = weight
    
    @property
    def hight(self) -> float:
        return self.__hight
    
    @hight.setter
    def hight(self, hight) -> None:
        self.__hight = hight
    
    @property
    def sex(self) -> str:
        return self.__sex
    
    @sex.setter
    def sex(self, sex) -> None:
        self.__sex = sex

    @property
    def refer(self) -> str:
        return self.__refer

    def set_hight(self) -> None:
        self.hight += 0.05

    def set_older(self, year: int) -> None:
        count = 1
        while count <= year:
            self.years_old += 1
            if(self.years_old < 21):
                self.set_hight()
            count += 1

    def set_weight(self, weight: float) -> None:
        self.weight += weight

    def set_lose_weight(self, weight: float) -> None:
        self.weight -= weight

    def get_infos(self) -> None:
        print(f"\nNome: {self.name}\nSexo: {self.sex}")
        print(f"Idade: {self.years_old} anos\nPeso: {self.weight}kg")
        print(f"Altura: {self.hight:.2f}m")