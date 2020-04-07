from flask import Flask, render_template
from flask_ngrok import run_with_ngrok


app = Flask(__name__)
run_with_ngrok(app)

@app.route("/")
def home():
    return render_template("Osnova.html")


if __name__ == "__main__":
    app.run()
