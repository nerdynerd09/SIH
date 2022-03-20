import requests,nmap
import re
from nmapscanner import portScanner

servicesList = []
cveList = []

dictionary,ipList,currentIP,currentMAC,networkIPs,networkMAC,vendor = portScanner()

for ip in ipList:
    for key in dictionary['scan'][ip]['tcp'].keys():
        servicesList.append([ip,dictionary['scan'][ip]['tcp'][key]['product'],dictionary['scan'][ip]['tcp'][key]['version']])
print(servicesList)


for i in range (len(servicesList)):
    print(servicesList[i][1])
    print(servicesList[i][2])
    cveUrl = f'https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword={servicesList[i][1]}+{servicesList[i][2]}'
    res = requests.get(cveUrl).text  

    reg = re.findall(r'name=CVE.*\"',res)

    for j in range(5):
        try:
            print(servicesList[i][0],servicesList[i][1],reg[j][5:-1])
            cveList.append([servicesList[i][0],servicesList[i][1],reg[j][5:-1]])
        except IndexError:
            pass


print(cveList)