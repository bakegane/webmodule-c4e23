from flask import Flask, render_template
app = Flask(__name__)
@app.route("/user/<username>")
def files(username):
    users_list = {
        "ted" : {
            "name" : "Teddy",
            "age" : 20,
        },
        "todd" : {
            "name" : "Toddy",
            "age" : 25,
        },
        "tess" : {
            "name" : "Tessy",
            "age" : 22,
        },
        "taz" : {
            "name" : "Tazzy",
            "age" : 21,
        },
    }

    if username in users_list:
        return render_template("hoso.html",files = users_list[username])
    else:
        return "user not found"
if __name__ == "__main__":
    app.run(debug=True)