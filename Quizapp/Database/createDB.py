import sqlite3

conn = sqlite3.connect('Tiango.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Cplusplus;
DROP TABLE IF EXISTS Java;
DROP TABLE IF EXISTS Python;
DROP TABLE IF EXISTS MySQL;
DROP TABLE IF EXISTS JavaScript;
DROP TABLE IF EXISTS Aptitude;

DROP TABLE IF EXISTS CplusplusAttempted;
DROP TABLE IF EXISTS JavaAttempted;
DROP TABLE IF EXISTS PythonAttempted;
DROP TABLE IF EXISTS MySQLAttempted;
DROP TABLE IF EXISTS JavaScriptAttempted;
DROP TABLE IF EXISTS AptitudeAttempted;

DROP TABLE IF EXISTS CplusplusScore;
DROP TABLE IF EXISTS JavaScore;
DROP TABLE IF EXISTS PythonScore;
DROP TABLE IF EXISTS MySQLScore;
DROP TABLE IF EXISTS JavaScriptScore;
DROP TABLE IF EXISTS AptitudeScore;

CREATE TABLE User (
    id  TEXT NOT NULL PRIMARY KEY UNIQUE,
    name    TEXT,
    password TEXT
);

CREATE TABLE CplusplusAttempted (
	id  TEXT NOT NULL,
    attempt INTEGER,
    FOREIGN KEY(id) REFERENCES User(id)
);

CREATE TABLE JavaAttempted (
	id  TEXT NOT NULL,
    attempt INTEGER,
    FOREIGN KEY(id) REFERENCES User(id)
);

CREATE TABLE PythonAttempted (
	id  TEXT NOT NULL,
    attempt INTEGER,
    FOREIGN KEY(id) REFERENCES User(id)
);

CREATE TABLE MySQLAttempted (
	id  TEXT NOT NULL,
    attempt INTEGER,
    FOREIGN KEY(id) REFERENCES User(id)
);

CREATE TABLE JavaScriptAttempted (
	id  TEXT NOT NULL,
    attempt INTEGER,
    FOREIGN KEY(id) REFERENCES User(id)
);

CREATE TABLE AptitudeAttempted (
	id  TEXT NOT NULL,
    attempt INTEGER,
    FOREIGN KEY(id) REFERENCES User(id)
);

CREATE TABLE CplusplusScore (
	id  TEXT NOT NULL,
    Score INTEGER,
    FOREIGN KEY(id) REFERENCES User(id)
);

CREATE TABLE JavaScore (
	id  TEXT NOT NULL,
    Score INTEGER,
    FOREIGN KEY(id) REFERENCES User(id)
);

CREATE TABLE PythonScore (
	id  TEXT NOT NULL,
    Score INTEGER,
    FOREIGN KEY(id) REFERENCES User(id)
);

CREATE TABLE MySQLScore (
	id  TEXT NOT NULL,
    Score INTEGER,
    FOREIGN KEY(id) REFERENCES User(id)
);

CREATE TABLE JavaScriptScore (
	id  TEXT NOT NULL,
    Score INTEGER,
    FOREIGN KEY(id) REFERENCES User(id)
);

CREATE TABLE AptitudeScore (
	id  TEXT NOT NULL,
    Score INTEGER,
    FOREIGN KEY(id) REFERENCES User(id)
);
CREATE TABLE Cplusplus (
	question TEXT,
	option1 TEXT,
	option2 TEXT,
	option3 TEXT,
	option4 TEXT,
	answer TEXT
);

CREATE TABLE Java (
	question TEXT,
	option1 TEXT,
	option2 TEXT,
	option3 TEXT,
	option4 TEXT,
	answer TEXT
);

CREATE TABLE Python (
	question TEXT,
	option1 TEXT,
	option2 TEXT,
	option3 TEXT,
	option4 TEXT,
	answer TEXT
);

CREATE TABLE MySQL (
	question TEXT,
	option1 TEXT,
	option2 TEXT,
	option3 TEXT,
	option4 TEXT,
	answer TEXT
);

CREATE TABLE JavaScript (
	question TEXT,
	option1 TEXT,
	option2 TEXT,
	option3 TEXT,
	option4 TEXT,
	answer TEXT
);

CREATE TABLE Aptitude (
	question TEXT,
	option1 TEXT,
	option2 TEXT,
	option3 TEXT,
	option4 TEXT,
	answer TEXT
);

''');

cur.close();
