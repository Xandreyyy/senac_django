import tkinter as tk
from Word import Word

def reverse_input() -> str:
    string = Word(ipt.get())
    final_result = string.get_reversed()
    return result.config(text = final_result)

root = tk.Tk()
root.geometry('300x300')
root.resizable(False, False)
root.title('REVERSE WORDS v300 by Leonidas (300 SPARTANS vs 30k PERSIANS) GAMER HIGHT DEFINITION')

# o wrapper da parte direita
frame = tk.Frame(root)
frame.grid(row = 0, column = 1, sticky = 'w')

# labels
label = tk.Label(root, text = 'Enter a word:', font = ('Arial', 15))
label.grid(row = 0, column = 0, sticky = 'n')

final_result = str()
result = tk.Label(frame, text = final_result, font = ('Arial', 14))
result.grid(row = 1, column = 1, sticky = 'wn')

# input
ipt = tk.Entry(frame, width = 20, font = ('Arial', 15))
ipt.grid(row = 0, column = 1, padx = 3)

# botão
btn = tk.Button(frame, text = 'REVERSE', command = reverse_input, width = 15, height = 2)
btn.grid(row = 2, column = 1, sticky = 'wn')

root.mainloop()