import tkinter as tk
from tkinter import messagebox
from Text import Text

def is_letter(right_ipt, left_ipt):
    if(right_ipt.isalpha() and left_ipt.isalpha()):
        return True
    else: return False

def is_diff(right_ipt, left_ipt):
    if(right_ipt != left_ipt):
        return True
    else: return False

def is_char(right_ipt, left_ipt):
    if(len(right_ipt) == 1 and len(left_ipt) == 1):
        return True
    else: return False

def replace_char():
    selected_char, replace_char = to_replace.get(), replace_letter.get()

    if(is_letter(selected_char, replace_char) and is_diff(selected_char, replace_char) and is_char(selected_char, replace_char)):
        new_text = Text(def_text, selected_char, replace_char)
        replaced_txt['text'] = new_text.get_text()
    elif(is_letter(selected_char, replace_char) == False):
        messagebox.showerror(title = 'ERRO', message = 'Insira apenas letras!')
    elif(is_char(selected_char, replace_char) == False):
        messagebox.showerror(title = 'ERRO', message = 'Insira uma única letra!')
    elif(is_diff(selected_char, replace_char) == False):
        messagebox.showerror(title = 'ERRO', message = 'As letras precisam ser diferentes!')

def_text = 'Ut condimentum mi placerat\nlibero dictum semper. In non\ntortor posuere, porta lacus at,\naliquet justo. Nunc laoreet ac-\ncumsan eleifend. Donec iacu\nlisultricies nisi, ac pharetra ma\nurisvulputate vitae. Nivamus la-\noreet pretium vehicula.'
root = tk.Tk()
root.geometry('550x550')
root.grid_anchor('center')
root.title('REPLACE TEXT LETTER v3000')

# frames
left_container = tk.Frame(root)
left_container.grid(row = 0, column = 0)

middle_container = tk.Frame(root)
middle_container.grid(row = 0, column = 1)

right_container = tk.Frame(root)
right_container.grid(row = 0, column = 2)

# inputs
to_replace = tk.Entry(left_container)
to_replace.grid(row = 0, column = 0)

replace_letter = tk.Entry(right_container)
replace_letter.grid(row = 0, column = 1)

# textos
default_text = tk.Label(left_container, text = def_text, justify = 'left', font = (13))
default_text.grid(row = 1, column = 0)

replaced_txt = tk.Label(right_container, text = def_text, justify = 'left', font = (13))
replaced_txt.grid(row = 1, column = 1)

# botão
btn = tk.Button(middle_container, text = '➡', width = 7, command = replace_char, activeforeground='red')
btn.grid(row = 1, column = 0)

root.mainloop()