import urllib2
def auth(uid):
	status = urllib2.urlopen("http://sm.ipdev.in/lacs/auth.php?id="+str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])).read() #contacting the server to check whether UID is present or not
	return status
def log(uid):
	#adding record to log
	