import MySQLdb
def server_automate():
	#Fetching Data from Server
	
	#Remote MySQL Server Configuration
	r_db = MySQLdb.connect("ipdev.in","ipdev_sm_lacs","raspberry","ipdev_sm_lacs")
	
	#local MySQL Server Configuration
	l_db = MySQLdb.connect("localhost","root","raspberry","lacs");
	
	#Remote Server Cursor Initialization
	r_cursor = r_db.cursor()
	
	#Local Server Cursor Initialization
	l_cursor = l_db.cursor()
	
	#Fetching New Rows From the Remote Server
	query = "SELECT * FROM rfid WHERE new=1"
	
	#To be run on LocalServer of Raspberry
	query_build_insert = "INSERT INTO rfid(carduid, user, time) VALUES"

	#Query Initialization for Setting New Columns as Old Columns at Remote Server
	u_f_table = "UPDATE";
	u_f_col = []
	u_f_status = []

	#Fetching New Rows from the server
	r_cursor.execute(query)
	
	#Getting No. of the new columns on the server
	b = r_cursor.rowcount

	if b>1:
		#building Insert query and update query using loop
		for i in range(b):
			row = r_cursor.fetchone()

			#Making Query to be run on local server
			a = "('"+str(row[1])+"','"+str(row[2])+"','"+str(row[3])+"'),"
			query_build_insert = query_build_insert+str(a)
			
			#Making Query to be run on Remote Server
			u_f_table = u_f_table+" rfid t"+str(i+1)+" JOIN"
			u_f_col.append("t"+str(i+1)+".carduid='"+str(row[1])+"'")
			u_f_status.append("t"+str(i+1)+".new='0'")
			
		#Removing Last JOIN From the statement
		u_f_table = u_f_table[:-4]

		#Removing last , from the query
		query_build_insert = query_build_insert[:-1]
		
		#To run on server side
		s_update_query = u_f_table+" ON "+str(' AND '.join(u_f_col))+" SET "+str(','.join(u_f_status))
		print "\n \n "+query_build_insert+"\n \n \n \n "+s_update_query
		l_cursor.execute(query_build_insert)
		r_cursor.execute(s_update_query)
	elif b==1:
		row = r_cursor.fetchone()
		qu = "INSERT INTO rfid(carduid, user, time) VALUES"+"('"+str(row[1])+"','"+str(row[2])+"','"+str(row[3])+"')"
		up_s = "UPDATE rfid SET new=0 WHERE carduid='"+str(row[1])+"'"
		l_cursor.execute(qu)
		r_cursor.execute(up_s)
	else:
		print "No New Rows at the server"
server_automate()

