import tkinter as tk
from tkinter import messagebox
import json
import random

class Quiz:
    def __init__(self) -> None:
        self.__questions = list
        self.__answers = list
        self.__question = str
        self.__answer = str
        self.__user_answer = tk.StringVar(value = ' ')
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
    def question(self) -> str:
        return self.__question

    @property
    def answer(self) -> str:
        return self.__answer

    @property
    def user_answ(self) -> str:
        return self.__user_answer

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

    @user_answ.setter
    def user_answ(self, answer: str):
        self.__user_answer = answer

    def load_data(self) -> None:
        with open("./USANDO_VERSIONAMENTO/quiz/data.json", encoding = 'UTF-8') as data_quiz:
            data = data_quiz.read()
            questions_and_answers = json.loads(data)

        self.questions = questions_and_answers['questions']
        self.answers = questions_and_answers['answers']
    
    def random_question(self) -> int:
        random_question_index = random.randint(0, len(self.questions) - 1)
        return random_question_index
    
    def new_question(self) -> str:
        random_question = self.random_question()
        question_keys = list(self.questions[random_question].keys())
        question_values = list(self.questions[random_question].values())

        self.question = question_keys[0] # select the question number (q1, q2, etc...)
        self.answer = question_values[1] # select the right answer
        
        question = self.questions[random_question]
        return question.get(self.question) # return the question number value, ex: p1: <question> -> return the "<question> text"

    def clicked(self, value):
        print(value)

    def get_answers(self, answers: list) -> None:
        answers_frame = tk.Frame(root)
        count = 0
        for answer in answers:
            label = tk.Radiobutton(answers_frame, text = answer, command = lambda btn_value = answer: self.clicked(btn_value))
            label.grid(row = count, column = 0, sticky = 'w')
            count += 1

        answers_frame.grid(row = 2, column = 0, sticky = 'w')
    # BACK -----

    # GUI  -----
    def display_title(self) -> None:
        h1 = tk.Label(root, text = 'QUIZIZINHO', font = ('Arial', 34, 'bold'), bg = 'darkblue', fg = 'white', pady = 5)
        h1.grid(row = 0, column = 0, sticky = 'ew')

    def display_question(self) -> None:
        question_text = tk.Label(root, text = self.new_question())
        question_text.grid(row = 1, column = 0, sticky = 'w')

    def display_anwers(self) -> None:
        for answer in self.answers:
            question_number = list(answer.keys())[0]

            if question_number == self.question:
                self.get_answers(answer[question_number])
                return
    # GUI  -----

root = tk.Tk()
root.geometry("600x500")
root.title("SENAC question game v3000")
quis = Quiz()

root.mainloop()