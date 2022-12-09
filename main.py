from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
from PIL import Image, ImageTk
from banco import*

# OPÇÕES COMBOBOX
listSexo=["Masculino","Feminino"]

#INSERIR
#------------
def insert():
    try:
        # VERIFICA SE O NOME JA FOI INSERIDO
        param = e_name.get()
        result = pesquisa_info_nome(param)
        if result:
            MessageBox.showerror("Error",'Inserir dados diferentes')
        else:
            rg = e_rg.get()
            name = e_name.get()
            phone = e_phone.get()
            sexo = lb_sexo.get()

            lista = [rg, name, phone, sexo]

            #VERIFICA SE TEM CAMPO VAZIO
            if(rg == "" or name == "" or phone == "" or sexo == ""):
                MessageBox.showinfo("Erro", "Todos os campos são obrigatórios")
            else:
                inserir_info(lista) 
                #APÓS CONFIRMAR, APAGA AS LINHAS
                e_rg.delete(0, 'end')
                e_name.delete(0, 'end')
                e_phone.delete(0, 'end')
                lb_sexo.delete(0, 'end')
                MessageBox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
                show()
    except Exception as es:
                MessageBox.showerror("Error", f"Error Due to: {str(es)}", parent=tela_principal)

#DELETAR
#------------
def delete():
    try:
        tv_dados = tv.focus()
        tv_dicionario = tv.item(tv_dados)
        tv_lista = tv_dicionario['values']
        valor_id = [tv_lista[0]]
        #ESTRUTURA DE DECISÃO EM JANELA PARA CONFIRMAR A REMOÇÃO DE DADOS
        result = MessageBox.askquestion('Remover dados?', 'Tem certeza que deseja remover dados?')
        if result == 'yes':        
            deletar_info(valor_id)
            MessageBox.showinfo('Sucesso', 'Os dados foram removidos com sucesso')       
        show()
    except IndexError:
        MessageBox.showerror('Erro', 'Selecione um registro na tabela')

#ATUALIZAR
#------------
def update():
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
           #VERIFICA SE OS CAMPOS ESTÃO VAZIOS
           if(rg == "" or name == "" or phone == "" or sexo == ""):
                MessageBox.showinfo("Erro", "Todos os campos são obrigatórios")
           else:
                atualizar_info(lista)
                MessageBox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

                e_rg.delete(0, 'end')
                e_name.delete(0, 'end')
                e_phone.delete(0, 'end')
                lb_sexo.delete(0, 'end')
           bt_confirmar.place_forget()
           show()
        #CARREGA IMAGEM CONFIRMAR - BOTAO CONFIRMAR
        bt_confirmar= Button(tela_principal, image=img_confirmar, compound=LEFT, anchor='nw', 
        bg="#3b3b3b",bd=0,activebackground="#3b3b3b", command=atualiza)
        bt_confirmar.place(x=260,y=349)
    except IndexError:
        MessageBox.showerror('Erro', 'Selecione um registro na tabela')

def consulta(event=None):
    like = e_name1.get()
    if(like == ""):
        MessageBox.showinfo("Status", "Campo Obrigatório")
    else:
        param = e_name1.get().strip()
        rows = consulta_info(param)
        #DELETA TODOS OS DADOS PARA NÂO DUPLICAR
        tv.delete(*tv.get_children())
        for row in rows:
            tv.insert("", "end", values=row)       
        bt_lista.place(x=380, y=100)

#CONFIGURACÃO JANELA
root = Tk()
root.geometry("900x430+200+50")
root.title('Teste de CRUD')

#FRAME TELA PRINCIPAL
tela_principal = Frame(root, bg="#353535")
tela_principal.place(x=0, y=0, width=900, height=430)

#TITULO
texto = Label(tela_principal, text="Teste de CRUD", font=("Arial Black",25), bg="#353535", fg="white")
texto.place(x=299, y=20)

texto_admin = Label(tela_principal, text="Administrador", font=("Arial Black",22),bg="#353535", fg="white")
texto_admin.place(x=29, y=95)

#CRIA IMAGEM ADMIN-CRUD
img_admin = Image.open('assets/admin.png')
img_admin = img_admin.resize((60,60), Image.Resampling.LANCZOS)
img_admin = ImageTk.PhotoImage(img_admin)

