import sqlite3 as lite

#CRIANDO CONEXÂO
con = lite.connect('dados.db')

def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO cadastro (rg, name, phone, sexo) VALUES (?, ?, ?, ?)"
        cur.execute(query, i)

# Acessar informações
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM cadastro"
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)
    return lista

def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM cadastro WHERE id=?"
        cur.execute(query, i)