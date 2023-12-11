import tkinter as tk
from tkinter import messagebox

class GUI:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Usando classes no tkinter hehe")

        # widget master
        self.menubar = tk.Menu(self.root)

        # widget filho recebe o widget pai (widget master)
        self.menu_section1 = tk.Menu(self.menubar, tearoff=0) # menu pai
        self.menu_section1.add_command(label="Sair", command=self.sure_window) # add_command adiciona um menu filho
        self.menu_section1.add_separator()
        self.menu_section1.add_command(label="Me tira daqui", command=exit)

        self.menu_section2 = tk.Menu(self.menubar, tearoff=0) # outro menu pai
        self.menu_section2.add_command(label="Mostrar mensagem", command=self.show_msg)
        
        # widget master vai receber os menus pais
        self.menubar.add_cascade(menu=self.menu_section1, label="Sair")
        self.menubar.add_cascade(menu=self.menu_section2, label="Mostrar")

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Inserir mensagem: ", font=("Arial", 12))
        self.label.pack()

        self.txtarea = tk.Text(self.root, height=3, font=("sans", 10))
        self.txtarea.bind("<KeyPress>", self.shortcut)
        self.txtarea.pack()

        # vars: StringVar, IntVar, DoubleVar, BooleanVar
        self.is_checked = tk.BooleanVar()
        self.check = tk.Checkbutton(self.root, text="Check", font=("sans-serif", 12), variable=self.is_checked)
        self.check.pack()
        
        # widget pai           widget ⬇ mestre
        self.btn_frame = tk.Frame(self.root) 
        self.btn_frame.columnconfigure(0, weight=1)
        self.btn_frame.columnconfigure(1, weight=1)

        # 1º widget filho         widget pai ⬇
        self.show_btn = tk.Button(self.btn_frame, text="MOSTRAR MSG", command=self.show_msg)
        self.show_btn.grid(row=0, column=0)

        # 2º widget filho         widget pai ⬇
        self.clear_btn = tk.Button(self.btn_frame, text="LIMPAR", command=self.clear_txt)
        self.clear_btn.grid(row=0, column=1, padx=10)

        self.btn_frame.pack() # NÃO SE ESQUEÇA DE SEMPRE DAR PACK DO WIDGET PAI

        self.root.protocol("WM_DELETE_WINDOW", self.sure_window)
        self.root.mainloop()

    def show_msg(self):
        # get sem parâmetro retorna o valor da var // "1.0" -> início & "tk.END" -> até o final do conteúdo
        if self.is_checked.get() == True and self.txtarea.get("1.0", tk.END) != '\n': 
            messagebox.showwarning(title="PARABÉNS", message=f'Você digitou: {self.txtarea.get("1.0", tk.END)}')
        elif self.txtarea.get("1.0", tk.END) == '\n':
            messagebox.showerror(title="ERRO", message="Você precisa digitar alguma coisa!")
        else:
            messagebox.showerror(title="ERRO", message="Você precisa clicar na checkbox!")

    def shortcut(self, event):
        if event.state == 12:
            self.show_msg()

    def sure_window(self):
        # askyesno retorna bool
        if messagebox.askyesno(title="SAIR", message="Você tem certeza que deseja sair?"):
            self.root.destroy()

    def clear_txt(self):
        self.txtarea.delete("1.0", tk.END)

GUI()