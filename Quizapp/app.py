from flask import Flask, render_template, request, session, redirect, flash, url_for
import sqlite3 as db


app = Flask(__name__)

app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

database_path = "Database/Tiango.sqlite"

# The Login Page
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')
	
# The Registration Page
@app.route('/signupPage')
def signupPage():
	return render_template('signupPage.html')
    
# From Login Page it will be redirected to check if user is valid or not
@app.route('/validate', methods=["POST"])
def validate():
	id = request.form.get("userID")
	password = request.form.get("pwd")
	try:
		with db.connect(database_path) as conn:
			cur = conn.cursor()
			cur.execute("SELECT id, password FROM User WHERE id = ?", (id,))
			row = cur.fetchone()
			cur.close()
			if row is None:
				flash("Invalid username or password")	# Display message to invalid user.
				return redirect(url_for("index"))
			elif (row[0] == id and row[1] == password):
				session["id"] = id
				session["logged_in"] = True
				return redirect(url_for("allQuizes"))
			else:
				flash("Invalid username or password")	# Display message to invalid user.
				return redirect(url_for("index"))
				
	except:
		flash("Invalid!")
		return redirect(url_for("index"))
	
# from Registration Page, it will be redirected to check if user already exists
@app.route('/signupValidate', methods=["POST"])
def signupValidate():
	id = request.form.get("userID")
	user = request.form.get("uname")
	password = request.form.get("pwd")
	try:
		with db.connect(database_path) as conn:
			cur = conn.cursor()
			cur.execute("SELECT id FROM User WHERE id = ?", (id,))
			row = cur.fetchone()
			if row is None:
				cur.execute("INSERT INTO User VALUES(?, ? ,?)", (id, user, password))
				conn.commit()
				cur.close()
				session["id"] = id
				session["logged_in"] = True
				return redirect(url_for("allQuizes"))
			else:
				flash("User already exists.")
				return redirect(url_for("signupPage"))
	except Exception:
		flash("Invalid request.")
		return redirect(url_for("signupPage"))
		

@app.route('/allQuizes', methods = ["GET", "POST"])
def allQuizes():
	if session["logged_in"] == True:
		return render_template('allQuizes.html', name = session["id"])
	else:
		return redirect(url_for("index"))
	

"""Check if user has already attempted that quiz or not
If attempted, then display score
"""
@app.route('/check')
def check():
	if session["logged_in"] == True:
		id = session["id"]
		quizName = request.args.get("type")
		session["quizName"] = quizName
		attemptTable = quizName + "Attempted"	# concat "Attempted" word, because thats how I have named the table
		try:
			with db.connect(database_path) as con:
				cur = con.cursor()
				query = "SELECT id FROM {} WHERE id = ?".format(attemptTable)
				cur.execute(query, (id,))
				row = cur.fetchone()
				cur.close()
				#Quiz not attempted
				if row is None:
					return redirect(url_for("instructions"))
				else:
					return redirect(url_for("display"))
		except Exception as e:
			print(e)
			return redirect(url_for("allQuizes"))
	else:
		return redirect(url_for("index"))
			
		
@app.route('/instructions')
def instructions():
	if session["logged_in"] == True:
		return render_template('instructions.html', quiz = session["quizName"], name = session["id"])
	else:
		return redirect(url_for("index"))

# Display list of questions
@app.route('/questions', methods = ["POST"])
def questions():
	quizName = session["quizName"]
	try:
		with db.connect(database_path) as conn:
			cur = conn.cursor()
			query = "SELECT * FROM {}".format(quizName)
			cur.execute(query)
			ques_opts = cur.fetchall()
			cur.close()
			return render_template("questions.html", questions = ques_opts, quizName = quizName)
	except:
		return redirect(url_for("allQuizes"))

		
# Calculate score and store in database.
@app.route('/calculate', methods = ["GET", "POST"])
def calculate():
	id = session["id"]
	attemptTable = session["quizName"] + "Attempted"
	scoreTable = session["quizName"] + "Score"
	userAnsTable = session["quizName"] + "UserAnswer"
	quiz = session["quizName"]
	try:
		with db.connect(database_path) as conn:
			cur = conn.cursor()
			query = "SELECT answer FROM {}".format(quiz)
			cur.execute(query)
			rows = cur.fetchall()
			score = 0
			user = list()
			for i in range(10):		# 10 questions
				user.append(request.form.get(str(i+1)))
				score += 1 if user[i] == rows[i][0] else 0
				
			if quiz == "Aptitude":		#Apti has 10 questions 2 marks each
				score *= 2
			query = "INSERT INTO {} VALUES (?, ?)".format(attemptTable)
			cur.execute(query, (id, 1))
			query = "INSERT INTO {} VALUES (?, ?)".format(scoreTable)
			cur.execute(query, (id, score))
			query = "INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(userAnsTable)
			cur.execute(query, (id, user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9])) 
			conn.commit()
			cur.close()
		return redirect(url_for("display"))
	except Exception as e:
		print("in calculate",e)
		return redirect(url_for("allQuizes"))
	
# Display score	
@app.route('/display', methods = ["GET", "POST"])
def display():
	if session["logged_in"] == True:
		id = session["id"]
		scoreTable = session["quizName"] + "Score"	# concat "Score" word because thats how I have named the table
		try:
			with db.connect(database_path) as conn:
				cur = conn.cursor()
				query = "SELECT * FROM {} WHERE id = ?".format(scoreTable)
				cur.execute(query, (id,))
				row = cur.fetchone()
				query = "SELECT * FROM {} ORDER BY Score DESC, id".format(scoreTable)
				cur.execute(query)
				scores = cur.fetchall()
				cur.close()
				return render_template('display.html', score = row[1], scores = scores)
		except Exception as e:
			print("in display",e)
			return redirect(url_for("allQuizes"))
	else:
		return redirect(url_for("index"))
	
@app.route('/answers', methods = ["GET", "POST"])
def answers():
	id = session["id"]
	quiz = session["quizName"]
	userAnsTable = quiz + "UserAnswer"
	try:
		with db.connect(database_path) as conn:
			cur = conn.cursor()
			query = "SELECT * FROM {}".format(quiz)
			cur.execute(query)
			ques_opts = cur.fetchall()
			query = "SELECT * FROM {} WHERE id = ?".format(userAnsTable)
			cur.execute(query, (id, ))
			userAns = cur.fetchone()
			cur.close()
			print(userAns)
			return render_template("answers.html", quizName = quiz, questions = ques_opts, user_ans = userAns)
	except Exception as e:
		print("answers", e)
		return redirect(url_for("display"))
		
@app.route('/logout')
def logout():
	session["logged_in"] = False 
	return redirect(url_for("index"))

if __name__ == "__main__":
	app.run(port=5000, debug="True")
