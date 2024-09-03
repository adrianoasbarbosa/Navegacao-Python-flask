from flask import Flask, render_template

app = Flask(__name__)

#Rota para a página inicial (Index)

@app.route('/')
def index():
    return render_template('index.html')