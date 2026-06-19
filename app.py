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
        return redirect("/login")
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

@app.route("/produto/<codigo>", methods=["GET"])
def ret_produto(codigo):
    produto = buscar_produto(codigo)

    if not produto:
        return "Produto não encontrado"  

    lista_comentarios = visualizar_comentarios()
    logado = "usuario_logado" in session
    return render_template("produtos.html", produto=produto, comentarios=lista_comentarios, logado=logado)

@app.route("/comentarios/comentar", methods=["POST"])
def comentar():
 
    codigo_produto = request.form.get("codigo_produto")
    comentario = request.form.get("comentario")

    usuario = session.get("usuario_logado", {})
    codigo_usuario = usuario.get("codigo_usuario") or usuario.get("id") or 1

 
    try:
        adicionar_comentarios(codigo_usuario, comentario, codigo_produto)
    except:
        pass 
        
    return redirect("/") 
    

if __name__ == "__main__":
    app.run(debug=True)



