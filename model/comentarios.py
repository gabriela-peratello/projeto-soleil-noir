from database.conexao import conectar

def adicionar_comentarios(codigo_usuario, nome_completo:str, comentario:str):
    try:
        conexao, cursor = conectar()
        cursor.execute(
            """
            INSERT INTO comentarios(codigo_usuario, nome_completo, comentario)
            VALUES (%s, %s, %s)

    """, (codigo_usuario, nome_completo, comentario)
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
            INNER JOIN usuarios ON comentarios.codigo_usuario = usuarios.codigo_usuario

    """                             
        )    
        
        comentarios = cursor.fetchall()


        conexao.close()
        return comentarios
    
   
