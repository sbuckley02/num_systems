import os
from flask import Flask, render_template, request, session
from flask_session import Session

#configure application
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

#create a list of lowercase letters
letters = []
for num in range(97,123):
	letters.append(chr(num))

#disable browser caches
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

#use the local file system
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#the main page
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/learn")
def learn():
	return render_template("learn.html",letters=letters)

@app.route("/convert")
def convert():
	#create a list of alternating colors for the character table rows
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