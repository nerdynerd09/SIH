from snortTest import snortAttack
import requests
import time
from sendmail import mailReport


matchString = "Classification: Potentially Bad Traffic"
synAttack = "[Classification: Potentially Bad Traffic] [Priority: 2] {TCP}"
icmpAttack = "[Classification: Attempted Information Leak] [Priority: 2] {ICMP}"

alertString = "You are DoS safe"
synAlert = "You are SYN DoS safe"
icmpAlert = "You are ICMP DoS safe"

synMailSent = False
icmpMailSent = False

def dosDetection():
	global alertString
	global synAlert
	global icmpAlert
	global synMailSent
	global icmpMailSent

	snortAttack()
	i=0
	while True:
		with open('attackResult.txt','r') as f:
			content = f.read()
			# if matchString in content:
			# 	alertString = "You are under DDoS Attack"

			if synAttack in content:
				synAlert = "You are under SYN DDoS Attack"
				requests.post('http://127.0.0.1:5000/attackDetection', data={'attackType': "ddos",'alertType': "syn"})
				if synMailSent == False:
					mailReport("SYN DOS attack ho gya!!!")
					print("SYN mail sent")
					synMailSent = True

			if icmpAttack in content:
				icmpAlert = "You are under ICMP DDoS Attack"
				requests.post('http://127.0.0.1:5000/attackDetection', data={'attackType': "ddos",'alertType': "icmp"})
				if icmpMailSent == False:
					mailReport("ICMP DOS attack ho gya!!!")
					print("ICMP mail sent")
					icmpMailSent = True

				# requests.post('http://127.0.0.1:5000/attackDetection', data={'attackType': "ddos"})
				# mailReport("DOS attack ho gya!!!")
		# i+=1
		# print(f"SynAlert: {synAlert}\tICMPAlert: {icmpAlert}")
		# requests.post('http://127.0.0.1:5000/attackDetection', data={'attackType': "ddos"})
		time.sleep(2)
		# return alertString

# dosDetection()