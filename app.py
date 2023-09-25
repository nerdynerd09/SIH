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
from initialMail import initialReportGenerator
from pysharktest import packetCapture

app = Flask(__name__)
app.config['SECRET_KEY'] = "BROWNRING"
socket = SocketIO(app)

i=0

urlList = []
capturedPackets = []

@app.route("/")
@app.route("/dashboard")
def hello_world():
    # networkIPs,networkMAC,vendor,currentIP,currentMAC = nmapper()

    # Working
    dictionary,ipList,currentIP,currentMAC,networkIPs,networkMAC,vendor,cveList = portScanner()    
    # print("Port scanning done.\n")
    threading.Thread(target=sniffer.sniffing,args=('eth0',),daemon=False).start()
    # threading.Thread(target=arpSniff,args=('eth0',),daemon=True).start()
    # threading.Thread(target=dosDetection,daemon=True).start()
    # initialReportGenerator(networkIPs,networkMAC,vendor,currentIP,currentMAC,cveList)
    # return render_template('index.html',dictionary=dictionary,ipList=ipList,currentMAC=currentMAC,currentIP=currentIP,networkIPs=networkIPs,networkMAC=networkMAC,vendor=vendor,cveList=cveList)
    threading.Thread(target=packetCapture).start()
    return render_template('index.html',dictionary=dictionary,ipList=ipList,currentMAC=currentMAC,currentIP=currentIP,networkIPs=networkIPs,networkMAC=networkMAC,vendor=vendor,cveList=cveList)

    # return render_template('index.html')    

    # return render_template('wireshark.html')    
    
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

@app.route("/datapackets", methods = ['POST'])
def capturePacketsFn():
    data = request.form
    d = dict(data)
    capturedSrc = d.get('src')
    capturedDst = d.get('dst')
    capturedLayer = d.get('layer')

    # packetList = d.get('packetList')
    # print(f"SRC: {capturedSrc}\tDST: {capturedDst}\tLayer: {capturedLayer}")
    capturedPackets.append([capturedSrc,capturedDst,capturedLayer])
    # print(f"CapturedPacket: {capturedPackets}")
    socket.emit("capturedPackets",{'packets':capturedPackets})      
    return jsonify(isError = False,
                    message = "Success",
                    statusCode = 200,
                    data = data), 200

@app.route("/attackDetection", methods = ['POST'])
def attackDetectionFn():
    data = request.form
    d = dict(data)
    alertType = d.get('alertType')
    attackType = d.get('attackType')
    # print(f"AlertType: {alertType}")

    
    # if attackType == "ddos":
    #     socket.emit("ddos");

    if (d.get('alertType')=="syn"):
        socket.emit("synattack")

    if(d.get('alertType')=="icmp"):
        socket.emit("icmpattack")
    
    # if attackType == "arp":
    #     socket.emit("arp")
    return jsonify(isError= False,
                    message= "Success",
                    statusCode= 200,
                    data= data), 200

@app.route("/arpDetection", methods = ['POST'])
def arpAttackDetectionFn():
    data = request.form
    d = dict(data)
    attackType = d.get('attackType')

    if attackType == "arp":
        socket.emit("arp")
    return jsonify(isError = False,
                    message = "Success",
                    statusCode = 200,
                    data = data), 200

    

# @app.route("/nmapper")
# def nmap():
#     capturePackets = packetCapture()
#     return render_template('nmapscannerdisplay.html',capturePackets=capturePackets)



if __name__ =="__main__":
    socket.run(app,debug=False)
