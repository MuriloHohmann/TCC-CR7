from flask import Flask, render_template

app = Flask(__name__)

# Rota principal (Tela de Login)
@app.route("/")
def login():
    return render_template("login.html")

# Rota quando clicar em "Login"
@app.route("/home")
def home():
    return render_template("home.html") # Lembre-se de criar esse HTML em templates/

# Rota quando clicar em "Cadastrar"
@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html") # Lembre-se de criar esse HTML em templates/

if __name__ == "__main__":
    app.run(debug=True)