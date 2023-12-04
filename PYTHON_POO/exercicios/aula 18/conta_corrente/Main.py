from Conta_Corrente import Acc_Corrente as Acc
import validations as val
from os import system

def instantiating_account() -> None:
    values = []
    while True:
        name = input("Insira seu nome: ")
        if(val.val_acc_name(name) == True):
            values.append(name.upper())
            break

    while True:
        num = input("Insira o dígito da conta: ")
        if(val.val_acc_num(num) == True):
            values.append(int(num))
            break

    account = Acc(values[0], values[1])
    system("cls")
    return account

def show_options() -> None:
    print(f"{'='*25}")
    print(f"|    1 -> alterar nome \t|")
    print(f"|    2 -> sacar   \t|")
    print(f"|    3 -> depositar  \t|")
    print(f"|    0 -> sair da aba  \t|")
    print(f'|   "q" -> encerrar  \t|')
    print(f"{'='*25}")

def display_acc_infos(acc) -> classmethod:
    return acc.get_info()

def new_acc_name(class_account) -> None:
    print('Digite "conta" para verificar informações da conta!')
    while True:
        new_name = input('Qual será o novo nome?: ').upper()
        if(new_name == "0"):
            system("cls")
            break
        elif(new_name.casefold() == "conta"): display_acc_infos(class_account)
        elif(val.val_acc_name(new_name) and new_name != class_account.name):
            class_account.name = new_name
            system("cls")
            return
        else:
            print("Insira um nome diferente do atual!")

def deposit_money(class_account) -> None:
    print('Digite "conta" para verificar informações da conta!')
    while True:
        deposit_value = input("Insira o valor do deposito: ")
        if(deposit_value.casefold() == "conta"): display_acc_infos(class_account)
        elif(deposit_value == "0"):
            system("cls")
            break
        elif(val.val_deposit(deposit_value, class_account)):
            deposit_value = float(deposit_value)
            class_account.balance = deposit_value
            system("cls")
            break

def remove_money(class_account) -> None:
    print('Digite "conta" para verificar informações da conta!')
    while True:
        drawout_value = input("Insira o valor do saque: ")
        if(drawout_value.casefold() == "conta"): display_acc_infos(class_account)
        elif(drawout_value == "0"):
            system("cls")
            break
        elif(val.val_money_value(drawout_value)):
            drawout_value = float(drawout_value)
            if(drawout_value <= class_account.balance):
                class_account.drawout_money(drawout_value)
                system("cls")
                return
            else:
                print("O valor do saque é maior que o saldo da conta!")

def call_account_method(option: int, class_account) -> None:
    match option:
        case 1:
            new_acc_name(class_account)
        case 2:
            remove_money(class_account)
        case 3:
            deposit_money(class_account)

def main() -> None:
    account = instantiating_account()
    while True:
        show_options()
        option = input()
        if(option == "q"): break
        elif(option == "conta"): display_acc_infos(account)
        elif(val.val_option(option)):
            option = int(option)
            call_account_method(option, account)
    return

main()