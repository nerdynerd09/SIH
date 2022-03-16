from snortTest import snortAttack
import requests
import time

matchString = "Classification: Potentially Bad Traffic"
alertString = "you are safe"

def dosDetection():
	global alertString
	snortAttack()
	i=0
	while i<100:
		with open('attackResult.txt','r') as f:
			content = f.read()
			if matchString in content:
				alertString = "You are under DDoS Attack"
				requests.post('http://127.0.0.1:5000/attackDetection', data={'attackType': "ddos"})
			
		i+=1
		print(alertString)
		# requests.post('http://127.0.0.1:5000/attackDetection', data={'attackType': "ddos"})
		time.sleep(2)
		# return alertString

# dosDetection()