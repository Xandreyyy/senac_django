import tkinter as tk
# tkinter = toolkit interface
# https://tcl.tk/man/tcl8.6/TkCmd/contents.htm

# gera o frame
window = tk.Tk()
# informamos largura x altura do frame
window.geometry('300x300')
# título do frame
window.title('Meu app Py')
# gera um texto
label = tk.Label(text = 'Oi mãe')
# ???
label.grid(column = 2, row = 4)
# define a ancoragem no centro
label.pack(anchor = 'center')

# usado para mostrar na tela
window.mainloop()