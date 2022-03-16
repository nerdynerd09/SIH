import time
import random

alertString = "Safe!!"
def testFunc():
	global alertString
	while True:
		a = random.randint(1,5)
		if a == 2:
			alertString = "Attaccked!!"
		else:
			alertString = "Safe!!"
		print(f"AlertString: {alertString}, a:{a}")
		time.sleep(2)
# testFunc()