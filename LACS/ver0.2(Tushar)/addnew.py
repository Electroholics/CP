import MySQLdb
def addnewentry(uid,name,rollno):
	#Connecting to MySQL database
	db = MySQLdb.connect("localhost","root","raspberry","local");
	#Declaring a cursor to execute SQL queries
	c = db.cursor()
	#query for adding UID ,ROLLNO,NAME
	insert = """INSERT INTO auth(uid, rollno, name) VALUES('%s',%s,'%s')"""%(uid,rollno,name)
	# print insert
	try:
		c.execute(insert)
		db.commit()
	except:
		db.rollback()
	# c.execute("SELECT * FROM auth")	
	# row=c.fetchone()
	# print row
	db.close()


uid=raw_input("Enter uid:")
rollno=input("Enter roll number:")
name=raw_input("Enter your name:")
addnewentry(uid,name,rollno)
