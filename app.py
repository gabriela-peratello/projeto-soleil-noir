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
    return render_template("index.html")




# ROTA PÁGINA PRODUTO
@app.route("/produto")
def pag_produto():
    produtos = visualizar_produtos()
    return render_template("produtos.html", produtos = produtos)

@app.route("/produto/<codigo>")
def rec_produtos(codigo):
    produto = buscar_produto(codigo)
    return render_template("produto.html", produto = produto)



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
    

@app.route("/comentario")
def visualizar_comen():
    comentario = visualizar_comentarios()
    return render_template("produtos.html", comentario = comentario)

@app.route("/comentarios/comentar", methods=["POST"])
def comentar():
    nome_completo = request.form.get("nome")
    codigo_usuario = request.form.get("codigo")
    comentario = request.form.get("comentario")
    if adicionar_comentarios(nome_completo, codigo_usuario, comentario) == True:
        return redirect("/produto")
    else:
        return "Algum campo está em branco"




    

if __name__ == "__main__":
    app.run(debug=True)



