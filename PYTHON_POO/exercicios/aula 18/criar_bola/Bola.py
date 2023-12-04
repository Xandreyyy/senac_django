class Bola:
    def __init__(self, color: str, diam: int, material: str) -> None:
        self.color = color
        self.diam = diam
        self.material = material

    def trocar_cor(self, changed_color) -> None:
        last_color = self.color
        self.color = changed_color
        print(f'\nCor anterior: {(last_color).capitalize()}\nCor atual: {(self.color).capitalize()}')

    def mostrar_cor(self) -> None:
        print(f'\nAtual cor: {self.color}')

def validate_material(mat: str) -> str:
    allowed_mats = ["poliuretano", "borracha", "latex", "látex", "algodão", "algodao", "couro"]
    if(mat.casefold() in allowed_mats):
        return allowed_mats
    return False

def validate_diam(diam: str) -> int:
    try:
        diam = int(diam)
        if(diam % 1 == 0): return diam
        else: print("Insira o diâmetro em centímetros!")
    except ValueError:
        print("Insira o diâmetro da bola!")
        return False

def validate_color(color: str) -> str:
    if(not color.isalpha()):
        print("Cor inválida!")
        return False
    else: return color

def inputValue():
    msgs = ["Qual será o material da bola? ", "Qual será a cor da bola? ", "Qual será o diâmetro da bola? "]
    values = []
    cont = 0
    while cont < len(msgs):
        value = input(msgs[cont])
        i = msgs.index(msgs[cont])
        cont += 1
        match i:
            case 0:
                if(validate_material(value) != False):
                    values.append(validate_material(value))
                else: print(f"Material inválido! Lista dos materiais permitidos: \nPoliuretano;\nBorracha;\nLátex;\nAlgodão.")
            case 1:
                if(validate_color(value) != False):
                    values.append(validate_color(value))
            case 2:
                if(validate_diam(value) != False):
                    values.append(validate_diam(value))
    return values

ball_features = inputValue()
ball_obj = Bola(ball_features[0], ball_features[1], ball_features[2])