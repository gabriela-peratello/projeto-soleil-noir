from flask import Flask, jsonify, render_template, request, redirect, session

from model.usuarios import cadastrar_usuario
from model.comentarios import adicionar_comentarios
from model.comentarios import visualizar_comentarios

from model.usuarios import logar_usuario
from model.produtos import visualizar_produtos, buscar_produto


app = Flask(__name__)
app.secret_key = "nossomosincriveiskisskisskiss"

@app.route("/")
def index():
    produtos = visualizar_produtos()
    return render_template("index.html", produtos = produtos)




# ROTA PÁGINA PRODUTO
@app.route("/produto")
def pag_produto():
    produtos = visualizar_produtos()
    return render_template("index.html", produtos=produtos)



# ROTA PÁGINA DE LOGIN
@app.route("/login")
def pag_login():
    return render_template("login.html")

@app.route("/logar", methods=["POST"])
def pag_log_usuario():
    email = request.form.get("usuario")
    senha = request.form.get("senha")
    resultado = logar_usuario(email, senha)
    if resultado:
        print("usuario logado")
        session["usuario_logado"] = resultado
        return redirect("/")
    
    else:
        return redirect("/cadastrar")
    

# ROTA PÁGINA DE CADASTRO
@app.route("/cadastrar")
def pag_cadastrar():
    return render_template("cadastrar.html")

@app.route("/cadastrar/post", methods = ["POST"])
def pag_cadastr_usuario():
    nome_completo = request.form.get("nome")
    email = request.form.get("usuario")
    telefone = request.form.get("telefone")
    endereco = request.form.get("endereco")
    senha = request.form.get("senha")
    if cadastrar_usuario(nome_completo, email, telefone, endereco, senha):
        return redirect("/")
    else:
        return "Erro ao cadastrar!!"



# ROTA PÁGINA PRODUTO
@app.route("/produto")
def pag_produto():
    # Busca os produtos e os comentarios do banco
    lista_produtos = visualizar_produtos()
    lista_comentarios = visualizar_comentarios()
    # verifica se ta logado
    logado = "usuario_logado" in session
    return render_template("produtos.html", produtos=lista_produtos, comentarios=lista_comentarios, logado=logado)

@app.route("/produto/<codigo>")
def ret_produto(codigo):
    # 1. Usa o código capturado para buscar APENAS o produto clicado
    produto_escolhido = buscar_produto(codigo)
    
    # 2. Busca todos os comentários normalmente
    lista_comentarios = visualizar_comentarios()
    
    # 3. Verifica o status de login
    logado = "usuario_logado" in session
    
    # Entrega o produto específico para a página produtos.html
    return render_template(
        "produtos.html", 
        produto=produto_escolhido, 
        comentarios=lista_comentarios, 
        logado=logado
    )





@app.route("/comentarios/comentar", methods=["POST"])
def comentar():
    # verifica se ta logado
    if "usuario_logado" not in session:
        return redirect("/login")
    
    usuario = session["usuario_logado"]
    codigo_usuario = usuario.get("codigo_usuario") or usuario.get("id") 
    nome_completo = usuario.get("nome_completo") or usuario.get("nome")
    
    comentario = request.form.get('comentario')
    
    if adicionar_comentarios(codigo_usuario, nome_completo, comentario):
        return redirect("/produto")
    else:
        return "Algum campo está em branco"
    



    
 



    

if __name__ == "__main__":
    app.run(debug=True)



