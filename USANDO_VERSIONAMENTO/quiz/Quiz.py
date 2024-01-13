import tkinter as tk
from tkinter import messagebox
import json
import random

class Quiz:
    def __init__(self) -> None:
        self.__questions = list()
        self.__answers = list()
        self.__question_number = int()
        self.__screen_elements = list()
        self.__question = str()
        self.__answer = str()
        self.__user_answer = tk.StringVar(value = ' ')
        self.__score = int()
        self.__misses = int()
        self.load_data()
        self.display_title()
        self.generate_question_label()
        self.generate_answers_buttons()
        self.display_elements()
        self.display_next_button()

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

    @property
    def score(self) -> str:
        return self.__score

    @property
    def screen_elements(self) -> list:
        return self.__screen_elements

    @property
    def misses(self) -> int:
        return self.__misses

    @property
    def question_number(self) -> int:
        return self.__question_number

    @questions.setter
    def questions(self, questions_list: list) -> None:
        self.__questions = questions_list

    @answers.setter
    def answers(self, answers_list: list) -> None:
        self.__answers = answers_list

    @question.setter
    def question(self, question: str) -> None:
        self.__question = question

    @answer.setter
    def answer(self, answer: str) -> None:
        self.__answer = answer

    @user_answ.setter
    def user_answ(self, answer: str) -> None:
        self.__user_answer = answer
    
    @screen_elements.setter
    def screen_elements(self, screen_el: tk) -> None:
        self.__screen_elements = screen_el

    @score.setter
    def score(self, score: int) -> None:
        self.__score = score

    @misses.setter
    def misses(self, miss) -> None:
        self.__misses = miss

    @question_number.setter
    def question_number(self, number) -> None:
        self.__question_number = number

    # BACK -----
    def load_data(self) -> None:
        with open("./USANDO_VERSIONAMENTO/quiz/data.json", encoding = 'UTF-8') as data_quiz:
            data = data_quiz.read()
            questions_and_answers = json.loads(data)

        self.questions = questions_and_answers['questions']
        self.answers = questions_and_answers['answers']
    
    def random_question(self) -> int:
        random_question_index = random.randint(0, len(self.questions) - 1)
        print(f"\nEscolhido: {random_question_index}")
        print(f"Len: {len(self.questions)}")
        self.question_number = random_question_index

        return random_question_index
    
    def select_question(self) -> int:
        random_question = self.random_question()
        question_keys = list(self.questions[random_question].keys())
        question_values = list(self.questions[random_question].values())

        self.question = question_keys[0] # select the question number (q1, q2, etc...)
        self.answer = question_values[1] # select the right answer

        return random_question

    def get_question(self) -> str:
        question = self.questions[self.select_question()]

        return question.get(self.question) # return the question number value, ex: p1: <question> -> return the "<question> text"
    
    def next_button(self) -> None:
        answer = self.user_answ.get()

        if answer != ' ' and len(self.questions) != 0:

            if answer == self.answer:
                self.score += 1
            else:
                self.misses += 1

            self.questions.pop(self.question_number)
            self.display_elements()
        elif len(self.questions) == 0:
            messagebox.showinfo(title = "JOGO TERMINADO", message = f"Acertos: {self.score}\nErros: {self.misses}")
    # BACK -----

    # GUI  -----
    def display_title(self) -> None:
        h1 = tk.Label(root, text = 'QUIZIZINHO', font = ('Arial', 34, 'bold'), bg = 'darkblue', fg = 'white', pady = 5)
        h1.grid(row = 0, column = 0, sticky = 'ew')

    def generate_question_label(self) -> None:
        question_text = tk.Label(root)

        self.screen_elements.append(question_text)
        question_text.grid(row = 1, column = 0, sticky = 'w')

    def generate_answers_buttons(self) -> None:
        answers_frame = tk.Frame(root)
        first_list = self.answers[0]["q1"]
        count = 0

        while count <= len(first_list) - 1:

            option = tk.Radiobutton(answers_frame, variable = self.user_answ)
            self.screen_elements.append(option)

            option.grid(row = count, column = 0, sticky = 'w')

            count += 1

        answers_frame.grid(row = 2, column = 0, sticky = 'w')

    def get_answers_question(self) -> list:
        for answer in self.answers:
            question_number = list(answer.keys())[0]

            if question_number == self.question:
                return list(answer.values())[0]

    def display_elements(self) -> None:
        self.screen_elements[0]['text'] = self.get_question()
        answers_text = self.get_answers_question()
        i = 0

        for element in self.screen_elements:
            if self.screen_elements.index(element) != 0:
                element['text'] = answers_text[i]
                element['value'] = answers_text[i]

                i += 1

    def display_next_button(self):
        next_btn = tk.Button(root, text = 'PRÓXIMA', command = self.next_button)
        next_btn.grid(row = 3, column = 0, sticky = 'w')
    # GUI  -----

root = tk.Tk()
root.geometry("600x500")
root.title("SENAC question game v3000")
quiz_class = Quiz()

root.mainloop()