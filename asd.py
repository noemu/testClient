import sys
import binascii

from twisted.internet import reactor
from twisted.python import log

from autobahn.twisted.websocket import WebSocketClientFactory, \
    WebSocketClientProtocol, \
    connectWS


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

    def onMessage(self, payload, isBinary):
        if payload[0] is 61:
            print(payload)
        if (payload[0] is 94) and (len(payload) > 3):
            print("send keep alive:")
            print(b'\x5d\x01\x08\x00'+payload[3]+b'\x01')
            self.sendCode(b'\x5d\x01\x08\x00'+payload[3]+b'\x01')
        print(payload)
        if not isBinary:
            print("Text message received: {}".format(payload))
        #reactor.callLater(1, self.react)


if __name__ == '__main__':

    log.startLogging(sys.stdout)

    headers = {'Origin': 'http://live-de-prod-eb.tuanguwen.com:80','Sec-WebSocket-Protocol':'default-protocol','Sec-WebSocket-Extensions':''}

    factory = WebSocketClientFactory('ws://live-de-prod-eb.tuanguwen.com:80', headers=headers)
    factory.protocol = EchoClientProtocol
    connectWS(factory)

    reactor.run()
