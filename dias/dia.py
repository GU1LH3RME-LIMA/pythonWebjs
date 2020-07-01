import datetime
from flask import Flask, render_template
'''
    algoritmo simples para definir se o dia é par ou impar
'''
app = Flask(__name__)

@app.route("/")

def index():
    hoje=datetime.datetime.now()#objeto recebera a data atual
    return render_template("index.html",dia=hoje.day)
