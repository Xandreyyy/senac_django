import tkinter as tk

class TTT:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.title('Viamão Velha')

        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.grid(column=0, row=0)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.btn1 = tk.Button(self.btn_frame, text=" ", width=12, height=8).grid(column=0, row=0)
        self.btn2 = tk.Button(self.btn_frame, text=" ", width=12, height=8).grid(column=1, row=0)
        self.btn3 = tk.Button(self.btn_frame, text=" ", width=12, height=8).grid(column=2, row=0)

        self.btn4 = tk.Button(self.btn_frame, text=" ", width=12, height=8).grid(column=0, row=1)
        self.btn5 = tk.Button(self.btn_frame, text=" ", width=12, height=8).grid(column=1, row=1)
        self.btn6 = tk.Button(self.btn_frame, text=" ", width=12, height=8).grid(column=2, row=1)

        self.btn7 = tk.Button(self.btn_frame, text=" ", width=12, height=8).grid(column=0, row=2)
        self.btn8 = tk.Button(self.btn_frame, text=" ", width=12, height=8).grid(column=1, row=2)
        self.btn9 = tk.Button(self.btn_frame, text=" ", width=12, height=8).grid(column=2, row=2)

        self.root.mainloop()

TTT()