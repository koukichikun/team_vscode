from flask import Flask,render_template,request,redirect,session,url_for
import string
import os

app=Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

@app.route("/en")
def en():
    return render_template("en.html")

@app.route("/kekka",methods=['POST'])
def kekka():
    hankei=request.form.get("hankei")
    ensyu=hankei*2*3.14
    menseki=hankei*hankei*3.14
    return render_template("kekka.html",menseki=menseki,ensyu=ensyu)

@app.route("/a")
def top2():
    return render_template("kyuyo.html")   

@app.route("/b")
def kekka2():
    kane=request.form.get("kane")
    roudou=request.form.get("roudou")

    okane = kane*roudou

    return render_template("kekka2.html",okane=okane)


if __name__=="__main__":
    app.run(debug=True)