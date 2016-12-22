from flask import render_template

from logic_circuit import app

@app.route("/")
def homepage():
    return app.send_static_file("homepage.html")

