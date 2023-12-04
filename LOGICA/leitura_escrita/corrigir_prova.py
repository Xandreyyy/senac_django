from os import system
studentsAnswer = "./LOGICA/leitura_escrita/students_score.csv"
answersSheet = "./LOGICA/leitura_escrita/answer_sheet.csv"

def add_student() -> str:
    while True:
        student = input('Insira o RA do estudante ("q" sair): ')
        if(student == "q"):
            system("cls")
            return False
        elif(len(student) == 7 and student.isdigit()):
            student += ";"
            return student
        else:
            print("RA inválido!")

def add_students_answ(student: str, answer_num: int) -> str:
    while True:
        # fatiei a str "student" para remover o ";"
        answer = input(f'Insira a resposta da {answer_num}ª questão do estudante {student[0:-1]} ("q" sair): ').casefold()
        if(answer == "q"): return False
        elif(len(answer) == 1 and answer in ["a", "b", "c", "d", "e"]):
            answer += ";"
            return answer
        else:
            print("Resposta inválida!")

def calc_percent(score: float, totalAns: int) -> str:
    average = score / totalAns
    percent = average * 100
    return f'{str(int(percent))}%'

# define a quantidade de perguntas -> criando e escrevendo no arquivo que contém o gabarito
def define_answers_sheet() -> int:
    with open(file=answersSheet, mode="w", encoding="utf8") as answers_sheet:
        answers_sheet.write("GABARITO\n") # cabeçalho
        total_answers = 1
        print('Olá, professor! Você define quantidade de respostas, para finalizar digite "q"!\n')

        while True:
            rightAnswer = input(f"Defina a reposta correta para a {total_answers}ª questão: ").casefold()
            if(rightAnswer == "q"): break
            elif(rightAnswer in ["a", "b", "c", "d", "e"]):
                answers_sheet.write(f"Questão {total_answers}: {rightAnswer}\n")
                total_answers += 1
            else:
                print('Insira apenas "a", "b", "c", "d" ou "e"!')
    return total_answers

# AQUI ACONTECE A INTERAÇÃO COM O USUÁRIO
# 1º: define o cabeçalho do "file_scores" com o RA dos alunos, 2º: escreve a resposta de cada aluno no arquivo
def define_students_answers() -> None:
    with open(file=studentsAnswer, mode="w", encoding="utf8") as file_scores:
        students = [] # lista usada para citar o RA do aluno ao pedir o input do usuário
        total_answers = define_answers_sheet()

        while True:
            student = add_student()
            if(student == False):
                file_scores.write("\n")
                break
            file_scores.write(student)
            students.append(student)

        # para cada aluno pede a sua resposta, então temos: pergunta 1 -> pede a resposta da pergunta 1 de cada aluno, assim sucessivamente...
        answer_num = 1
        while answer_num <= total_answers:
            for i in range(len(students)):
                answer = add_students_answ(students[i], answer_num)
                if(answer == False): break
                file_scores.write(answer)
                if(i == len(students) - 1):
                    file_scores.write("\n")
            answer_num += 1

def get_answers_sheet() -> list:
    with open(file=answersSheet, mode="r") as answers_sheet:
        answers_sheet.readline() # descontar o cabeçalho
        answers = []
        for i in answers_sheet:
            i = i.split() # transforma a linha em um array de strings
            answer = i[-1] # a letra que representa a resposta sempre é o último item do array
            answers.append(answer)

    return answers

def get_students_answers() -> list:
    with open(file=studentsAnswer, mode="r") as file_scores:
        scoreRow = file_scores.readline()
        scores = []
        while scoreRow:
            scoreRow = file_scores.readline()
            rowSplitted = scoreRow.split(";")
            scores.append(rowSplitted)
        scores.pop(-1) # remove lista vazia
    return scores

def calc_students_result() -> dict:
    studentsResult = dict()
    students_answers, answerssheet = get_students_answers(), get_answers_sheet()
    allStudents = len(students_answers[0]) - 1 # pega a 1ª lista de respostas e desconta o item "\n"
    indexCount = 0

    while indexCount < allStudents:
        answerScore = 0
        sep = ';' if indexCount < allStudents - 1 else '\n'
        for arr in students_answers:
            if(arr[indexCount] == answerssheet[indexCount]):
                answerScore += 1

        studentsResult.update({f'{str(answerScore)}{sep}': f'{calc_percent(answerScore, len(students_answers))}{sep}'})
        indexCount += 1

    return studentsResult

def add_students_result() -> None:
    with open(file=studentsAnswer, mode='a') as file_scores:
        final_result = calc_students_result()

        for key in final_result.keys():
            file_scores.write(key)
        for value in final_result.values():
            file_scores.write(value)

        system("cls")
        print("*Cada item é um aluno\n\n*Chave: representa nota\n*Valor: representa porcentagem da média\n")
        print(final_result)

def main() -> None:
    define_students_answers()
    calc_students_result()
    add_students_result()

main()