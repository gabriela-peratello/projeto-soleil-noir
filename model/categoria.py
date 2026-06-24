from database.conexao import conectar

def recuperar_categorias():
    conexao, cursor = conectar()
    cursor.execute("""
                SELECT id_categoria, nome_categoria FROM categorias

""")

    categorias = cursor.fetchall()
    conexao.close()
    return categorias


def recuperar_categorias_id(id_categoria):
    conexao, cursor = conectar()
    cursor.execute("""
            SELECT id_categoria, nome_categoria FROM categorias WHERE id_categoria = %s

""", [id_categoria])
    
    categoria = cursor.fetchone()
    conexao.close()

    return categoria