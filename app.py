from flask import Flask, render_template , request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "senaimeupinto"

# Crie a conexão aqui para que o rest do arquivo a encontre:
conexao = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="", 
    database="CR7GOAT" 
)

# Rota principal (Tela de Login)
@app.route("/")
def login():
    return render_template("login.html")

# Rota quando clicar em "Login"
@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/cadastroadm', methods=['POST'])
def cadastraadm():

    email = request.form['email']
    senha = request.form['senha']
    tipo = request.form['tipo']

    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO usuario(email, senha, tipo)
        VALUES (%s,%s,%s)
        """,
        (email, senha, tipo)
    )

    conexao.commit()

    return redirect('/cadastroadm')


@app.route('/cadastro', methods=['POST'])
def cadastro():

    email = request.form['email']
    senha = request.form['senha']


    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO usuario(email, senha, tipo)
        VALUES (%s,%s,%s)
        """,
        (email, senha, "usuario")
    )

    conexao.commit()

    return render_template("/cadastro.html")

@app.route('/login', methods=['POST'])
def hub():

    email = request.form['email']
    senha = request.form['senha']

    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT * FROM usuario
        WHERE email=%s
        """,
        (email,)
    )

    usuario = cursor.fetchone()

    if usuario is None or usuario[2] != senha:
        return "Email ou senha incorretos"


    session['email'] = usuario[1]
    session['tipo'] = usuario[3] 

    if usuario[3] == "admin":
        return redirect('/adm')


    return render_template('home.html')


# Rota quando clicar em "Cadastrar"
@app.route("/cadastro")
def cadastra():
    return render_template("cadastro.html") # Lembre-se de criar esse HTML em templates/

# Rota para Histórico de Movimentações
@app.route("/movimentacoes")
def movimentacoes():
    return render_template("Movimentacoes.html")

# Rota para a Tela de Estoque
@app.route("/estoque")
def estoque():
    return render_template("Estoque.html")
@app.route("/adm")
def adm():
    return render_template("adm.html")
@app.route("/cadastroadm")
def cadastroadm():
    return render_template("cadastroadm.html")
@app.route("/estoqueadm")
def estoqueadm():
    return render_template("estoqueadm.html")




if __name__ == "__main__":
    app.run(debug=True)
