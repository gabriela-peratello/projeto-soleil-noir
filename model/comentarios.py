from database.conexao import conectar

def adicionar_comentarios(codigo_usuario, comentario:str):
    try:
        conexao, cursor = conectar()
        cursor.execute(
            """
            INSERT INTO comentarios(codigo_usuario, comentario)
            VALUES (%s, %s)

    """, (codigo_usuario, comentario)
        )

        conexao.commit()
        conexao.close()

        return True

    except Exception as erro:
        print(erro)
        return False
 
    
    

def visualizar_comentarios():
        conexao, cursor = conectar()
        cursor.execute(
            """
            SELECT usuarios.nome_completo, comentarios.comentario from comentarios
            INNER JOIN usuarios on usuarios.nome_completo = usuarios.nome_completo

    """
        )
        
        requisitos = cursor.fetchall()


        conexao.close()
        return requisitos
    
   
