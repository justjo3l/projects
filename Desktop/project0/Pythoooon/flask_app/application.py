from flask import Flask, render_template
from functions import length
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("page0.html")


@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    check = name == "Joel"
    WelcName = "Hello, " + name
    le = int(length(name))
    nol = le
    nas = set()
    for i in range(nol):
        nas.add(i)
    return render_template("page0.html", check=check, WelcName=WelcName,
                           nas=nas, le=nol)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
