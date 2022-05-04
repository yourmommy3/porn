from flask import *
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
     return render_template("index.html");


@app.route("/Add")
def add():
    return render_template("Add.html")


@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
        #    with sqlite3.connect("emp.db") as con:
            con = sqlite3.connect("emp.db")
            cur = con.cursor()
            cur.execute("INSERT into EMP values (name, email) values (?,?)", (name, email))
            con.commit()
            msg = "Employee successfully Added"
        except:
            con.rollback()
            msg = "We can not add the employee to the list"
        finally:
            return render_template("Success.html", msg=msg)
            con.close()


@app.route("/View")
def view():
    con = sqlite3.connect("emp.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from EMP")
    rows = cur.fetchall()
    return render_template("View.html", rows=rows)


@app.route("/Delete")
def delete():
    return render_template("Delete.html")


@app.route("/delete_record", methods=["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("emp.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from EMP where id = ?", id)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html", msg=msg)


if __name__ == "__main__":
    app.run(debug=True)

