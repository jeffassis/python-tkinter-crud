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
im_admin_crud = Image.open('assets/admin.png')
im_admin_crud = im_admin_crud.resize((60,60), Image.Resampling.LANCZOS)
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

#BOTÕES DE FUNÇÕES CRUD
#CRIA IMAGEM INSERIR
im_ml_botao = Image.open('assets/bt_inserir.png')
im_ml_botao  = im_ml_botao.resize((60,30), Image.Resampling.LANCZOS)
im_ml_botao  = ImageTk.PhotoImage(im_ml_botao )
#CARREGA IMAGEM INSERIR - BOTAO INSERIR
l_ml_botao= Button(tela_principal, image=im_ml_botao, compound=LEFT, anchor='nw', 
bg="#3b3b3b",bd=0,activebackground="#3b3b3b")
l_ml_botao.place(x=20,y=349)
#CRIA IMAGEM DELETAR
im_ml_botao1 = Image.open('assets/bt_deletar.png')
im_ml_botao1  = im_ml_botao1.resize((60,30), Image.Resampling.LANCZOS)
im_ml_botao1  = ImageTk.PhotoImage(im_ml_botao1 )
#CARREGA IMAGEM DELETAR - BOTAO DELETAR
l_ml_botao1= Button(tela_principal, image=im_ml_botao1, compound=LEFT, anchor='nw', 
bg="#3b3b3b",bd=0,activebackground="#3b3b3b")
l_ml_botao1.place(x=100,y=349)
#CRIA IMAGEM EDITAR
im_ml_botao2 = Image.open('assets/bt_editar.png')
im_ml_botao2  = im_ml_botao2.resize((60,30), Image.Resampling.LANCZOS)
im_ml_botao2  = ImageTk.PhotoImage(im_ml_botao2 )
#CARREGA IMAGEM EDITAR - BOTAO EDITAR
l_ml_botao2= Button(tela_principal, image=im_ml_botao2, compound=LEFT, anchor='nw', 
bg="#3b3b3b",bd=0,activebackground="#3b3b3b")
l_ml_botao2.place(x=180,y=349)
#CRIA IMAGEM BUSCAR
im_ml_botao3 = Image.open('assets/bt_buscar.png')
im_ml_botao3  = im_ml_botao3.resize((60,30), Image.Resampling.LANCZOS)
im_ml_botao3  = ImageTk.PhotoImage(im_ml_botao3 )
#CARREGA IMAGEM BUSCAR - BOTAO BUSCAR
l_ml_botao3= Button(tela_principal, image=im_ml_botao3, compound=LEFT, anchor='nw', 
bg="#3b3b3b",bd=0,activebackground="#3b3b3b")
l_ml_botao3.place(x=260,y=349)

#PARTE PESQUISA E PAINEL DE DADOS
#CRIA IMAGEM Pesquisar
im_ml_pesquisa = Image.open('assets/pesquisab.png')
im_ml_pesquisa = im_ml_pesquisa.resize((30,30), Image.Resampling.LANCZOS)
im_ml_pesquisa = ImageTk.PhotoImage(im_ml_pesquisa)
#CARREGA IMAGEM Pesquisar
l_ml_pesquisa= Button(tela_principal, image=im_ml_pesquisa, compound=LEFT, anchor='nw', 
bg="#353535",bd=0,activebackground="#353535")
l_ml_pesquisa.place(x=460,y=95)
#PESQUISA
e_name1 = Entry(tela_principal, width=32,bd=0,bg="#353535",fg="white", insertbackground="white",font=1)
e_name1.place(x=510, y=95)
#SEPARADOR
ttk.Separator(tela_principal, orient=HORIZONTAL).place(x=510,y=120,  width=290)
#CRIA IMAGEM - LISTA
im_lista = Image.open('assets/lista.png')
im_lista = im_lista.resize((40,40), Image.Resampling.LANCZOS)
im_lista = ImageTk.PhotoImage(im_lista)
#CARREGA IMAGEM - LISTA
l_im_lista= Button(tela_principal, image=im_lista, compound=LEFT, anchor='nw', bg="#353535",bd=0,activebackground="#3b3b3b")

root.mainloop()