from Aluno import Aluno

# a forma mais adequada para trabalhar com classes
# class Main:
#     # def main():
#     #     aluno = Aluno(nome='Alexandre', matricula='1234567', notas=[1, 2, 3, 4, 5])
    
#     # if __name__ == "__main__": main()

def validateMatricula(matr: str) -> int:
    if(len(matr) == 7):
        try:
            matr = int(matr)
            return matr
        except ValueError:
            print("Uma RA possuí 7 dígitos!")
            return False
        except Exception as exc:
            print(f"ERRO: {Exception}\n{type(exc)}, {exc}")
            return False
    else: return False

def validateNotas(nota: str) -> float:
    try:
        nota = float(nota)
        if(nota in range(0, 11)):
            return nota
        else: return False
    except ValueError:
            print("A nota precisa ser um número válido!")
            return False
    except Exception as exc:
        print(f"ERRO: {Exception}\n{type(exc)}, {exc}")
        return False

def getValues() -> list:
    student = input('Nome do aluno ("q" para sair): ')
    if(student.casefold() == 'q'): return 'q'
    messages = [f'Matrícula de {student}: ', 'Insira nota: ']
    values = [student]
    scores = []
    for i in messages:
        if(messages.index(i) == 1):
            while len(scores) < 5:
                inputValue = input(i)
                if(validateNotas(inputValue) != False):
                    scores.append(validateNotas(inputValue))
                    values.append(scores)
                else: print("Nota inválida!")
        else:
            inputValue = input(i)
            if(messages.index(i) == 0 and validateMatricula(inputValue) != False):
                values.append(validateMatricula(inputValue))
    return values

def instantiateAluno() -> None:
    students = []
    while True:
        arrData = getValues()
        if('q' in arrData): break
        alunoObj = Aluno(arrData[0], arrData[1], arrData[2])
        students.append(alunoObj.nome)
        alunoObj.Infos()
        print(f'\n\nTamanho da turma: {len(students)}\n{students}')

instantiateAluno()