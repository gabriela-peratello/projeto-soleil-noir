from flask import Flask, jsonify, render_template, request, redirect


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


if __name__ == "__main__":
    app.run(debug=True)



