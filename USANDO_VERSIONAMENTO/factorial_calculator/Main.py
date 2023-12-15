import tkinter as tk
from Factorial import Factorial

def calc_factorial():
    num = Factorial(ipt.get())
    result['text'] = num.get_factorial()

root = tk.Tk()
root.geometry('300x300')
root.resizable(False, False)
root.title('FACTORIAL CALCULATOR 3000')

frame = tk.Frame(root)
frame.grid(row = 0, column = 1)

# labels
label = tk.Label(root, text = 'Enter a number:', font = ('Rockwell', 15))
label.grid(row = 0, column = 0, sticky = 'n')

final_result = str()
result = tk.Label(frame, text = final_result, font = ('Rockwell', 13))
result.grid(row = 1, column = 1, sticky = 'w')

# inputs
ipt = tk.Entry(frame, font = ('Rockwell', 14))
ipt.grid(row = 0, column = 1, padx = 2)

# botão
btn = tk.Button(frame, text = 'CALCULATE', command = calc_factorial)
btn.grid(row = 2, column = 1, sticky = 'w')

root.mainloop()