import json
import os

from flask import Flask, render_template, request

from getBoard import *

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
    if os.stat('temp/temp.json').st_size == 0:
        open('temp/temp.json', 'w').close()
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
@app.route("/quit",  methods=["GET", "POST"])
def quit():
    with open('temp/temp.json', 'r') as file:
        data = json.load(file)
    file.close()
    return render_template("quit.html", result=data['unsolved'], soln=data['final_layout'])

@app.route("/solution_after_try", methods=["GET", "POST"])
def solution_after_try():
    with open('temp/temp.json', 'r') as file:
        data = json.load(file)
    file.close()
    return render_template("solution_after_try.html", result=data['unsolved'], soln=data['final_layout'])


@app.route("/submit", methods=["GET", "POST"])
def submit():
    userInputs={}
    solution_set = {}
    decision = []

    for key, value in request.form.to_dict(flat=False).items():
        for elem in value:
            if elem == '':
                userInputs.update({key: -1})
            else:
                userInputs.update({key: int(elem)})
    with open('temp/temp.json', 'r') as file:
        data = json.load(file)
    file.close()

    for keys, values in data['final_layout'].items():
        for key, val in values.items():
            solution_set.update({key: val[0]})

    for key, user in userInputs.items():
        if solution_set[key] == user:
            decision.append(1)
        else:
            decision.append(3)
    if 3 in decision:
        return render_template("submitWrong.html", soln=data['final_layout'])
    else:
        return render_template("submitWin.html")




if __name__ == "__main__":
    app.run(debug=True)