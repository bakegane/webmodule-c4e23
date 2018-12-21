from flask import Flask, request, render_template, session, redirect, url_for
app = Flask(__name__)
app.config["SECRET_KEY"] = "abcdef"
from models.user import User
from models.movie import Movie
import mlab

mlab.connect()

@app.route("/profile")
def profile():
    if "token" in session:
      username = session["token"]
      user = User.objects(username=username).first()
      movies = Movie.objects(user=user)
      # for m in movies:
      #   print(m.title)
      return render_template("profile.html", movie_list = movies)
    else:
        return "Forbidden!!!!"

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")
  else:
    form = request.form
    username = form["username"]
    password = form["password"]
    found_user = User.objects(username=username).first()
    if found_user is None:
      return "No such users"
    elif found_user.password != password:
      return "Wrong password"
    else:
      session["token"] = username
      return "OK"

@app.route("/logout")
def logout():
  if "token" in session:
    del session["token"]
  return redirect(url_for("login"))

@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
  if "token" not in session:
    return redirect("/login")

  if request.method == "GET":
    return render_template("add_movie.html")
  elif request.method == "POST":
    form = request.form
    title = form["title"]
    image = form["image"]
    year = form["year"]
    username = session["token"]
    user = User.objects(username=username).first()
    new_movie = Movie(title=title, image=image, year=year, user=user)
    new_movie.save()
    return "OK"


if __name__ == '__main__':
    app.run(debug=True)