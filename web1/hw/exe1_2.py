from flask import Flask, redirect
app = Flask(__name__)
@app.route("/")
def home():
    return redirect("http://techkids.vn", code=302)
if __name__ == "__main__":
    app.run(debug=True)