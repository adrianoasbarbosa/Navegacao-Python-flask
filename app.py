from flask import Flask, render_template

app = Flask(__name__)

#Rota para a página inicial (Index)

@app.route('/')
def index():
    return render_template('index.html')

#Rota para a página sobre (Sobre)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

#Rota para a página contato (Contato)

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)