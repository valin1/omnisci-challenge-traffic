from flask import Flask
from flask import request
from flask import redirect, render_template, session, abort

app = Flask(__name__)
@app.route("/")
def index():
    return "Flask App!"

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
        'test.html',name=name)

@app.route("/members")
def members():
	return "Members"

if __name__ == "__main__":
	app.run()