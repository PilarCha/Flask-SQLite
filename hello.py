from flask import Flask, render_template, request
import sqlite3
import os
# this will store the directory of this specific file in a variable
currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
# reloads templates on every change
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/", methods = ["POST"])
def phonebook():
    name = request.form["Name"]
    phonenumber = request.form["Phonenumber"]
    connection = sqlite3.connect(currentdirectory + "\phonebook.db")
    cursor = connection.cursor()
