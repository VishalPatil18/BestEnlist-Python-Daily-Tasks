import sqlite3 as db

con = db.connect("Tiango.sqlite")
cur = con.cursor()

cur.executescript('''

DROP TABLE IF EXISTS CplusplusUserAnswer;
DROP TABLE IF EXISTS JavaUserAnswer;
DROP TABLE IF EXISTS PythonUserAnswer;
DROP TABLE IF EXISTS MySQLUserAnswer;
DROP TABLE IF EXISTS JavaScriptUserAnswer;
DROP TABLE IF EXISTS AptitudeUserAnswer;


CREATE TABLE CplusplusUserAnswer(
	id TEXT,
	Q1 TEXT,
	Q2 TEXT,
	Q3 TEXT,
	Q4 TEXT,
	Q5 TEXT,
	Q6 TEXT,
	Q7 TEXT,
	Q8 TEXT,
	Q9 TEXT,
	Q10 TEXT
);

CREATE TABLE JavaUserAnswer(
	id TEXT,
	Q1 TEXT,
	Q2 TEXT,
	Q3 TEXT,
	Q4 TEXT,
	Q5 TEXT,
	Q6 TEXT,
	Q7 TEXT,
	Q8 TEXT,
	Q9 TEXT,
	Q10 TEXT
);

CREATE TABLE PythonUserAnswer(
	id TEXT,
	Q1 TEXT,
	Q2 TEXT,
	Q3 TEXT,
	Q4 TEXT,
	Q5 TEXT,
	Q6 TEXT,
	Q7 TEXT,
	Q8 TEXT,
	Q9 TEXT,
	Q10 TEXT
);

CREATE TABLE MySQLUserAnswer(
	id TEXT,
	Q1 TEXT,
	Q2 TEXT,
	Q3 TEXT,
	Q4 TEXT,
	Q5 TEXT,
	Q6 TEXT,
	Q7 TEXT,
	Q8 TEXT,
	Q9 TEXT,
	Q10 TEXT
);

CREATE TABLE JavaScriptUserAnswer(
	id TEXT,
	Q1 TEXT,
	Q2 TEXT,
	Q3 TEXT,
	Q4 TEXT,
	Q5 TEXT,
	Q6 TEXT,
	Q7 TEXT,
	Q8 TEXT,
	Q9 TEXT,
	Q10 TEXT
);

CREATE TABLE AptitudeUserAnswer(
	id TEXT,
	Q1 TEXT,
	Q2 TEXT,
	Q3 TEXT,
	Q4 TEXT,
	Q5 TEXT,
	Q6 TEXT,
	Q7 TEXT,
	Q8 TEXT,
	Q9 TEXT,
	Q10 TEXT
);


''')

con.commit()
cur.close()

