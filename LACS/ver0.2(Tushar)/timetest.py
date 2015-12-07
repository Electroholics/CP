from twisted.internet import task
from twisted.internet import reactor
import subprocess
import csv

timeout = 1.0 # One second

def doWork():
    time=subprocess.check_output("date +%s",shell=True).strip('\n')#Fetching time from rtc
    f=open('time.csv','at')#opening log file
    writer=csv.writer(f)#appending to log file
    writer.writerow([time])
    f.close()
    pass

l = task.LoopingCall(doWork)
l.start(timeout) # call every second

reactor.run()
