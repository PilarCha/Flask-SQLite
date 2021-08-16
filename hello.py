from flask import Flask, render_template, request
import sqlite3
import os
# this will store the directory of this specific file in a variable
currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/", method = ["POST"])
def phonebook():
    name = request.form["Name"]
    phonenumber = request.form["Phonenumber"]
    connection = sqlite3.connect(currentdirectory + "\phonebook.db")
    cursor = connection.cursor()

if __name__ == "__main__":
    app.run()
