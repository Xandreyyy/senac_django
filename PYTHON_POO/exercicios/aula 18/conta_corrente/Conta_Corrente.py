class Acc_Corrente:
    def __init__(self, acc_name: str, acc_num: int, acc_balance: float = 0.0) -> None:
        self.__name = acc_name
        self.__num = acc_num
        self.__balance = acc_balance

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

    @property
    def num(self) -> int:
        return self.__num

    # não é necessário método para alterar o dígito da conta

    @property
    def balance(self) -> str:
        return self.__balance

    @balance.setter
    def balance(self, money_value: float) -> None:
        self.__balance += money_value

    def drawout_money(self, value: float) -> None:
        self.balance -= value

    def get_info(self) -> None:
        print(f'\nNome: {self.name}\nNúmero da conta: {self.num}')
        print(f'Saldo: R${self.balance}')