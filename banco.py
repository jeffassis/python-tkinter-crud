import sqlite3 as lite

#CRIANDO CONEXÂO
con = lite.connect('dados.db')

# Inseri informações
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

# Deletar informações
def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM cadastro WHERE id=?"
        cur.execute(query, i)

# Atualizar informações
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE cadastro SET rg=?, name=?, phone=?, sexo=? WHERE id=?"
        cur.execute(query, i)

# Pesquisa informações na tabela
def consulta_info(param):
    with con:
        cur = con.cursor()
        query = (f"SELECT * FROM cadastro WHERE name like '%{param}%'")
        cur.execute(query)
        rows = cur.fetchall()
    return rows


def pesquisa_info_nome(param):
    with con:
        cur = con.cursor()
    find_name = ('SELECT * FROM cadastro WHERE name = ?')
    cur.execute(find_name,[(param)])
    result = cur.fetchall()
    return result
