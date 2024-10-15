from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/menu/")
def menu_page():
    return render_template("menu.html")


if __name__ == "__main__":
  app.run(port=5050, debug=True, )
