import os
from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

letters = []
for num in range(97,123):
	letters.append(chr(num))

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/learn")
def learn():
	return render_template("learn.html",letters=letters)

@app.route("/convert")
def convert():
	col = []
	odd = False
	for _ in range(26):
		if(odd):
			col.append("#212121")
			odd = False
		else:
			col.append("#4f4f4f")
			odd = True
	return render_template("convert.html",letters=letters, col=col)

@app.route("/calculate")
def calculate():
	return render_template("calculate.html",letters=letters)