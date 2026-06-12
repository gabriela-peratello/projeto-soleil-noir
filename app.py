from flask import Flask, jsonify, render_template, request, redirect

from model.usuarios import cadastrar_usuario

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")




# ROTA PÁGINA PRODUTO
@app.route("/produto")
def pag_produto():
    return render_template("produtos.html")



# ROTA PÁGINA DE LOGIN
@app.route("/login")
def pag_login():
    return render_template("login.html")


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
    

@app.route("/comentario", methods= ["POST"])
def comentar():
    pass

if __name__ == "__main__":
    app.run(debug=True)