#CARREGA IMAGEM ADMIN-CRUD
l_admin_crud= Label(tela_principal, image=img_admin, compound=LEFT, anchor='nw', bg="#353535",bd=0,activebackground="#3b3b3b")
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
img_inserir = Image.open('assets/bt_inserir.png')
img_inserir  = img_inserir.resize((60,30), Image.Resampling.LANCZOS)
img_inserir  = ImageTk.PhotoImage(img_inserir )
#CARREGA IMAGEM INSERIR - BOTAO INSERIR
bt_add= Button(tela_principal, command=insert,image=img_inserir, compound=LEFT, anchor='nw', 
bg="#3b3b3b",bd=0,activebackground="#3b3b3b")
bt_add.place(x=20,y=349)

#CRIA IMAGEM DELETAR
img_deletar = Image.open('assets/bt_deletar.png')
img_deletar  = img_deletar.resize((60,30), Image.Resampling.LANCZOS)
img_deletar  = ImageTk.PhotoImage(img_deletar )
#CARREGA IMAGEM DELETAR - BOTAO DELETAR
bt_delete= Button(tela_principal, command=delete,image=img_deletar, compound=LEFT, anchor='nw', 
bg="#3b3b3b",bd=0,activebackground="#3b3b3b")
bt_delete.place(x=100,y=349)

#CRIA IMAGEM EDITAR
img_editar = Image.open('assets/bt_editar.png')
img_editar  = img_editar.resize((60,30), Image.Resampling.LANCZOS)
img_editar  = ImageTk.PhotoImage(img_editar )
#CARREGA IMAGEM EDITAR - BOTAO EDITAR
bt_editar= Button(tela_principal, command=update, image=img_editar, compound=LEFT, anchor='nw', 
bg="#3b3b3b",bd=0,activebackground="#3b3b3b")
bt_editar.place(x=180,y=349)

#CRIA IMAGEM CONFIRMAR - BOTAO CONFIRMAR
img_confirmar = Image.open('assets/bt_confirmar.png')
img_confirmar  = img_confirmar.resize((60,30), Image.Resampling.LANCZOS)
img_confirmar  = ImageTk.PhotoImage(img_confirmar )

#PARTE PESQUISA E PAINEL DE DADOS
#CRIA IMAGEM Pesquisar
img_pesquisa = Image.open('assets/pesquisab.png')
img_pesquisa = img_pesquisa.resize((30,30), Image.Resampling.LANCZOS)
img_pesquisa = ImageTk.PhotoImage(img_pesquisa)
#CARREGA IMAGEM Pesquisar
bt_pesquisa= Button(tela_principal, image=img_pesquisa, compound=LEFT, anchor='nw', 
bg="#353535",bd=0,activebackground="#353535", command=consulta)
bt_pesquisa.place(x=460,y=95)

# CAMPO TEXTO PESQUISA
e_name1 = Entry(tela_principal, width=32,bd=0,bg="#353535",fg="white", insertbackground="white",font=1)
e_name1.place(x=510, y=95)

#SEPARADOR
ttk.Separator(tela_principal, orient=HORIZONTAL).place(x=510,y=120,  width=290)

#LINHA
ttk.Separator(tela_principal, orient=HORIZONTAL).place(x=100,y=405,  width=700)

# MOSTRA DADOS NA TABELA
def show():
   global tv
   bt_lista.place_forget()
   lista = mostrar_info()
   tabela_head = ['id', 'rg', 'nome', 'telefone', 'sexo']
   tv = ttk.Treeview(tela_principal, columns=tabela_head, show='headings')
   tv.place(x=380, y=150)
   #COLUNA
   hd = ["nw", "nw", "nw", "center", "center"]
   h = [50, 100, 150, 100, 100]
   n = 0
   for col in tabela_head:
    tv.heading(col, text=col.title(), anchor=CENTER)
    tv.column(col, width=h[n], anchor=hd[n])
    n += 1
   for item in lista:
        tv.insert("","end",values=item)

#CRIA IMAGEM - LISTA
img_lista = Image.open('assets/lista.png')
img_lista = img_lista.resize((40,40), Image.Resampling.LANCZOS)
img_lista = ImageTk.PhotoImage(img_lista)
#CARREGA IMAGEM - LISTA
bt_lista= Button(tela_principal, command=show, image=img_lista, compound=LEFT, anchor='nw', bg="#353535",bd=0,activebackground="#3b3b3b")

root.bind('<Return>', consulta)
show()
root.mainloop()