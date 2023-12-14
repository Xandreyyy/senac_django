import tkinter as tk
from tkinter import messagebox
from datetime import datetime as dt
from Person import Person

def calc_years_old() -> None:
    person1 = Person(i_nome.get(), dt(int(i_year.get()), int(i_month.get()), int(i_day.get())))
    messagebox.showinfo(title = 'RESULTADO', message = person1.get_years())



def reset_input() -> None:
    ipts = [i_nome, i_day, i_month, i_year]
    for ipt in ipts:
        ipt.delete(0, tk.END)

# cria frame principal
root = tk.Tk()
root.geometry('400x450')
root.title("AGE CALCULATOR")
root.resizable(False, False)

# criar labels
name = tk.Label(root, text = 'Insira seu nome: ', padx = 2, font = ('sans-serif', 12, 'bold'))
name.grid(row = 0, column = 0, sticky = "w")

day = tk.Label(root, text = 'Insira o dia de nascimento: ', padx = 2, font = ('sans-serif', 12, 'bold'))
day.grid(row = 2, column = 0, sticky = "w")

month = tk.Label(root, text = 'Insira o mês de nascimento: ', padx = 2, font = ('sans-serif', 12, 'bold'))
month.grid(row = 4, column = 0, sticky = "w")

year = tk.Label(root, text = 'Insira o ano de nascimento: ', padx = 2, font = ('sans-serif', 12, 'bold'))
year.grid(row = 6, column = 0, sticky = "w")

# criar inputs
i_nome = tk.Entry(root, width = 14, font = ('sans-serif', 12))
i_nome.grid(row = 1, column = 0, sticky = "w")

i_day = tk.Entry(root, width = 14, font = ('sans-serif', 12))
i_day.grid(row = 3, column = 0, sticky = "w")

i_month = tk.Entry(root, width = 14, font = ('sans-serif', 12))
i_month.grid(row = 5, column = 0, sticky = "w")

i_year = tk.Entry(root, width = 14, font = ('sans-serif', 12))
i_year.grid(row = 7, column = 0, sticky = "w")

# criar botões limpar campos e OK
btn_ok = tk.Button(root, text = 'OK', width = 8, command = calc_years_old)
btn_ok.grid(row = 8, column = 0)

btn_clear = tk.Button(root, text = 'LIMPAR', width = 8, command = reset_input)
btn_clear.grid(row = 8, column = 1)

root.mainloop()