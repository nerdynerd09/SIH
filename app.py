from pstats import SortKey
import threading
from flask import Flask, jsonify,render_template, request
from flask_socketio import SocketIO
import sniffer
from sniffer import process_packet,sniffing
from urlscan import urlScan
from nmapscanner import portScanner,nmapper
from attackAnalysis import dosDetection
from arpDetection import arpSniff
from testtext import testFunc

app = Flask(__name__)
app.config['SECRET_KEY'] = "BROWNRING"
socket = SocketIO(app)

i=0

urlList = []


@app.route("/")
@app.route("/dashboard")
def hello_world():
    # networkIPs,networkMAC,vendor,currentIP,currentMAC = nmapper()

    # Working
    dictionary,ipList,currentIP,currentMAC,networkIPs,networkMAC,vendor = portScanner()    
    threading.Thread(target=sniffer.sniffing,args=('eth0',),daemon=True).start()
    threading.Thread(target=arpSniff,args=('eth0',),daemon=True).start()
    threading.Thread(target=dosDetection,daemon=True).start()
    return render_template('index.html',dictionary=dictionary,ipList=ipList,currentMAC=currentMAC,currentIP=currentIP,networkIPs=networkIPs,networkMAC=networkMAC,vendor=vendor)


    # return render_template('index.html')
    
    # alertString = dosDetection()

    # alertString = testFunc()

    # print(alertString)
    # dosDetection()
    # return render_template('index.html')
    # return render_template('index.html',alertString=alertString)

    # return render_template('index.html',networkIPs=networkIPs,networkMAC=networkMAC,vendor=vendor,currentIP=currentIP,currentMAC=currentMAC)

@app.route("/addUrl", methods = ['POST'])
def addUrlFn():
    data = request.form
    d = dict(data)
    url = d.get('url')
    urlScore = d.get('urlScore')
    urlList.append([url,urlScore])
    print(f"UrlList: {urlList}")
    socket.emit("urlAdded",{"list" : urlList});
    return jsonify(isError= False,
                    message= "Success",
                    statusCode= 200,
                    data= data), 200


@app.route("/attackDetection", methods = ['POST'])
def attackDetectionFn():
    data = request.form
    d = dict(data)
    attackType = d.get('attackType')
    if attackType == "ddos":
        socket.emit("ddos");
    elif attackType == "arp":
        socket.emit("arp")
    return jsonify(isError= False,
                    message= "Success",
                    statusCode= 200,
                    data= data), 200

# @app.route("/arpDetection", methods = ['POST'])
# def addUrlFn():
#     data = request.form
#     d = dict(data)
#     arp = d.get('arpResult')
#     # arpList.append([arpResult])
#     # print(f"ArpResult: {arpList}")
#     socket.emit("arpDetecting",{"arpResult" : arp});
#     return jsonify(isError= False,
#                     message= "Success",
#                     statusCode= 200,
#                     data= data), 200


@app.route("/nmapper")
def nmap():
    # networkIPs,networkMAC,vendor,currentIP,currentMAC = nmapper()
    dictionary,ipList,currentIP,currentMAC = portScanner()
    return render_template('nmapscannerdisplay.html',dictionary=dictionary,ipList=ipList,currentMAC=currentMAC,currentIP=currentIP)
    # return render_template('nmapscannerdisplay.html',networkIPs=networkIPs,networkMAC=networkMAC,vendor=vendor,currentIP=currentIP,currentMAC=currentMAC)

if __name__ =="__main__":
    socket.run(app,debug=True)