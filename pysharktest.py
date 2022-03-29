import pyshark
import requests

# cap.sniff(timeout=10)
# print(cap)


capturePackets2 = []

def packetCapture():
	global capturePackets2
	cap = pyshark.LiveCapture(interface='eth0')
	for packets in cap.sniff_continuously():
		# print(f"packets['ip'].dst: {packets['ip'].dst}")
		# print(f"packet.ip.src: {packets.ip.src}")
		# print(f"packet[2].src: {packets[2].src}")
		# print(packets.transport_layer)
		# print(f"{packets.transport_layer} {packets.ip.src} -> {packets.ip.dst}")
		try:
			capturePackets2.append([packets.transport_layer,packets.ip.src,packets.ip.dst])
			requests.post('http://127.0.0.1:5000/datapackets', data={'src': packets.ip.src,'dst':packets.ip.dst,'layer':packets.transport_layer})		
			# requests.post('http://127.0.0.1:5000/datapackets', data={'packetList': capturePackets2})		
			# print(capturePackets2)
		except AttributeError:
			pass
	# return capturePackets2

	# if packets.dns.qry_name:
	# 	print(f"{packets.transport_layer} {packets.dns.qry_name} {packets.ip.src} -> {packets.ip.dst}")
	# elif packets.dns.resp_name:
	# 	print(f"{packets.transport_layer} {packets.dns.resp_name:} {packets.ip.src} -> {packets.ip.dst}")

# packetCapture()