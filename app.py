from flask import Flask, render_template

app = Flask(__name__)

#Rota para a página inicial (Index)

@app.route('/')
def index():
    return render_template('index.html')

#Rota para a página quem somos (Quem Somos)

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

#Rota para a página localizao (Localização)

@app.route('/localizacao')
def localizacao():
    return render_template('localizacao.html')

if __name__ == '__main__':
    app.run(debug=True)