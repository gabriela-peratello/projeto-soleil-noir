from database.conexao import conectar

def visualizar_produtos():
    conexao, cursor = conectar()
    cursor.execute("""
                    SELECT produto, descr, preco, foto FROM produtos;
                    """)
    produtos = cursor.fetchall()
    conexao.close()
    return produtos