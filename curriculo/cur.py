from flask import Flask, render_template, request, session
from flask_session.__init__ import Session

app= Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/",methods=["GET","POST"])
def curri():
    if session.get("linguagens") is None:
        session["linguagens"]=[]
    if request.method=="POST":
        lingua = request.form.get("lingua")
        session["linguagens"].append(lingua)
    return render_template("curri.html", linguagens=session["linguagens"])

@app.route("/prox",methods=["GET","POST"])           
def proxi():
    if session.get("habilidades") is None:
        session["habilidades"]=[]
    if request.method=="POST":
        hab = request.form.get("hab")
        session["habilidades"].append(hab)
        
    return render_template("prox.html",hab=session["habilidades"])
