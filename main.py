from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
from PIL import Image, ImageTk

#CONFIGURACÃO JANELA
root = Tk()
root.geometry("900x600+200+50")
#root.iconbitmap("")
root.title('Sistema de CRUD')
#FRAME TELA PRINCIPAL
tela_principal = Frame(root, bg="#353535")
tela_principal.place(x=0, y=0, width=900, height=600)

root.mainloop()