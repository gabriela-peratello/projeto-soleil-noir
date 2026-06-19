from database.conexao import conectar

def adicionar_comentarios(codigo_usuario, comentario: str, codigo_produto):
    try:
        conexao, cursor = conectar()
        # Adicionamos a coluna codigo_produto e o terceiro %s
        cursor.execute(
            """
            INSERT INTO comentarios (codigo_usuario, comentario, codigo_produto)
            VALUES (%s, %s, %s)
            """, 
            (codigo_usuario, comentario, codigo_produto) # Passando os 3 valores aqui
        )

        conexao.commit()
        conexao.close()

        return True

    except Exception as erro:
        print(f"Erro ao inserir comentário: {erro}")
        return False


def visualizar_comentarios():
    try:
        conexao, cursor = conectar()
        # Sua query com INNER JOIN está perfeita para buscar o nome do usuário!
        cursor.execute(
            """
            SELECT c.id_comentario, c.comentario, u.nome_completo 
            FROM comentarios c 
            INNER JOIN usuarios u ON c.codigo_usuario = u.codigo_usuario;
            """                             
        )        
        
        comentarios = cursor.fetchall()
        conexao.close()
        return comentarios
        
    except Exception as erro:
        print(f"Erro ao visualizar comentários: {erro}")
        return []