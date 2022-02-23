import threading
from flask import Flask,render_template
import sniffer
from sniffer import process_packet

app = Flask(__name__)

dataList = []
@app.route("/")
def hello_world():
    # data = threading.Thread(target=sniffer.sniffing,args=('Wi-Fi',))
    # data.start()
    threading.Thread(target=sniffer.sniffing,args=('Wi-Fi',)).start()
    print(f"Return value from main: {sniffer.returnValue}")
    if (sniffer.returnValue==None):
        pass
    else:
        if sniffer.returnValue in dataList:
            pass 
        else:
            dataList.append(sniffer.returnValue)
    print(f"Data from app: {dataList}")

    return render_template('index.html',dataList=dataList)

@app.route("/sniff")
def sniff():
    # data = sniffer.sniffing('Wi-Fi')
    # data = "Okay"
    # print(f"\nData from app: {data}")
    # return render_template('index.html')
    return "<p>this is sniff page</p>"


if __name__ =="__main__":
    app.run(debug=True)