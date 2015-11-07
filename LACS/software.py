import urllib2
import MySQLdb
import time
def addnewentry(uid, user, time):
	db = MySQLdb.connect("localhost","root","raspberry","lacs");
	c = db.cursor()
	q = "INSERT INTO rfid(carduid, user, time) VALUES("+str(uid)+","+str(user)+","+str(time)+")"
	c.execute(q)

def auth(uid):
	status = 0
	if len(uid)>=4:
		r_db = MySQLdb.connect("localhost","root","raspberry","lacs");
		r_cursor = r_db.cursor()
		key = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
		query = "SELECT * FROM rfid WHERE carduid='%s'" % key
		
		try:
			r_cursor.execute(query)
			data = r_cursor.rowcount
			status = data
			print status, uid
			if int(data) == 0:
				data = server_auth(uid)
				status = data
		except:
			print "Error: Unable to Fetch Data From Local"
	return status

	
def server_auth(uid):
	print "Running Server Authentication \n"
	status = 0
	r_db = MySQLdb.connect("ipdev.in","ipdev_sm_lacs","raspberry","ipdev_sm_lacs")
	r_cursor = r_db.cursor()
	key = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
	query = "SELECT * FROM rfid WHERE carduid='%s' AND deleted=0" % key
	
	try:
		r_cursor.execute(query)
		data = r_cursor.rowcount
		status = data
		roww = r_cursor.fetchone()
		print str(roww[1])
		addnewentry(str(roww[1]),str(roww[2]),str(roww[3]))
	except:
		print "Error: Unable to Fetch Data From Server"
	return status

	
def log(uid):
	fileName = "logs/logs-298yhjhboihnt.csv"
	fh = open(fileName,"a")
	ts = time.time()
	u = '|'.join(str(x) for x in uid)
	s = str(u) + "," + str(ts) + "\n"
	fh.write(s)
	print "Log Entered"
	

