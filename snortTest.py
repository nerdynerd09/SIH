from subprocess import *


def snortAttack():
	log = open('attackResult.txt', 'w') 
	Popen(['snort','-c','/etc/snort/snort.conf','-A','console'],shell=False,stdout=log,stderr=log)

snortAttack()