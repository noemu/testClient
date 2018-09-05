import sys
import binascii
import urllib.request
import urllib
import ssl
import webbrowser
import os
import time

from twisted.internet import reactor
from twisted.python import log
from twisted.internet.protocol import ReconnectingClientFactory

from autobahn.twisted.websocket import WebSocketClientFactory, \
    WebSocketClientProtocol, \
    connectWS

fh = logging.FileHandler('testClient.log')
fh.setLevel(logging.DEBUG)
logger = logging.getLogger('testClient')
logger.addHandler(fh)

def openSearcher(frage,antwort1,antwort2,antwort3):
    new=2
    if os.name == 'nt':
        webbrowser.get(using='windows-default').open("https://www.google.de/search?q=" +urllib.parse.quote_plus(frage+" AND ("+antwort1+" OR "+antwort2+" OR "+antwort3+")"),new=new)
    else:
        webbrowser.get(using='google-chrome').open("https://www.google.de/search?q=" +urllib.parse.quote_plus(frage+" AND ("+antwort1+" OR "+antwort2+" OR "+antwort3+")"),new=new)
    #webbrowser.get(using='google-chrome').open("https://www.google.de/search?q=" +urllib.parse.quote_plus(frage+" AND ("+antwort1+" OR "+antwort2+" OR "+antwort3+")"),new=new)
    #webbrowser.get(using='google-chrome').open("https://www.google.de/search?q=" +urllib.parse.quote_plus(antwort1),new=new)
    #webbrowser.get(using='google-chrome').open("https://www.google.de/search?q=" +urllib.parse.quote_plus(antwort2),new=new)
    #webbrowser.get(using='google-chrome').open("https://www.google.de/search?q=" +urllib.parse.quote_plus(antwort3),new=new)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    webInput = urllib.parse.quote_plus(frage+" "+antwort1+" "+antwort2+" "+antwort3)      
    url = "https://www.google.de/search?q=" + webInput
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    #print(url)
    req = urllib.request.Request(url,None,hdr)
    response = urllib.request.urlopen(req,context=ctx).read().decode('utf-8')
    responseHigh = response
    #for wort in frage.split():
        #responseHigh = responseHigh.replace(wort,'<mark>'+wort+'</mark>')
    for wort in antwort1.split():
        responseHigh = responseHigh.replace(wort,'<mark>'+wort+'</mark>')
    for wort in antwort2.split():
        responseHigh = responseHigh.replace(wort,'<mark>'+wort+'</mark>')
    for wort in antwort3.split():
        responseHigh = responseHigh.replace(wort,'<mark>'+wort+'</mark>')
    file = open('high.html','w', encoding="utf8")
    file.write(responseHigh)
    file.close()    
    urlFIle = 'file://' + os.path.realpath('high.html')
    #if os.name == 'nt':
        #webbrowser.get(using='windows-default').open(urlFIle,new=new)
    #else:
        #webbrowser.get(using='google-chrome').open(urlFIle,new=new)


