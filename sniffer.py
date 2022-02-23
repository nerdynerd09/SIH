from time import sleep
import scapy.all as scapy
from scapy.layers import http

returnValue = None

def sniffing(interface):
    # scapy.sniff(filter='port 80' ,iface='Wi-fi',prn=process_packet)
    scapy.sniff(iface=interface,prn=process_packet)

def process_packet(packet):
    # print(packet.show())
    global returnValue 
    if packet.haslayer(http.HTTPRequest):
        returnValue = (packet[http.HTTPRequest].Host).decode('utf-8')
        # dataList.append((packet[http.HTTPRequest].Host).decode('utf-8'))
    return returnValue
    sleep(2)

# for i in range(5):
#     t = threading.Thread(target=sniffing,args=['Wi-Fi'])
#     print(threading.current_thread().getName())
#     t.start()