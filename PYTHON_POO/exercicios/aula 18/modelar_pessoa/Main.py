from Person import Person as Pessoa
import validations as val
from os import system

def transform_sex_word(sex: str) -> str:
    if(sex.startswith("f")):
        sex = "feminino"
        return sex
    sex = "masculino"
    return sex

def instantiating_person() -> list:
    msgs = ["Qual será o nome dela?: ", "Quantos anos ela terá?: ", "Quantos quilos pesará?: ", "Qual será a sua altura?: ", "Qual é o sexo dela?: "]
    values = []
    count = 0
    while count < len(msgs):
        print("\n\tCriando uma pessoa...")
        value = input(msgs[count])
        if(value == "q"): return False
        system("cls")
        index = msgs.index(msgs[count])
        match index:
            case 0:
                if(val.val_name(value) == True):
                    values.append(value)
                    count += 1
            case 1:
                if(val.val_years_old(value, values[0]) == True):
                    value = int(value)
                    values.append(value)
                    count += 1
            case 2:
                if(val.val_weight(value, values[0]) == True):
                    value = float(value)
                    values.append(value)
                    count += 1
            case 3:
                if(val.val_hight(value) == True):
                    value = float(value)
                    values.append(value)
                    count += 1
            case 4:
                if(val.val_sex(value) == True):
                    values.append(transform_sex_word(value))
                    count += 1
    return values

def call_Person_methods(ipt: int, class_person) -> classmethod:
    match ipt:
        case 1:
            year_old = input(f"Quantos anos você deseja envelhecer {class_person.refer} {class_person.name}?: ")
            if(val.val_years_old(year_old, class_person.name) == True):
                system("cls")
                year_old = int(year_old)
                return class_person.set_older(year_old)
        case 2:
            weight = input(f"Quantos kg você deseja adicionar n{class_person.refer} {class_person.name}?: ")
            if(val.val_weight(weight, class_person.name) == True):
                system("cls")
                weight = float(weight)
                return class_person.set_weight(weight)
        case 3:
            lose_weight = input(f"Quantos kg você deseja remover d{class_person.refer} {class_person.name}?: ")
            if(val.val_weight(lose_weight, class_person.name) == True):
                system("cls")
                lose_weight = float(lose_weight)
                return class_person.set_lose_weight(lose_weight)

def select_option() -> int:
    print(f"{'='*25}")
    print(f"|   1 -> envelhecer   \t|")
    print(f"|   2 -> engordar   \t|")
    print(f"|   3 -> emagrecer   \t|")
    print(f"{'='*25}")
    option = input("Digite a opção desejada: ")
    if(option == "q"): return False
    elif(val.val_option(option)):
        option = int(option)
        return option

def main():
    values = instantiating_person()
    if(values == False): return
    person = Pessoa(values[0], values[1], values[2], values[3], values[4])
    person.get_infos()
    print('Use "q" para encerrar!')
    while True:
        custom = select_option()
        if(custom == False): break
        call_Person_methods(custom, person)
        person.get_infos()

main()