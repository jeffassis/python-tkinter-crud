from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
from PIL import Image, ImageTk

#nomes que vc quer no menu escolha
listSexo=["Masculino","Feminino"]

#CONFIGURACÃO JANELA
root = Tk()
root.geometry("900x600+200+50")
#root.iconbitmap("assets/crud.ico")
root.title('Teste de CRUD')
#FRAME TELA PRINCIPAL
tela_principal = Frame(root, bg="#353535")
tela_principal.place(x=0, y=0, width=900, height=600)

#TITULO
texto = Label(tela_principal, text="Teste de CRUD", font=("Arial Black",25), bg="#353535", fg="white")
texto.place(x=299, y=20)

texto_admin = Label(tela_principal, text="Administrador", font=("Arial Black",22),bg="#353535", fg="white")
texto_admin.place(x=29, y=95)

#CRIA IMAGEM ADMIN-CRUD
im_admin_crud = Image.open('assets/admin_crud.png')
im_admin_crud = im_admin_crud.resize((60,60), Image.ANTIALIAS)
im_admin_crud = ImageTk.PhotoImage(im_admin_crud)
#CARREGA IMAGEM ADMIN-CRUD
l_admin_crud= Label(tela_principal, image=im_admin_crud, compound=LEFT, anchor='nw', bg="#353535",bd=0,activebackground="#3b3b3b")
l_admin_crud.place(x=261,y=95)

#TEXTOS
#RG
rg = Label(tela_principal, text="RG", font =('Arial Black', 12), bg="#353535",fg="white")
rg.place(x=20,y=176)
#NOME
name = Label(tela_principal, text="Nome", font =('Arial Black', 12), bg="#353535",fg="white")
name.place(x=20,y=216)
#TELEFONE
phone = Label(tela_principal, text="Telefone", font =('Arial Black', 12), bg="#353535",fg="white")
phone.place(x=20,y=256)
#SEXO
nomesexo1 = Label(tela_principal, text="Sexo", font =('Arial Black', 12), bg="#353535",fg="white")
nomesexo1.place(x=20,y=296)

#CAMPOS CRUD
#RG
e_rg = Entry(tela_principal, width=23,font=1)
e_rg.place(x=120, y=180)
#NOME
e_name = Entry(tela_principal, width=23,font=1)
e_name.place(x=120, y=220)
#TELEFONE
e_phone = Entry(tela_principal, width=23, font=1)
e_phone.place(x=120, y=260)
#ESCOLHA SEXO
lb_sexo = ttk.Combobox(tela_principal, values=listSexo, font=1)
lb_sexo.place(x=120,y=300, width=180)

root.mainloop()