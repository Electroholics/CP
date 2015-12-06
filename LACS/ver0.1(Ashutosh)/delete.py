import MySQLdb
#Remote MySQL Server Configuration
r_db = MySQLdb.connect("ipdev.in","ipdev_sm_lacs","raspberry","ipdev_sm_lacs")
	
#local MySQL Server Configuration
l_db = MySQLdb.connect("localhost","root","raspberry","lacs");

#Remote Server Cursor Initialization
r_cursor = r_db.cursor()
	
#Local Server Cursor Initialization
l_cursor = l_db.cursor()

#Fetching New Rows From the Remote Server to Delete
query = "SELECT * FROM rfid WHERE deleted=1"
toDelete = []
r_cursor.execute(query)
b = r_cursor.rowcount

if b>1:
	for i in range(b):
		r = r_cursor.fetchone()
		toDelete.append(str(r[1]))
	q = "DELETE FROM rfid WHERE carduid IN ('" + str(','.join(toDelete)) + "')"
	l_cursor.execute(q)
elif b==1:
	s = r_cursor.fetchone()
	l_cursor.execute("DELETE FROM rfid WHERE carduid='"+str(s[1])+"'")
else:
	print "Everything OK"