import sqlite3

#Open database
conn = sqlite3.connect('database.db')

#Create table
conn.execute('''CREATE TABLE projects
		(pid INTEGER PRIMARY KEY, 
		name TEXT,
		locality TEXT,
		address TEXT,
		date DATE,
		phone_no TEXT,
		no_student TEXT,
		status TEXT	)''')

conn.execute('''CREATE TABLE versions
		(version INTEGER PRIMARY KEY,
		pid INTEGER,
		date DATE,
		FOREIGN KEY(pid) REFERENCES projects(pid)
		)''')

conn.execute('''CREATE TABLE templates
		(qid INTEGER PRIMARY KEY,
		questions TEXT,
         qtype TEXT
		)''')

conn.execute('''CREATE TABLE assessment
		(aid INTEGER PRIMARY KEY,
		 pid INTEGER,
		 qid INTEGER,
		 answers TEXT,
		 FOREIGN KEY(pid) REFERENCES projects(pid),
		 FOREIGN KEY(qid) REFERENCES templates(qid)
		)''')
conn.execute('''CREATE TABLE actionplan
		(aid INTEGER PRIMARY KEY,
		 pid INTEGER,
		 activities TEXT,
		 description TEXT,
		 date DATE,
		 progress TEXT,
		 version INTEGER,
		 FOREIGN KEY(pid) REFERENCES projects(pid),
		 FOREIGN KEY(version) REFERENCES versions(version)
		 
		)''')
conn.execute('''CREATE TABLE users
		(qid INTEGER PRIMARY KEY,
		 username TEXT,
		 password TEXT,
		 role TEXT
		)''')





conn.close()
