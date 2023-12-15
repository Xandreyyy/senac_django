from datetime import datetime as dt

class Person:
    def __init__(self, name: str, b_date: dt) -> None:
        self.__name = name
        self.__birth_date = b_date

    @property
    def name(self):
        return self.__name 

    @name.setter      
    def name(self, name: str) -> None:
        self.__name = name
    
    @property
    def b_date(self):
        return self.__birth_date

    @b_date.setter
    def b_date(self, b_date: str) -> None:
        self.__birth_date = b_date

    def get_years(self):
        return dt.today().year - self.b_date.year