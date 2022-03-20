import scapy.all as scapy
from scapy.layers import http
import requests

dataList = []
returnValue = None
urlValue = ""
uncleanIndex = 0

def sniffing(interface):
    scapy.sniff(iface=interface,prn=process_packet)

def process_packet(packet):
    global returnValue
    global urlValue 
    if packet.haslayer(http.HTTPRequest):
        urlValue = (packet[http.HTTPRequest].Host).decode('utf-8')
        
    if returnValue != urlValue:
        returnValue = urlValue
        if returnValue in dataList:
            pass
        else:
            # requests.post('http://127.0.0.1:5000/addUrl', data={'url': returnValue})
            global uncleanIndex
            uncleanIndex=0
            data = requests.get('https://www.virustotal.com/api/v3/domains/'+returnValue,headers={'x-apikey':'bb64ef17ec6332feded9ce796fb84883f056eaa55cd65cf2274d9e03cb51c424'}).json()
            try:
                for key in ((data['data']['attributes']['last_analysis_results']).keys()):
                    if (data['data']['attributes']['last_analysis_results'][key]['result']) != "clean":
                        uncleanIndex +=1 
            except KeyError:
                pass
            requests.post('http://127.0.0.1:5000/addUrl', data={'url': returnValue,'urlScore':uncleanIndex})

            dataList.append([returnValue,uncleanIndex])
        # print(f"ReturnValue: {returnValue}")
    else:
        pass
    return dataList

