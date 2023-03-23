# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Daniel" 
    idade = "14" 

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def home1():

    nome = "Pedro" 
    idade = "36" 

    return render_template('pai.html' , nome = nome , idade = idade)

# defina a rota para a página da mãe
@app.route("/mãe")
def home2():

    nome = "Erika" 
    idade = "36" 

    return render_template('mae.html' , nome = nome , idade = idade)


# defina a rota para a página do amigo
@app.route("/amigo")
def home3():

    nome = "Vinicius" 
    idade = "15" 

    return render_template('amigo.html' , nome = nome , idade = idade)


# adicione outras rotas, se você quiser
@app.route("/irmão")
def home4():

    nome = "Gustavo" 
    idade = "13" 

    return render_template('index.html' , nome = nome , idade = idade)


# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
