import tkinter as tk
import json
import random

class Quiz:
    def __init__(self) -> None:
        self.__questions = list
        self.__answers = list
        self.__question = str
        self.__answer = str
        self.load_data()
        self.display_title()
        self.display_question()
        self.display_anwers()

    # BACK -----
    @property
    def questions(self) -> list:
        return self.__questions

    @property
    def answers(self) -> list:
        return self.__answers

    @property
    def question(self) -> tuple:
        return self.__question

    @property
    def answer(self) -> tuple:
        return self.__answer

    @questions.setter
    def questions(self, questions_list: list):
        self.__questions = questions_list

    @answers.setter
    def answers(self, answers_list: list):
        self.__answers = answers_list

    @question.setter
    def question(self, question: str):
        self.__question = question

    @answer.setter
    def answer(self, answer: str):
        self.__answer = answer

    def load_data(self) -> None:
        with open("./USANDO_VERSIONAMENTO/quiz/data.json", encoding = 'UTF-8') as data_quiz:
            data = data_quiz.read()
            questions_and_answers = json.loads(data)

        self.questions = questions_and_answers['questions']
        self.answers = questions_and_answers['answers']
    
    def random_question(self) -> int:
        random_question_index = random.randint(0, len(self.questions) - 1)
        return random_question_index
    # BACK -----

    # GUI  -----
    def display_title(self) -> None:
        h1 = tk.Label(root, text = 'QUIZIZINHO', font = ('Arial', 34, 'bold'), bg = 'darkblue', fg = 'white', pady = 5)
        h1.grid(row = 0, column = 0, sticky = 'ew')

    def new_question(self) -> None:
        random_question = self.random_question()
        question_keys = list(self.questions[random_question].keys())
        question_values = list(self.questions[random_question].values())

        self.question = question_keys[0] # select the question number (q1, q2, etc...)
        self.answer = question_values[1] # select the right answer
        
        question = self.questions[random_question]
        return question.get(self.question) # return the question number value, ex: p1: <question> -> return the "<question>"

    def display_question(self) -> None:
        label = tk.Label(root, text = self.new_question())
        label.grid(row = 1, column = 0)

    def display_anwers(self) -> None:
        pass
    
    # GUI  -----

root = tk.Tk()
root.geometry("600x500")
root.title("SENAC question game v3000")
quis = Quiz()


root.mainloop()