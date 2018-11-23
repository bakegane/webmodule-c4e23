from flask import Flask, render_template

app = Flask(__name__)

#function binding
@app.route("/") #neu user truy cap / , home dc start
def home():
    return "Hello Flask"

@app.route("/c4e")
def c4e():
    return "Hello C4E"

@app.route("/me")
def me():
    return "Hello Tuan"

@app.route("/add/<int:x>/<int:y>")
def add(x, y):
    s = x + y
    return str(s)

@app.route("/posts/<int:index>")
def posts(index):
    titles = [
        "Trời mưa",
        "Trời nắng",
        "Trời mây",     
    ]
    t = titles[index]
    contents = [
        "Tôi ngủ",
        "Tôi chơi game",
        "Tôi nghe nhạc",
    ]
    c = contents[index]
    return render_template("post.html", title=t, content=c)

@app.route("/movie")
def movie():
    return render_template ("movie.html", name="Batman", image="https://apollo2.dl.playstation.net/cdn/UP9000/CUSA02299_00/FREE_CONTENTlfrM9XqFMPLKmUpQpxJS/PREVIEW_SCREENSHOT3_163995.jpg")

@app.route("/movies")
def movies():
#    movie_titles = [
#        "Deadpool",
#        "Black widow",
#        "Hulk",
#        "Caps",
#    ]
    movie_list = [
        {
            "title": "Deadpool",
            "image": "https://apollo2.dl.playstation.net/cdn/UP9000/CUSA02299_00/FREE_CONTENTlfrM9XqFMPLKmUpQpxJS/PREVIEW_SCREENSHOT3_163995.jpg",
        },
        {
            "title": "Batman",
            "image": "https://apollo2.dl.playstation.net/cdn/UP9000/CUSA02299_00/FREE_CONTENTlfrM9XqFMPLKmUpQpxJS/PREVIEW_SCREENSHOT3_163995.jpg",
        },
        {
            "title": "Spiderman",
            "image": "https://apollo2.dl.playstation.net/cdn/UP9000/CUSA02299_00/FREE_CONTENTlfrM9XqFMPLKmUpQpxJS/PREVIEW_SCREENSHOT3_163995.jpg",
        },
    ]
    return render_template("movies.html", movies=movie_list)

if __name__ == "__main__":
    app.run(debug=True)