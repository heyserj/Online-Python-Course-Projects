from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from datetime import datetime

app = Flask(__name__)
Bootstrap5(app)

@app.route("/")
def home():
    current_year = datetime.now().year
    return render_template("index.html", current_year=current_year)

@app.route("/athletics")
def athletics():
    current_year = datetime.now().year
    return render_template("athletics.html", current_year=current_year)

@app.route("/academics")
def academics():
    current_year = datetime.now().year
    return render_template("academics.html", current_year=current_year)

@app.route("/professional")
def professional():
    current_year = datetime.now().year
    return render_template("professional.html", current_year=current_year)

@app.route("/contact")
def contact():
    current_year = datetime.now().year
    return render_template("contact.html", current_year=current_year)

if __name__ == "__main__":
    app.run(debug=True)