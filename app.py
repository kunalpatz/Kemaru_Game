from flask import Flask, render_template, request, url_for, send_from_directory
from getBoard import *
import json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/rules")
def rules():
    return render_template("rules.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/new" , methods=['POST'])
def new_game():
    data = launch(request.form['level'])
    final_layout = {'final_layout': data['final_solution'], 'unsolved': data['pattern']}
    with open('temp/temp.json', 'w') as file:
        file.write(json.dumps(final_layout))
    file.close()
    return render_template("newgame.html", result=data['pattern'])

@app.route("/solution", methods=["GET", "POST"])
def solution():
    with open('temp/temp.json', 'r') as file:
        data = json.load(file)
    file.close()
    return render_template("solution.html", result=data['unsolved'], soln=data['final_layout'])

# TODO : implement submit
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        req = request.form
    print(req)
    with open('temp/temp.json', 'r') as file:
        data = json.load(file)
    file.close()
    print(data)
    return render_template("solution.html", result=data['unsolved'], soln=data['final_layout'])

if __name__ == "__main__":
    app.run(port=1024, debug=True)