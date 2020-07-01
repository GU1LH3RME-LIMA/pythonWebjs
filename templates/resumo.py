from flask import Flask, render_template
'''
    um mini curriculo onde será mostrado as linguagens e habilidade
'''
app=Flask(__name__)

@app.route("/")

def index():
    linguagens=["Python","PHP","Java","HTML/CSS/JAVASCRIPT","C","C++","R","Ruby","MySQL"]
    return render_template("index.html",prog=linguagens)

@app.route("/prox")

def proxi():
    hab=["Algoritmo","CRUD","WEBDESIGN","Ponteiros","JavaFX","BackEnd"]
    return render_template("prox.html",hab=hab)

