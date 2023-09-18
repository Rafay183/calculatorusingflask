from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("cal1.html")

@app.route("/cal2")
def contact():
    return render_template("cal2.html")

@app.route("/cal3")
def about():
    return render_template("cal3.html")

if __name__ == "__main__":
    app.run(debug=True)