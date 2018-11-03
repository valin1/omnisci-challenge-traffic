from flask import Flask
from flask import request
from flask import redirect, render_template, session, abort
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
@app.route("/")
def index():
    return render_template(
        'index.html')

@app.route("/hello/")
def hello():
    return render_template(
        'bootstrap/base.html')

@app.route("/members")
def members():
	return "Members"

if __name__ == "__main__":
	app.run()