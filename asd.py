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

from autobahn.twisted.websocket import WebSocketClientFactory, \
    WebSocketClientProtocol, \
    connectWS

def openSearcher(frage,antwort1,antwort2,antwort3):
    new=2
    #webbrowser.get(using='google-chrome').open("https://www.google.de/search?q=" +urllib.parse.quote_plus(frage),new=new)
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
    print(url)
    req = urllib.request.Request(url,None,hdr)
    response = urllib.request.urlopen(req,context=ctx).read().decode('utf-8')
    responseHigh = response
    for wort in frage.split():
        responseHigh = responseHigh.replace(wort,'<mark>'+wort+'</mark>')
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
    if os.name == 'nt':
        webbrowser.get(using='windows-default').open(urlFIle,new=new)
    else:
        webbrowser.get(using='google-chrome').open(urlFIle,new=new)


class EchoClientProtocol(WebSocketClientProtocol):

    def onConnect(self, response):
        print(response)

    def sendCode(self,code):
        bin =  binascii.unhexlify(code)
        self.sendMessage(bin,isBinary = True)


    def sendHello(self):
        pl = "0300080d1210346433663337393432666533643439381a096747433662614669672220613530353365393430313530623564353561303930653439616638643538653632d7014541415a41665a41694c70315a416742414250526f3059564375494f32515065685a43664567616f5954437748654f6a776a4b5a415a416857634e554e346c5a41646664454b42624c58514f5638644e62684555727561615134476639585a416455336a5076477871326a77477564633239546e3569387473425a43535a4261553349646c305a42326b7050477276664b42495a4256473368385959727574315237544262616244386f69444d316d4b663361717756486a445747494139556e58496d78335357487254464c796633355456515a445a443aae01635970794b31327456376b3a41504139316246346d7474523730583856474d754475494d4d52534648696865507369564e51476f72793048444157416d5a7657334c786d3067396c4b4564726577554459424b572d4f6751436167426c7459747a7459636b4350344a31734b4c4c726b6d553554647471486c4e783978567270725861345856365a564b643651705a774542397a32755a51494938556a5345785569764941317758374d486655414a07616e64726f69646a04312e32307206322e31332e307801"
        bin =  binascii.unhexlify(pl)
        self.sendMessage(bin,isBinary = True)

    def onOpen(self):
        print()
        self.sendHello()
        self.sendCode('6c01') #GET neue Cash Termine
        self.sendCode('6c01') #GET neue Cash Termine
        self.sendCode('3b01') #GET links für streams
        self.sendCode('5d010801') #GET links für streams

    def popAndCompare(self, a, b):
        compareBytes = bytearray(binascii.unhexlify(b))
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
        if not self.popAndCompare(self,pl,'3D01'):
            print("not a question")
            print(payload)
            exit()
        questNR = 0
        if self.popAndCompare(self,pl,'08'):
            questNR = self.pop(self,pl,1)[0]
        else:
            questNR = 12
        if self.popAndCompare(self,pl,'10'):
            print(pl)
            self.pop(self,pl,5)
        else:
            print("sth weird 1")
            print(pl)
        if self.popAndCompare(self,pl,'2c'):
            self.pop(self,pl,2)
        else:
            print("sth weird 2")
            print(pl)
        if self.popAndCompare(self,pl,'08'):
            self.pop(self,pl,2)
        else:
            print("sth weird 3")
            print(pl)
        if self.popAndCompare(self,pl,'12'):
            questLen = self.pop(self,pl,1)[0]
            quest = self.pop(self,pl,questLen).decode(encoding="utf-8")
        else:
            print("sth weird 4")
            print(payload)
        if self.popAndCompare(self,pl,'1a'):
            ans1Len = self.pop(self,pl,1)[0]
            ans1 = self.pop(self,pl,ans1Len).decode(encoding="utf-8")
        else:
            print("sth weird 5")
            print(payload)
        if self.popAndCompare(self,pl,'1a'):
            ans2Len = self.pop(self,pl,1)[0]
            ans2 = self.pop(self,pl,ans2Len).decode(encoding="utf-8")
        else:
            print("sth weird 6")
            print(payload)
        if self.popAndCompare(self,pl,'1a'):
            ans3Len = self.pop(self,pl,1)[0]
            ans3 = self.pop(self,pl,ans3Len).decode(encoding="utf-8")
        else:
            print("sth weird 7")
            print(payload)
        openSearcher(quest,ans1,ans2,ans3)

    def onMessage(self, payload, isBinary):
        print(payload)
        if payload[0] is 61: # erhalten: Frage
            self.parseQuest(self,payload)            

        if (payload[0] is 94) and (len(payload) > 3): #erhalten: Keep Alive Packet
            print("send keep alive:")
            newKAPacket = (int.from_bytes(b'\x5d\x01\x08\x00','big')+payload[3]+1).to_bytes(4,byteorder ='big')
            print(newKAPacket)
            time.sleep(3)
            self.sendCode(binascii.hexlify(newKAPacket))

        if not isBinary:
            print("Text message received: {}".format(payload))
        #reactor.callLater(1, self.react)


if __name__ == '__main__':

    #openSearcher("was ist der zweit höchster berg der welt","k2","himalja","rocky mauntains")
    #exit()

    log.startLogging(sys.stdout)

    headers = {'Origin': 'http://live-de-prod-eb.tuanguwen.com:80','Sec-WebSocket-Protocol':'default-protocol','Sec-WebSocket-Extensions':''}

    factory = WebSocketClientFactory('ws://live-de-prod-eb.tuanguwen.com:80', headers=headers)
    factory.protocol = EchoClientProtocol
    connectWS(factory)

    reactor.run()
