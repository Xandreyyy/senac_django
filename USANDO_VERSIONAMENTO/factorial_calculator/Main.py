import tkinter as tk
from Factorial import Factorial

root = tk.Tk()
root.geometry('300x300')
root.resizable(False, False)
root.title('FACTORIAL CALCULATOR 3000')

frame = tk.Frame(root)

# labels
label = tk.Label(root, text = 'Enter a number:')
label.grid(row = 0, column = 0, sticky = 'n')

final_result = str()
result = tk.Label(frame, text = final_result)
result.grid(row = 1, column = 1)

# inputs
ipt = tk.Entry(frame)
result.grid(row = 0, column = 1)

# botão
btn = tk.Button(frame, text = 'CALCULATE')
result.grid(row = 2, column = 1)

frame.grid(row = 0, column = 1)
root.mainloop()