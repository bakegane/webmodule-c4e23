from flask import Flask, render_template, request
import mlab
from movie import Movie

mlab.connect()
app = Flask(__name__)

@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    if request.method == "GET": #user request form
        return render_template("add_movie.html")
    elif request.method == "POST": #user submit form
        form = request.form
        t = form["title"]
        i = form["image"]
        y = form["year"]
        m = Movie(title=t, image=i, year=y)
        m.save()
        return "Done!"


if __name__ == "__main__":
    app.run(debug=True)
