from flask import Flask, render_template, request , url_for
import sqlite3
import os
# this will store the directory of this specific file in a variable
currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.run(debug=True)

# reloads templates on every change
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def main():
    return render_template("Main.html")


@app.route("/add_user", methods=["POST"])
def adduser():
    name = request.form["Name"]
    phonenumber = request.form["Phonenumber"]
    connection = sqlite3.connect(currentdirectory + "\phonebook.db")
    cursor = connection.cursor()
    query1 = "INSERT INTO Phonebook VALUES({n},{pnm}).format(n=name,pnm = phonenumber)"
    cursor.execute(query1)
    connection.commit()

@app.route("/resultpage", methods = ["GET"])
def resultpage():
    try:
        if request.method == "GET":
            name = request.args.get("Name")
            connection = sqlite3.connect(currentdirectory + "\phonebook.db")
            cursor = connection.cursor()
            query1 = "Select Phonenumber from Phonebook WHERE Name = {n}".format(n=name)
            cursor.execute(query1)
            result = result.fetchall()[0][0]
            return render_template("Resultpage.html", Phonenumber = result)
    except:
        return render_template("Resultpage.html", Phonenumber = "")
