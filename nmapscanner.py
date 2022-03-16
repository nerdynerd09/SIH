# Getting basic details
import subprocess,nmap
import re
cmdList = []
subdomainIP = ""
currentIP = ""
currentMAC = ""
def nmapper():
	cmd = subprocess.check_output(['ifconfig']).decode('utf-8')
	global currentIP
	currentIP = (re.findall(r'inet\s.*\sn',cmd))[0][5:-2]
	global currentMAC
	currentMAC = re.findall(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',cmd)[0]
	print(f"Current IP: {currentIP}")
	print(f"Current MAC: {currentMAC}")
	global subdomainIP	
	subdomainIP = re.findall(r'.*\.',currentIP)
	subdomainIP = str(*subdomainIP)+'0/24' 

	# print(subdomainIP)

	# Getting all the devices inside a network

	# print("\n\n\t\t**********Searching for devices**********\n")
	nmapResult = subprocess.check_output(['nmap','-sn',subdomainIP]).decode('utf-8')
	# print("Nmap Result")
	# print(nmapResult)

	networkIPs = []
	# networkMAC = []
	vendor = []


	# Getting network IPs
	networkIPList = re.findall(r'Nmap scan.*',nmapResult)
	# print(networkIPList)
	for i in range(len(networkIPList)):
		networkIPs.append(re.findall(r'\d.*',networkIPList[i]))
	# print("IP Table")
	# print(networkIPs)


	# Getting Network Mac
	networkMAC = (re.findall(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',nmapResult))
	# print("MAC TAble")
	# print(networkMAC)

	# Getting Vendor
	vendorList = re.findall(r'MAC.*',nmapResult)
	for i in range(len(vendorList)):
		vendorMatch = re.findall(r'\(.*',vendorList[i])
		vendor.append(*vendorMatch)

	# print("Vendor Table")
	# print(vendor)

	# print("IP\t\t\tMAC Address\t\t\t\t\tVendor")
	# for i in range(len(networkIPList)-1):
	# 	print(f"{networkIPs[i][0]}\t\t{networkMAC[i]}\t\t{vendor[i]}")

	# return networkIPs,networkMAC,vendor,currentIP,currentMAC
	return networkIPs,networkMAC,vendor

def portScanner():
	nm = nmap.PortScanner()
	# subdomainIP = '192.168.1.0/24'
	networkIPs,networkMAC,vendor =nmapper()
	dictionary = nm.scan(subdomainIP,'0-1000')
	# ip = dictionary['scan']
	ipList = []
	# print(dictionary)
	for i in (dictionary['scan']):
		try:
			for key in ((dictionary['scan'][i]['tcp']).keys()):
				# print(f"Port number: {key} is running on ip {i}")
				if i not in ipList:
					ipList.append(i)
		except KeyError:
			pass
	# print(ip)
	# print(f"IPList: {ipList}\nDictionary: {dictionary}\nCurrentIP: {currentIP}\nCurrentMac: {currentMAC}\nNewtWork: {networkMAC}\nNetworkIPs: {networkIPs}\nVendor: {vendor}")
	return dictionary,ipList,currentIP,currentMAC,networkIPs,networkMAC,vendor


# portScanner()