class EchoClientProtocol(WebSocketClientProtocol):

    def onConnect(self, response):
        logger.info("--------onConnect:Response----------")
        logger.info(response)

    def sendCode(self,code):
        logger.info("--------sendCOde--------------------")
        logger.info(code)
        bin =  binascii.unhexlify(code)
        self.sendMessage(bin,isBinary = True)


    def sendHello(self):
        pl = "0300080d1210303236303032373435383437303435352ad80665794a68624763694f694a53557a49314e694973496d74705a434936496d4577593256694e4459334e444a684e6a4e6c4d546b324e4449784e6a4e684e7a49344e6d526a5a4451795a6a63304d7a597a4e6a596966512e65794a7063334d694f694a6f64485277637a6f764c334e6c593356795a585276613256754c6d6476623264735a53356a623230765932467a61484e6f623363745a4755694c434a68645751694f694a6a59584e6f633268766479316b5a534973496d46316447686664476c745a5349364d54557a4e6a45794e6a45314d79776964584e6c636c39705a434936496c68685244637a5544466b546b786f56315a5053574e51626d703659564a54636d316c516a4d694c434a7a645749694f694a59595551334d3141785a45354d6146645754306c6a55473571656d465355334a745a55497a4969776961574630496a6f784e544d324d5449324d54557a4c434a6c654841694f6a45314d7a59784d6a6b334e544d73496e426f6232356c5832353162574a6c63694936496973304f5445334e7a45334f446b794d7a49694c434a6d61584a6c596d467a5a53493665794a705a47567564476c306157567a496a7037496e426f6232356c496a7062496973304f5445334e7a45334f446b794d7a496958583073496e4e705a3235666157356663484a76646d6c6b5a5849694f694a77614739755a534a3966512e5656547443476c6a7836474d64437644744b5772686f4139724d466736696e63484a66364363626b457a4c576e535a68313442536b5952562d4f4d687054517a5166526a4955676e475839544a64576670346c577553755254386e6f5266424754344962696c4d6f6741424350497653724232312d532d78746a494b567165462d4a6568444871787559704c354b6b4749655a3463345735377264416c69514770462d71507479564c647062416a434550686c6b4b31427446314f353236626966306755704c4273694774774a34685f70477732775338643450795f32455643334a4c74527778594e6e54512d56464d4f45626452567053415658486d58596d57794b6a4446757a696e6c543457666552512d523742595759786578796878794c574b5445507565457a4870446b6c50754653446c6b52345057417a4146325f7332626c5f79622d6c5643454c527376734141774b413a9801663571664b317265304b343a415041393162456b534b424d30674b764b7a326c356c733934364b68786b4a61666f4e4e30466f5663692d444a5a366b4c2d4b44305f5a4353452d6d7a6154757a4c715a546738366b4b6171387542464e59415a6744635650312d4d53436f43796c6f7a51784f6f6c694a6e58326b46537a47304f5f6137623643616e6c67723844696d5a626d774b6f39704a07616e64726f69646a04312e32307206322e31332e307800"
        bin =  binascii.unhexlify(pl)
        self.sendMessage(bin,isBinary = True)

    def onOpen(self):
        self.sendHello()
        self.sendCode('6c01') #GET neue Cash Termine
        self.sendCode('6c01') #GET neue Cash Termine
        self.sendCode('3b01') #GET links für streams
        self.sendCode('5d010801') #First Keep Alive Package

    def popAndCompare(self, a, b):
        compareBytes = bytearray(binascii.unhexlify(b))
        #a = bytearray(pl)
        result = True
        for cb in compareBytes:
            if a[0] == cb:
                del a[0]
            else:
                result = False
        return result

    def pop(self, a, size):
        result = bytearray()
        for index in range(0,size):
            result.append(a[0])
            del a[0]
        return result

    def parseQuest(self, payload):
        pl = bytearray(payload)
        if not self.popAndCompare(pl,'3D01'):
            logger.info("not a question")
            logger.info(payload)
            return
        questNR = 0
        if self.popAndCompare(pl,'08'):
            questNR = self.pop(pl,1)[0]
        else:
            questNR = 12
        if self.popAndCompare(pl,'10'):
            logger.info(pl)
            self.pop(pl,5)
        else:
            logger.info("no 0x10 byte")
            logger.info(pl)
        if self.popAndCompare(pl,'2c'):
            self.pop(pl,2)
        else:
            logger.info("no 0x2c byte")
            logger.info(pl)
        self.popAndCompare(pl,'01')
        if self.popAndCompare(pl,'08'):
            self.pop(pl,2)
        else:
            logger.info("no 0x08 byte")
            logger.info(pl)
        if self.popAndCompare(pl,'12'):
            questLen = self.pop(pl,1)[0]
            quest = self.pop(pl,questLen).decode(encoding="utf-8")
        else:
            logger.info("no questLength id 0x12")
            logger.info(payload)
            return
        if self.popAndCompare(pl,'1a'):
            ans1Len = self.pop(pl,1)[0]
            ans1 = self.pop(pl,ans1Len).decode(encoding="utf-8")
        else:
            logger.info("sth weird 5")
            logger.info(payload)
        if self.popAndCompare(pl,'1a'):
            ans2Len = self.pop(pl,1)[0]
            ans2 = self.pop(pl,ans2Len).decode(encoding="utf-8")
        else:
            logger.info("sth weird 6")
            logger.info(payload)
        if self.popAndCompare(pl,'1a'):
            ans3Len = self.pop(pl,1)[0]
            ans3 = self.pop(pl,ans3Len).decode(encoding="utf-8")
        else:
            logger.info("sth weird 7")
            logger.info(payload)
        print("-----------------------")
        print("-----------------------")
        print(quest)
        print("-----------------------")
        print(ans1)
        print(ans2)
        print(ans3)
        print("-----------------------")
        print("-----------------------")
        openSearcher(quest,ans1,ans2,ans3)

    def onMessage(self, payload, isBinary):
        logger.info("---------Package received-----------")
        logger.info(binascii.hexlify(payload))
        if payload[0] is 61: # erhalten: Frage
            self.parseQuest(payload)            

        if (payload[0] is 94) and (len(payload) > 3): #erhalten: Keep Alive Packet
            #print("send keep alive:")
            newKAPacket = (int.from_bytes(b'\x5d\x01\x08\x00','big')+payload[3]+1).to_bytes(4,byteorder ='big')
            #print(newKAPacket)
            time.sleep(3)
            self.sendCode(binascii.hexlify(newKAPacket))

        if not isBinary:
            print("Text message received: {}".format(payload))
        #reactor.callLater(1, self.react)


class MyClientFactory(WebSocketClientFactory, ReconnectingClientFactory):

    protocol = EchoClientProtocol

    def clientConnectionFailed(self, connector, reason):
        print("Client connection failed .. retrying ..")
        self.retry(connector)

    def clientConnectionLost(self, connector, reason):
        print("Client connection lost .. retrying ..")
        self.retry(connector)


if __name__ == '__main__':

    #openSearcher("was ist der zweit höchster berg der welt","k2","himalja","rocky mauntains")
    #exit()

    log.startLogging(sys.stdout)

    headers = {'Origin': 'http://live-de-prod-eb.tuanguwen.com:80','Sec-WebSocket-Protocol':'default-protocol','Sec-WebSocket-Extensions':''}

    factory = MyClientFactory('ws://live-de-prod-eb.tuanguwen.com:80', headers=headers)

    factory.protocol = EchoClientProtocol

    #amd = EchoClientProtocol()
    #amd.onMessage(binascii.unhexlify('3d01080a10b8aec1a0da2c1a8d01088d321249556e7465722077656c6368657220506c617474656e6669726d612077757264652064617320416c62756d2022507572706c65205261696e2220766572c3b66666656e746c696368743f1a10436f6c756d626961205265636f7264731a145761726e65722042726f732e205265636f7264731a15556e6976657273616c204d757369632047726f757028b0ea0130b4f34c38f8ecc1a0da2c'),True)
    #exit()  
    connectWS(factory)

    reactor.run()
