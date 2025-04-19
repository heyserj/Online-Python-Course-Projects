from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from datetime import datetime

app = Flask(__name__)
Bootstrap5(app)

@app.context_processor
def inject_current_year():
    return {"current_year": datetime.now().year}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/athletics")
def athletics():
    return render_template("athletics.html")

@app.route("/academics")
def academics():
    return render_template("academics.html")

@app.route("/professional")
def professional():
    return render_template("professional.html")

if __name__ == "__main__":
    app.run(debug=True)