import scapy.all as scapy
import requests
from sendmail import mailReport

arpResult = "You are ARP safe!!"
def arpSniff(interface):
	scapy.sniff(iface=interface,prn=process_sniffed_packet)

def process_sniffed_packet(packet):
	global arpResult	
	# arpResult = None
	# arpResult = "Everyhting is safe"
	if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
		originalmac = mac(packet[scapy.ARP].psrc)
		responsemac = packet[scapy.ARP].hwsrc
		if originalmac != responsemac:
			arpResult = "Alert!! ARP Table attacked."
			requests.post('http://127.0.0.1:5000/attackDetection', data={'attackType': "arp"})
			mailReport("ARP Table Spoofed")
			# print(arpResult)
	# return arpResult
	print(arpResult)
 	

def mac(ipadd):
	arpRequest = scapy.ARP(pdst=ipadd)
	br = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_req_br = br / arpRequest 
	list_1 = scapy.srp(arp_req_br, timeout=5,verbose=False)[0]
	return list_1[0][1].hwsrc
	# return list_1


# arpSniff('eth0')



