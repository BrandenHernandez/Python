# Flask to route web requests to html pages

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/branden")
def branden():
    return render_template("branden.html")
   
# Thanks for looking
