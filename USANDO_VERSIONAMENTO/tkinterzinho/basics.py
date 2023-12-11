import tkinter as tk
# widgets -> tkinter se baseia em widgets, que são objetos instanciados (Label, Text, Entry, Button...)

#  n (north)                                  x, y -> representa a POSIÇÃO do elemento
# w e (west & east) -> oeste e leste          width, height -> representam o TAMANHO do elemento
#  s (south)

root = tk.Tk()
root.geometry("400x400")
root.title("Hello Viamão!")

label = tk.Label(root, text="Pequeno texto", font=("Arial", 12))
label.pack(anchor="center", pady=10)

# hight é definido pela quantidade de linhas
txtarea = tk.Text(root, height=2, font=("sans", 14))
txtarea.pack()

my_input = tk.Entry(root, font=("Times New Roman", 12))
my_input.pack(anchor="w", pady=5)

btn_frame = tk.Frame(root)
btn_frame.columnconfigure(0, weight=1)
btn_frame.columnconfigure(1, weight=1)
btn_frame.columnconfigure(2, weight=1)

btn1 = tk.Button(btn_frame, text="1")
btn1.grid(row=0, column=0, sticky="we")

btn2 = tk.Button(btn_frame, text="2")
btn2.grid(row=0, column=1, sticky="we")

btn3 = tk.Button(btn_frame, text="3")
btn3.grid(row=0, column=2, sticky="we")

btn4 = tk.Button(btn_frame, text="4")
btn4.grid(row=1, column=0, sticky="we")

btn5 = tk.Button(btn_frame, text="5")
btn5.grid(row=1, column=1, sticky="we")

btn6 = tk.Button(btn_frame, text="6")
btn6.grid(row=1, column=2, sticky="we")

btn_frame.pack(fill="both")

button = tk.Button(root, text="ENVIAR", font=("sans-serif", 12), border=1, background="green", activebackground="lime", fg="white")
button.pack(anchor="w")

button = tk.Button(root, text="❤️", border=1, width=3)
# colocar widgets manualmente
button.place(x=190, y=350)

root.mainloop()