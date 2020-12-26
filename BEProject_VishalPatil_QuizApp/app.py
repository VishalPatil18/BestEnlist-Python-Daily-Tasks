from flask import Flask,render_template,request,url_for,redirect,session,flash
from datetime import datetime

import json

with open('quiz.json') as file:
    quizapp = json.load(file)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

# Routes for the app
@app.route("/",methods=['GET','POST'])
def quiz():
    if request.method == 'POST':
        # Store the theme in a session variable
        session["theme"] = request.form["theme"]

        # Store all the questions, choices and correct answer for the selected theme
        session["game"] = [{theme:questions} for (theme,questions) in quizapp.items() if theme==session["theme"]][0]
        
        session["total_questions"] = len(session["game"][session["theme"]])

        session["id"] =  0
        session["score"] = 0

        session["current_question"] = [game for game in session["game"][session["theme"]]][session["id"]]

        return render_template("start_quiz.html", game = session["current_question"])

    return render_template("quiz.html", quizapp = quizapp)


@app.route('/start_quiz',methods=['GET','POST'])
def start_quiz():
    if request.method == "POST":
        print(session["id"])
        given_answer = request.form["given_answer"]
        print(given_answer)
        if given_answer == session["current_question"]["answer"]:
            flash("Correct Answer","correct")
            session["score"] += 1
        else:
            flash("Incorrect Answer","wrong")

        if session["total_questions"] > session["id"] + 1:
            session["id"] += 1
            session["current_question"] = [game for game in session["game"][session["theme"]]][session["id"]]
        else:
            flash("Quiz Completed. Try another Theme","completed")

    return render_template("start_quiz.html",
    game = session["current_question"])


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)