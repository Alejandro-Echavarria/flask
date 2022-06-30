from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "estoesunallavesecreta"

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return "Login page2"

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/dinamic", methods=['GET', 'POST'])
def dinamic():
    if request.method == "POST":

        urls = {}

        if os.path.exists("urls.json"):
            with open("urls.json") as url_file:
                urls = json.load(url_file)

        if request.form["name"] in urls.keys():
            flash('Esa clave (o nombre) ya está cargada')
            return redirect(url_for("form"))

        if "url" in request.form.keys():
            
            urls = {request.form['name']: request.form['url']}
        else:
            file = request.files["file"]
            full_name_file = request.form["name"] + secure_filename(file.filename)
            file.save("static/uploads/" + full_name_file)
            urls[request.form["name"]] = {"file": full_name_file} 


        with open("urls.json", "w") as url_file:
            json.dump(urls, url_file)
            flash("El archivo se ha guardado correctamente", "success")

        return render_template("dinamic.html", name=request.form["name"])
    else:
        return redirect(url_for('home'))

@app.route("/img/<string:name>")
def redirect_to(name):
    if os.path.exists("urls.json"):
        with open("urls.json") as url_file:
            urls = json.load(url_file)
            if name in urls.keys():
                return redirect(url_for("static", filename="uploads/" + urls[name]["file"]))