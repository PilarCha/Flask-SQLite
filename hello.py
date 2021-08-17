from flask import Flask, render_template, request , g
import sqlite3
import os
# this will store the directory of this specific file in a variable
currentdirectory = os.path.dirname(os.path.abspath(__file__))

DATABASE = 'C:\sqlite\Phonebook.db'

app = Flask(__name__)

# reloads templates on every change
app.config['TEMPLATES_AUTO_RELOAD'] = True

# make sure you could connect to database check
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def main():
    return render_template("Main.html")

@app.route('/add_user', methods=["POST"])
def adduser():
    name = request.form["Name"]
    phonenumber = request.form["Phonenumber"]
    # open up the database connection
    cursor = get_db().cursor()
    query1 = "INSERT INTO Phonebook (Name,Phone) VALUES('{n}',{pnm})".format(n=name,pnm = phonenumber)
    print("the error can be found here " + query1)
    get_db().execute(query1)
    get_db().commit()


@app.route("/resultpage", methods = ["GET"])
def resultpage():
    try:
        if request.method == "GET":
            name = request.args.get("Name")
            connection = sqlite3.connect(currentdirectory + "\phonebook.db")
            cursor = connection.cursor()
            query1 = "Select Phonenumber from Phonebook WHERE Name ={n}".format(n=name)
            cursor.execute(query1)
            result = result.fetchall()[0][0]
            return render_template("Resultpage.html", Phonenumber = result)
    except:
        return render_template("Resultpage.html", Phonenumber = "")

if __name__ == '__main__':
    app.run(debug=True)
