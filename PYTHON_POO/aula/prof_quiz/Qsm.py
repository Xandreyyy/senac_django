from tkinter import *
from tkinter import messagebox as mb
import json

class Qsm:

    def __init__(self) -> None:
        self.pergunta_no = 0
        self.mostra_titulo()
        self.mostra_pergunta()
        self.op_escolhida = IntVar()
        self.opcao = self.radio_buttons()
        self.mostrar_opcoes()
        self.buttons()
        self.tam_dados = len(questao)
        self.correto = 0

    def mostrar_resultado(self):
        cont_err = self.tam_dados - self.correto
        correto = f'Acertos: {self.correto}'
        erros = f'Erros: {cont_err}'

        score = int(self.correto / self.tam_dados * 100)

        resultado = f'Placar: {score}'

        mb.showinfo('Resultado', f'{resultado}\n{correto}\n{erros}')
    
    def ver_pergunta(self, pergunta_no) -> bool:
        
        if self.op_escolhida.get() == resposta[pergunta_no]:
            return True

    def btnProx(self):
        if self.ver_pergunta(self.pergunta_no):
            self.correto += 1

        self.pergunta_no += 1

        if self.pergunta_no == self.tam_dados:
            self.mostrar_resultado()
            janela.destroy()
        else:
            self.mostra_pergunta()
            self.mostrar_opcoes()
    
    def buttons(self):
        btnProximo = Button(janela, 
                            text = 'Próxima', 
                            command = self.btnProx,
                            width = 10, bg = 'black', fg = 'white',
                            font = ('arial', 16, 'bold'))
        btnProximo.place(x = 350, y = 350)

        btnSair = Button(janela, 
                        text = 'Sair', 
                        command = janela.destroy,
                        width = 10, 
                        bg = 'black', 
                        fg = 'white',
                        font = ('arial', 16, 'bold'))
        
        btnSair.place(x = 700, y = 50)

    def mostrar_opcoes(self):
        val = 0
        
        self.op_escolhida.set(0)

        for op in opcoes[self.pergunta_no]:
            self.opcao[val]['text'] = op
            val += 1

    def mostra_pergunta(self):
        pergunta_no = Label(janela, text = questao[self.pergunta_no], width = 60,
        font = ('arial' ,16, 'bold' ), anchor = 'w' )
        pergunta_no.place(x = 70, y = 100)

    def mostra_titulo(self):
        titulo = Label(janela, text= 'Quiz', width = 50, bg = "green",fg = 'white', font = ('arial', 20, 'bold'))
        titulo.place(x = 0, y = 2)

    def radio_buttons(self):
        
        q_list = []
        
        y_pos = 150
        
        while len(q_list) < 5:
            
            radio_btn = Radiobutton(janela, text = ' ',variable = self.op_escolhida,
            value = len(q_list) + 1,font = ('arial', 14))
            
            q_list.append(radio_btn)
            
            radio_btn.place(x = 100, y = y_pos)
            y_pos += 40
    
        return q_list
    

janela = Tk()
janela.geometry('800x450')
janela.title('SENAC - Quiz')

with open('PYTHON_POO/aula/prof_quiz/dados.json') as f:
    dado = json.load(f)

questao = (dado['perguntas'])
opcoes = (dado['opcoes'])
resposta = (dado['resposta'])

qsm = Qsm()

janela.mainloop()