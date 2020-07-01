from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def index():
    headline="Bem vindo"
    return render_template("indexin.html",headline=headline)
@app.route("/tchau")
def valeu():
    headline="Valeu,Bro"
    return render_template("indexin.html",headline=headline)
    
