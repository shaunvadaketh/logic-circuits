from flask import render_template

from logic_circuit import app

@app.route("/")
def homepage():
    return render_template("index.html")

