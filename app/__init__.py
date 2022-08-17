from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Note Store - Home", url=os.getenv("URL"))

@app.route("/CMPE327")
def CMPE327():
    return render_template("CMPE327.html", title="Note Store - CMPE 327", 
                            url=os.getenv("URL"), name="CMPE 327 - Software Quality Assurance")