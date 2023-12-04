from os import system
def val_name(person_name: str) -> bool:
    if(person_name.isalpha() and person_name.istitle()):
        return True
    elif(person_name.isalpha() and not person_name.istitle()):
        print("O nome deve conter apenas a primeira letra maiúscula!")
        return False
    elif(len(person_name) > 1):
        print("Insira apenas o 1º nome dela!")
        return False
    else:
        print("Esse nome não é válido!")
        return False

def val_years_old(years_old: str, person_name: str) -> bool:
    try:
        years_old = int(years_old)
        if(1 <= years_old <= 116):
            return True
        elif(years_old < 1):
            print("Preica ter pelo menos 1 ano de idade!")
            return False
        print(f"{person_name} não pode ser mais velho(a) que María Branyas!")
        return False
    except ValueError:
        print("A idade precisa ser um número inteiro!")
        return False

def val_weight(weight: str, person_name: str) -> bool:
    try:
        weight = float(weight)
        if(1 <= weight <= 635):
            return True
        elif(weight > 635):
            print(f"{person_name} não pode ser mais obeso(a) que Jon Brower!")
            return False
        else:
            print('É necessário inserir um valor positivo!')
            return False
    except ValueError:
        print("O peso precisa ser numérico!")
        return False

def val_hight(hight: str) -> int:
    try:
        hight = float(hight)
        if(hight <= 2.61):
            return True
        elif(hight >= 0.45):
            return True
        elif(hight > 2.61):
            print("Não é possível ser mais alto que 2.61m!")
            return False
        print("Não é possível ser menor que 0.45m (45cm)!")
        return False
    except ValueError:
        print("A idade precisa ser um número inteiro!")
        return False

def val_sex(sex: str) -> bool:
    sexes = ["feminino", "masculino", "fem", "mas", "f", "m"]
    if(sex.isalpha() and sex in sexes):
        return True
    else:
        print('Insira apenas "feminino" ou "masculino"!')
        return False

def val_option(opt: str) -> int:
    try:
        opt = int(opt)
        if(opt in range(1, 4)):
            return True
        else:
            system("cls")
            print("Esse número não está no intervalo de 1 a 3!")
            return False
    except ValueError:
        system("cls")
        print("Forneça apenas números!")
        return False