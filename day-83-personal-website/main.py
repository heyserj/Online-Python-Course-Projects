from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from datetime import datetime

app = Flask(__name__)
Bootstrap5(app)

@app.route("/")
def home():
    current_year = datetime.now().year
    return render_template("index.html", current_year=current_year)

if __name__ == "__main__":
    app.run(debug=True)