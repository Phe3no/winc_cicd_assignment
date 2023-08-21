# Import what we need from flask
from flask import Flask, render_template

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested


@app.route('/')
def index():
    return render_template("public/index.html")


@app.route('/calculations')
def calculations():
    return render_template("public/calculations.html")


if __name__ == "__main__":
    app.run()
