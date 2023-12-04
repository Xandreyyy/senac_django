def val_acc_name(name: str) -> bool:
    list_name = name.split()
    no_spaces_name = ''.join(list_name)
    if(no_spaces_name.isalpha() and len(no_spaces_name) > 2):
        return True
    else:
        print("Nome inválido!")
        return False

def val_acc_num(acc_num: str) -> bool:
    try:
        acc_num = float(acc_num)
        if(acc_num % 1 != 0):
            print("O número da conta é um número inteiro!")
            return False
        elif(acc_num in range(1, 10)):
            return True
        elif(acc_num > 9):
            print("O número da conta deve ser apenas um dígito!")
            return False
        else:
            print("O número da conta precisa ser positivo!")
            return False
    except ValueError:
        print("Número de conta inválido.")
        return False

def val_money_value(money_value: str) -> bool:
    try:
        money_value = float(money_value)
        if(money_value > 0):
            return True
        elif(money_value == 0):
            return False
        else:
            print("Não é possível inserir valores negativos.")
            return False
    except ValueError:
        print("Insira um valor numérico!")
        return False

def val_deposit(money_value: str, class_account) -> bool:
    if(val_money_value(money_value)):
        money_value = float(money_value)
        if(money_value >= class_account.balance):
            return True
    else: return False

def val_option(option: str) -> bool:
    if(option.casefold() == "conta"): return
    try:
        option = int(option)
        if(option == 0):
            print("Essa opção só pode ser usada dentro de uma aba!")
        elif(option in range(1, 4)):
            return True
        else:
            print("Essa opção não existe! Selecione apenas: 1, 2 ou 3\n")
            return False
    except ValueError:
        print("Insira apenas números!")