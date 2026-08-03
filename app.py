from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "senaimeupinto"


conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="CR7GOAT"
)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route('/cadastroadm', methods=['POST'])
def cadastroadm():
    email = request.form['email']
    senha = request.form['senha']
    tipo = request.form['tipo']

    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO usuario(email, senha, tipo)
        VALUES (%s, %s, %s)
    """, (email, senha, tipo))
    
    conexao.commit()
    cursor.close()
    return redirect('/cadastroadm')


@app.route('/cadastro', methods=['POST'])
def cadastro():
    email = request.form['email']
    senha = request.form['senha']

    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO usuario(email, senha, tipo)
        VALUES (%s, %s, %s)
    """, (email, senha, "usuario"))
    
    conexao.commit()
    cursor.close()
    return redirect('/')  


@app.route('/login', methods=['POST'])
def hub():
    email = request.form['email']
    senha = request.form['senha']

    cursor = conexao.cursor()
    cursor.execute("""
        SELECT * FROM usuario WHERE email = %s
    """, (email,))
    
    usuario = cursor.fetchone()
    cursor.close()

    if usuario is None or usuario[2] != senha:
        return "Email ou senha incorretos"

    session['email'] = usuario[1]
    session['tipo'] = usuario[3]

    if usuario[3] == "admin":
        return redirect('/adm')

    return redirect('/home')


@app.route("/cadastro", methods=['GET'])
def cadastra():
    return render_template("cadastro.html")


@app.route("/movimentacoes")
def movimentacoes():
    return render_template("Movimentacoes.html")




@app.route("/estoque")
def estoque():
    cursor = conexao.cursor()
    cursor.execute("SELECT id, produto, categoria, quantidade FROM estoque")
    movimentacoes = cursor.fetchall()
    cursor.close()
    return render_template("Estoque.html", movimentacoes=movimentacoes)


@app.route('/deletar_item/<int:id>', methods=['POST'])
def deletar_item(id):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM estoque WHERE id = %s", (id,))
    conexao.commit()
    cursor.close()
    return redirect('/estoque')



@app.route("/adm")
def adm():
    return render_template("adm.html")

@app.route("/cadastroadm", methods=['GET'])
def cadastroadm_page():
    return render_template("cadastroadm.html")

@app.route("/estoqueadm")
def estoqueadm():
    return render_template("estoqueadm.html")


if __name__ == "__main__":
    app.run(debug=True)