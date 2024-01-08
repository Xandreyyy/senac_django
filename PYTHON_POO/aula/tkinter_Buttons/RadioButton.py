import tkinter as tk
from tkinter.messagebox import *

def mostrar_escolha():
    showinfo(title = 'RESULTADO', message = f'Você escolheu {tamanho_selecionado.get()}')

root = tk.Tk()
root.geometry('400x400')
root.resizable(False, False)
root.title('Radio button')

label = tk.Label(root, text = 'Escolha o tamanho: ')
label.grid()

tamanho_selecionado = tk.StringVar(root, value = 'M')
tamanhos = (('Pequeno', 'P'),
            ('Médio', 'M'),
            ('Grande', 'G'),
            ('Extra Grande', 'XG'),
            ('Extra Extre Grande', 'XXG')
           )

for i in range(len(tamanhos)):
    rd = tk.Radiobutton(root, text = tamanhos[i][0], value = tamanhos[i][1], variable = tamanho_selecionado, padx = 3, pady = 3)
    rd.grid(sticky = 'w')

btn_escolha = tk.Button(root, text = 'LER TAMANHO', command = mostrar_escolha)
btn_escolha.grid()

root.mainloop()