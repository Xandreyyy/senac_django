#0000000 (7 dígitos)
def addStudent() -> str:
    student = input('Insira o RA do aluno ("q" sair): ')
    if(student == "q"): return False
    elif(len(student) == 7 and student.isdigit()):
        student += ";"
        return student
    else: print("RA inválido!")

with open(file="./LOGICA/corrigir_prova/students_score.csv", mode="w") as file_scores:
    while True:
        student = addStudent()
        if(student == False): break
        file_scores.write(student)