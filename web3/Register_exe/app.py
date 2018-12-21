from flask import Flask, render_template, request
import mlab
from register import Register

mlab.connect()
app = Flask(__name__)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        form = request.form
        u = form["username"]
        p = form["password"]

        exist_user = Register.objects(username=u).first()
        if exist_user != None: #da co nguoi dung
            return "Unavailable"
        else:
            r = Register(username=u, password=p)
            r.save()
            return "verify your email"

if __name__ == "__main__":
    app.run(debug=True)