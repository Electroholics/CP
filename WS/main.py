import time
import Adafruit_DHT
#library by Adafruit to interface DHT11
sensor = Adafruit_DHT.DHT11
#defining the sensor DHT22 compatible
pin = 4
#GPIO pin no
while 1:
	tempfile = open("/sys/bus/w1/devices/28-00000554028a/w1_slave")
	#reading data from DS18B20
	text = tempfile.read()
	tempfile.close()
	temp = float(text.split("\n")[1].split(" ")[9][2:])/1000
	#reading data from DHT11
	humidity,temperature=Adafruit_DHT.read_retry(sensor,pin)
	#printing required temp and humidity
	print "Temperature:",temp,"\nHumidity:",humidity
	time.sleep(1)
