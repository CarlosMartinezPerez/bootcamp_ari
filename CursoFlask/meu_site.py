from flask import Flask, render_template

app = Flask(__name__)
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario = nome_usuario)

if __name__ == "__main__":
    app.run(debug=True)

"""
Para comocar o site no ar ou fazer alterações:
pasta do projeto> heroku login
pasta do projeto> heroku git:remote -a vaitimao
pasta do projeto> git add .
pasta do projeto> git commit -am "deploy inicial 180723"
pasta do projeto> git push heroku master

Endereço do site:
https://vaitimao-5e0e3cd23a82.herokuapp.com/
"""
