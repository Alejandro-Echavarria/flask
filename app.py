from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path

app = Flask(__name__)

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
            return redirect(url_for("form"))

        urls = {request.form['name']: request.form['url']}

        with open("urls.json", "w") as url_file:
            json.dump(urls, url_file)

        return render_template("dinamic.html", name=request.form["name"])
    else:
        return redirect(url_for('home'))