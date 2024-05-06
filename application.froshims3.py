from flask import Flask, redirect, render_template, request
import cvs

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("dorm"):
        return render_template("failure.html")
    file = open("registrants.cvs", "a")
    writer = cvs.writer(file)
    writer.writerow((request.form.get("name"), request.form.get("dorm")))
    file.close()
    return render_template("success.html")

# Thanks for looking
