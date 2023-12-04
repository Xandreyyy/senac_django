class Aluno:
    def __init__(self, nome: str, matricula: int, notas: list) -> None:
        self.nome = nome
        self.matricula = matricula
        self.notas = notas

    def SumNotas(self):
        sum = 0
        for nota in self.notas:
            sum += nota
        return sum

    def CalcAverage(self):
        return self.SumNotas() / len(self.notas)

    def Infos(self):
        print(f"\nAluno: {self.nome}\nMatrícula: {self.matricula}")
        print(f"Notas: {', '.join(str(nota) for nota in self.notas)}\nMédia: {self.CalcAverage()}")