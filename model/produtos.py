from database.conexao import conectar

def visualizar_produtos():
    conexao, cursor = conectar()
    cursor.execute("""
                    SELECT produto, descr, preco, foto FROM produtos;
                    """)
    produtos = cursor.fetchall()
    conexao.close()
    return produtos


def buscar_produto(codigo):
    
    conexao, cursor = conectar()
    cursor.execute("""
                    SELECT produto, descr, preco, foto FROM produtos WHERE codigo = %s;
                    """, [codigo])
    produto = cursor.fetchone() 
    conexao.close()
    return produto
