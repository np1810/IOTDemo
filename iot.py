## Setup GPIO Pin 11 as LED+ and Pin 9 as GROUND

## Auto Start Python Script
## sudo nano /etc/profile
## To the bottom add the following line
## sudo python /home/pi/iot.py

import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library to use 'sleep'
import urllib ## Import url library

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
pin = 11 ## Set PIN number
GPIO.setup(pin, GPIO.OUT) ## Setup GPIO

response = "fail"
while True:
	res = urllib.urlopen("http://nitinpathak.com/IOTDemo/state.txt").read()
	if response != res: ## Enter only when STATE CHANGES...
		response = res
		if response == "on":
			print "Changing State to ON..."
			GPIO.output(pin,GPIO.HIGH)
		elif response == "off":
			print "Changing State to OFF..."
			GPIO.output(pin,GPIO.LOW)
		else:
			## print "ERROR! Breaking Loop.."
			## break ## break on unknown response
	time.sleep(1) ## 1 second delay
## response.close()
## GPIO.cleanup()
