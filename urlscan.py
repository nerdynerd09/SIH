import requests

uncleanIndex = 0
def urlScan(url):
	global uncleanIndex
	data = requests.get('https://www.virustotal.com/api/v3/domains/'+url,headers={'x-apikey':'bb64ef17ec6332feded9ce796fb84883f056eaa55cd65cf2274d9e03cb51c424'}).json()
	for key in ((data['data']['attributes']['last_analysis_results']).keys()):
	    # print(data['data']['attributes']['last_analysis_results'][key]['result'])
	    if (data['data']['attributes']['last_analysis_results'][key]['result']) != "clean":
	    	uncleanIndex +=1 
	print(f"Danger Score: {uncleanIndex}")
	return uncleanIndex
