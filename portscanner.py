import nmap,json


nm = nmap.PortScanner()
ip = '192.168.1.136'
# dictionary = nm.scan('192.168.1.0/24','22-443')
dictionary = nm.scan(ip,'0-65535')
print("\n")

json_object = json.dumps(dictionary, indent = 4) 
print(nm.all_hosts())
# print(dictionary)
# print(dictionary['scan'][ip]['tcp'])

# print(json_object)
# print(dictionary['scan'][ip]['status'])
# print(dictionary['scan'][ip]['tcp'][0]['state'])
# print(dictionary['scan'][ip]['tcp'][0]['name'])
# print(dictionary['scan'][ip]['tcp'][0]['product'])
# print(dictionary['scan'][ip]['tcp'][0]['version'])

# print("Port\tState\tName\tProduct\t\tVersion")
# for key in ((dictionary['scan'][ip]['tcp']).keys()):
# 	print(f"{key}\t{dictionary['scan'][ip]['tcp'][key]['state']}\t{dictionary['scan'][ip]['tcp'][key]['name']}\t{dictionary['scan'][ip]['tcp'][key]['product']}\t{dictionary['scan'][ip]['tcp'][key]['version']}")
# return dictionary