from twisted.internet import task
from twisted.internet import reactor

timeout = 1.0 # Sixty seconds

def doWork():
    import subprocess
    time=subprocess.check_output("date +%s",shell=True).strip('\n')
    import csv
    f=open('time.csv','at')
    writer=csv.writer(f)
    writer.writerow([time])
    f.close()
    pass

l = task.LoopingCall(doWork)
l.start(timeout) # call every sixty seconds

reactor.run()
