from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
from PIL import Image, ImageTk
from banco import*

# Opções ComboBox
listSexo=["Masculino","Feminino"]

#FUNÇÕES

#INSERIR
#------------
def insert():
    rg = e_rg.get()
    name = e_name.get()
    phone = e_phone.get()
    sexo = lb_sexo.get()

    lista = [rg, name, phone, sexo]

    #verifica se tem algum campo vazio
    if(rg == "" or name == "" or phone == "" or sexo == ""):
        MessageBox.showinfo("Erro", "Todos os campos são obrigatórios")
    else:
        inserir_info(lista) 
        #Após confirmar, apaga as linhas
        e_rg.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        lb_sexo.delete(0, 'end')
        MessageBox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        show()

#DELETAR
#------------
def delete():
    try:
        tv_dados = tv.focus()
        tv_dicionario = tv.item(tv_dados)
        tv_lista = tv_dicionario['values']
        valor_id = [tv_lista[0]]

        result = MessageBox.askquestion('Remover dados?', 'Tem certeza que deseja remover dados?')
        if result == 'yes':        
            deletar_info(valor_id)
            MessageBox.showinfo('Sucesso', 'Os dados foram removidos com sucesso')       
        show()
    except IndexError:
        MessageBox.showerror('Erro', 'Seleciona um dos dados na tabela')

#ATUALIZAR
#------------
def update():
    bt_add.config(state='disabled')
    bt_delete.config(state='disabled')
    bt_editar.config(state='disabled')
    try:
        tv_dados = tv.focus()
        tv_dicionario = tv.item(tv_dados)
        tv_lista = tv_dicionario['values']

        valor_id = tv_lista[0]
        
        e_rg.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        lb_sexo.delete(0, 'end')

        e_rg.insert(0, tv_lista[1])
        e_name.insert(0, tv_lista[2])
        e_phone.insert(0, tv_lista[3])
        lb_sexo.insert(0, tv_lista[4])
        
        def atualiza():
           rg = e_rg.get()
           name = e_name.get()
           phone = e_phone.get()
           sexo = lb_sexo.get()

           lista = [rg, name, phone, sexo, valor_id]
           #verifica se tem algum campo vazio
           if(rg == "" or name == "" or phone == "" or sexo == ""):
                MessageBox.showinfo("Erro", "Todos os campos são obrigatórios")
           else:
                atualizar_info(lista)
                MessageBox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

                e_rg.delete(0, 'end')
                e_name.delete(0, 'end')
                e_phone.delete(0, 'end')
                lb_sexo.delete(0, 'end')
           b_confirma.destroy()
           bt_add.config(state='normal')
           bt_delete.config(state='normal')
           bt_editar.config(state='normal')
           show()
        #CRIA IMAGEM CONFIRMAR
        b_confirma = Button(tela_principal, command=atualiza, text='OK', width=4,
                             font=('Ivy 7'), bg='lightyellow',relief='raised', overrelief='ridge')
        b_confirma.place(x=193, y=355)
    except IndexError:
        MessageBox.showerror('Erro', 'Seleciona um dos dados na tabela')

#CONFIGURACÃO JANELA
root = Tk()
root.geometry("900x430+200+50")
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
bt_add= Button(tela_principal, command=insert,image=im_ml_botao, compound=LEFT, anchor='nw', 
bg="#3b3b3b",bd=0,activebackground="#3b3b3b")
bt_add.place(x=20,y=349)
#CRIA IMAGEM DELETAR
im_ml_botao1 = Image.open('assets/bt_deletar.png')
im_ml_botao1  = im_ml_botao1.resize((60,30), Image.Resampling.LANCZOS)
im_ml_botao1  = ImageTk.PhotoImage(im_ml_botao1 )
#CARREGA IMAGEM DELETAR - BOTAO DELETAR
bt_delete= Button(tela_principal, command=delete,image=im_ml_botao1, compound=LEFT, anchor='nw', 
bg="#3b3b3b",bd=0,activebackground="#3b3b3b")
bt_delete.place(x=100,y=349)
#CRIA IMAGEM EDITAR
im_ml_botao2 = Image.open('assets/bt_editar.png')
im_ml_botao2  = im_ml_botao2.resize((60,30), Image.Resampling.LANCZOS)
im_ml_botao2  = ImageTk.PhotoImage(im_ml_botao2 )
#CARREGA IMAGEM EDITAR - BOTAO EDITAR
bt_editar= Button(tela_principal, command=update, image=im_ml_botao2, compound=LEFT, anchor='nw', 
bg="#3b3b3b",bd=0,activebackground="#3b3b3b")
bt_editar.place(x=180,y=349)
#CRIA IMAGEM BUSCAR
im_ml_botao3 = Image.open('assets/bt_buscar.png')
im_ml_botao3  = im_ml_botao3.resize((60,30), Image.Resampling.LANCZOS)
im_ml_botao3  = ImageTk.PhotoImage(im_ml_botao3 )
#CARREGA IMAGEM BUSCAR - BOTAO BUSCAR
bt_buscar= Button(tela_principal, image=im_ml_botao3, compound=LEFT, anchor='nw', 
bg="#3b3b3b",bd=0,activebackground="#3b3b3b")
bt_buscar.place(x=260,y=349)

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

#linha
ttk.Separator(tela_principal, orient=HORIZONTAL).place(x=100,y=405,  width=700)

def show():
   global tv
   lista = mostrar_info()
   tabela_head = ['id', 'rg', 'nome', 'telefone', 'sexo']
   tv = ttk.Treeview(tela_principal, columns=tabela_head, show='headings')
   tv.place(x=380, y=150)
   #coluna
   hd = ["nw", "nw", "nw", "center", "center"]
   h = [50, 100, 150, 100, 100]
   n = 0
   for col in tabela_head:
    tv.heading(col, text=col.title(), anchor=CENTER)
    tv.column(col, width=h[n], anchor=hd[n])
    n += 1
   for item in lista:
        tv.insert("","end",values=item)

show()

root.mainloop()