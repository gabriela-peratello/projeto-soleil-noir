from database.conexao import conectar

# Model pra cadastro do usuário

def cadastrar_usuario(nome_completo:str, email:str, telefone:str, endereco:str, senha:str):
    try:
        conexao, cursor = conectar()
        cursor.execute(""" INSERT INTO usuarios(nome_completo, email, telefone, endereco, senha)
                       VALUES(%s, %s, %s, %s, %s)""", [nome_completo, email, telefone, endereco, senha])
        
        conexao.commit()
        conexao.close()

        return True
    
    except Exception as e:
        print(e)
        return False
    

#  Model pra login do usuário

def logar_usuario(email:str, senha:str):
    try:
        conexao, cursor = conectar()
        cursor.execute("""SELECT email, senha FROM usuarios 
                       WHERE email= %s and senha = %s""",
                       [email, senha])
        conexao.close()

    except Exception as e:
        print(e)
        return False
