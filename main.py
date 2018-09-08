import sys
import binascii
import time
import logging
import subprocess
import copy

from twisted.internet import reactor,tksupport
from twisted.python import log
from twisted.internet.protocol import ReconnectingClientFactory

from autobahn.twisted.websocket import WebSocketClientFactory, \
    WebSocketClientProtocol, \
    connectWS

fh = logging.FileHandler('testClient.log')
fh.setLevel(logging.INFO)
logger = logging.getLogger('testClient')
logger.setLevel(logging.INFO)
logger.addHandler(fh)



def test(self):
    amd = self.factory.protocol
    amd.onMessage(binascii.unhexlify('3d01080a10b8aec1a0da2c1a8d01088d321249556e7465722077656c6368657220506c617474656e6669726d612077757264652064617320416c62756d2022507572706c65205261696e2220766572c3b66666656e746c696368743f1a10436f6c756d626961205265636f7264731a145761726e65722042726f732e205265636f7264731a15556e6976657273616c204d757369632047726f757028b0ea0130b4f34c38f8ecc1a0da2c'),True)
    amd.onMessage(binascii.unhexlify('3d0108011088cdbec9da2c1a33089c32121745696e205066657264206861742076696572202e2e2e3f1a0441726d651a0853636877656966651a054265696e6530c6df2f38c88bbfc9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080110c8cdf9d8da2c1a5108a832122a4d69742077656c6368656d205765726b7a6575672061726265697465742065696e20467269736575723f1a065363686572651a074cc3b66666656c1a0f53636872617562656e7a696568657230ebdc2d38888cfad8da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080210b8b1c2c9da2c1a53089d32123944696520436c656d656e74696e652068617420c3a475c39f65726c69636820676577c3b6686e6c69636820646965204661726265202e2e2e3f1a04426c61751a064f72616e67651a05576569c39f3096c03338f8efc2c9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080210f08dfcd8da2c1a6608a93212484b65696e20537465726e7a65696368656e2064657320696e204575726f70612067656272c3a47563686c696368656e20546965726b7265697365732069737420646572202e2e2e3f1a0553746965721a08536b6f7270696f6e1a0644726163686530a29d3038b0ccfcd8da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080310d0e5fed8da2c1a4b08aa32122c4b6ec3a4636b6562726f7420756e64204bc3b6747462756c6c6172207374616d6d656e20617573202e2e2e3f1a074974616c69656e1a05506f6c656e1a08536368776564656e30bbf4323890a4ffd8da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080310f8e9c4c9da2c1a3c089e321222576f20777572646520646572202254726162616e74222070726f64757a696572743f1a034444521a034252441a0944c3a46e656d61726b30eefa3538b8a8c5c9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080410f0b6c8c9da2c1a73089f32124e496e2077656c6368656d204c616e642064657220457264652077757264656e20646965206772c3b6c39f74656e2054656d70657261747572756e746572736368696564652067656d657373656e3f1a0b446575747363686c616e641a075370616e69656e1a08527573736c616e643086c83938b0f5c8c9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080410f8a581d9da2c1a5708ab321232496e2077656c63686572205374616474206861742064696520566f6c6b73776167656e20414720696872656e205369747a3f1a095374757474676172741a084dc3bc6e6368656e1a09576f6c66736275726730b3ba3538b8e481d9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d0108051080f9ccc9da2c1a6808a032124d45696e20506c616e657420756e736572657320536f6e6e656e73797374656d732065726c6974742065696e6520537461747573c3a46e646572756e672c2077656c63686572207761722065733f1a05506c75746f1a074a7570697465721a044d61727328904e30ce893e38c0b7cdc9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080510f89686d9da2c1a4e08ac32123757616e6e20737461727465746520646173206572737465206b6f6d6d65727a69656c6c6520506173736167696572666c75677a6575673f1a04313934301a04313931341a043139363128904e30e2ab3a38b8d586d9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080610c0f389d9da2c1a5e08ad321236576f20626566616e64207369636820646173206568656d616c69676520224bc3b66e69677265696368204162657373696e69656e223f1a084d6f73616d62696b1a0b4d6175726574616e69656e1a0ac3847468696f7069656e28a09c0130f2873e3880b28ad9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080610c8d8cfc9da2c1a890108a13212504d6172696c796e204d6f6e726f65202d20776572206b656e6e7420736965206e696368742120446f6368207765722077617220696872652064657574736368652053796e6368726f6e7374696d6d653f1a0f4d6172676f74204c656f6e686172641a1042726967697474652047726f7468756d1a0f53696d6f6e6520427261686d616e6e28a09c013086e940388897d0c9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d0108071088d38cd9da2c1a5208ae321241576965207669656c6520656967656e7374c3a46e64696765204b6c61766965726b6f6e7a65727465206b6f6d706f6e696572746520572e412e204d6f7a6172743f1a0232331a0231381a02333028904e30eae44038c8918dd9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080710e0c7d2c9da2c1a4e08a2321231496e2077656c636865722048c3b668652068c3a46e677420646572204b6f7262206265696d204261736b657462616c6c3f1a06332c3230206d1a06332c3035206d1a06322c3830206d28904e309dd44338a086d3c9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d0108081080ded5c9da2c1a6f08a3321257576965207669656c65205374656c6c656e207a7769736368656e204b6f706620756e642057697262656c73c3a4756c6520646573204d656e736368656e20686162656e206b65696e652042616e64736368656962656e3f1a044e756c6c1a0546c3bc6e661a045a77656928a09c0130beea4638c09cd6c9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080810c0e18fd9da2c1a5c08af321222446572206772c3b6c39f746520536565206465722057656c7420697374202e2e2e3f1a0d446572204261696b616c7365651a0f44657220566963746f7269617365651a13446173204b617370697363686573204d65657228a09c0130f2f3433880a090d9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d0108091088c192d9da2c1a7108b032124557656c6368657320426572676d61737369762074727567206c616e6765205a6569742064656e204e616d656e2065696e65732064657574736368656e204b6169736572733f1a095a7567737069747a651a0e4b696c696d616e6473636861726f1a0a48696e64756b7573636828a09c0130cad14638c8ff92d9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080910f083d9c9da2c1a7c08a43212514d6f727068696e2069737420616c73205363686d65727a6d697474656c2062656b616e6e742c20646f6368206175732077656c636865722050666c616e7a652077697264206573206765776f6e6e656e3f1a0b48616e6670666c616e7a651a0a5363686c61666d6f686e1a0b466c696567656e70696c7a28a09c0130cd964a38b0c2d9c9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080a10a0ebdbc9da2c1a870108a532125957656c636865722064657220666f6c67656e64656e204265677269666665207769726420696e204672c3bc687761726e73797374656d652066c3bc72204572642d20756e6420536565626562656e2076657277656e6465743f1a0b536569736d6f67726170681a0b54656e73696f6d657465721a0d4765696765727ac3a4686c657228b0ea0130adfd4c38e0a9dcc9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080a10b8aec1a0da2c1a8d01088d321249556e7465722077656c6368657220506c617474656e6669726d612077757264652064617320416c62756d2022507572706c65205261696e2220766572c3b66666656e746c696368743f1a10436f6c756d626961205265636f7264731a145761726e65722042726f732e205265636f7264731a15556e6976657273616c204d757369632047726f757028b0ea0130b4f34c38f8ecc1a0da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080a10e0f194d9da2c1a7e08b132124e57657220747269747420696d206c65747a74656e205374726569636820696e2057696c68656c6d2042757363682773204d617820756e64204d6f7269747a20696e20457273636865696e756e673f1a0b4261756572204d65636b651a0b576974776520426f6c74651a0f5363686e65696465722042c3b6636b28b0ea0130b2864938a0b095d9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080b10908be1c9da2c1a830108a632124d57656c63686520506572736f6e20776172206e6965205072c3a4736964656e74206f646572205072c3a4736964656e74696e206465732044657574736368656e2042756e646573746167733f201a0e526974612053c3bc73736d7574681a0e48656c6d7574205363686d6964741a0f4e6f7262657274204c616d6d6572742898fc0630e59d5238d0c9e1c9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d01080b10c8ed98d9da2c1a5b08b232123357656c6368652053696e6e657374c3a475736368756e672077697264206265777573737420686572766f726765727566656e3f1a0853796e6f7074696b1a0d54726f6d70652d4c276f65696c1a0853656d696f74696b28c8ec0630e2814d3888ac99d9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d0110d0bebbc9da2c1a33089b321222576965207669656c65205374756e64656e20686162656e207a77656920546167653f1a0232341a0234381a023732200130ded02c3890fdbbc9da2c'),True)
    #amd.onMessage(binascii.unhexlify('3d0110e0cef6d8da2c1a3f08a73212244b65696e652048756665206861742077656c63686573206469657365722054696572653f1a0550666572641a075363687765696e1a0448756e64200130dbe12a38a08df7d8da2c'),True)
    exit() 


class MyClientFactory(WebSocketClientFactory, ReconnectingClientFactory):
    

    def clientConnectionFailed(self, connector, reason):
        print("Client connection failed .. retrying ..")
        self.retry(connector)

    def clientConnectionLost(self, connector, reason):
        print("Client connection lost .. retrying ..")
        self.retry(connector)

class EchoClientProtocol(WebSocketClientProtocol):
   
    def onConnect(self, response):
        logger.info("--------onConnect:Response----------")
        logger.info(response)

    def sendCode(self,code):
        logger.info("--------sendCode--------------------")
        logger.info(code)
        bin =  binascii.unhexlify(code)
        self.sendMessage(bin,isBinary = True)


    def sendHello(self):
        pl = "0300080d1210303236303032373435383437303435352ad80665794a68624763694f694a53557a49314e694973496d74705a434936496d4577593256694e4459334e444a684e6a4e6c4d546b324e4449784e6a4e684e7a49344e6d526a5a4451795a6a63304d7a597a4e6a596966512e65794a7063334d694f694a6f64485277637a6f764c334e6c593356795a585276613256754c6d6476623264735a53356a623230765932467a61484e6f623363745a4755694c434a68645751694f694a6a59584e6f633268766479316b5a534973496d46316447686664476c745a5349364d54557a4e6a45794e6a45314d79776964584e6c636c39705a434936496c68685244637a5544466b546b786f56315a5053574e51626d703659564a54636d316c516a4d694c434a7a645749694f694a59595551334d3141785a45354d6146645754306c6a55473571656d465355334a745a55497a4969776961574630496a6f784e544d324d5449324d54557a4c434a6c654841694f6a45314d7a59784d6a6b334e544d73496e426f6232356c5832353162574a6c63694936496973304f5445334e7a45334f446b794d7a49694c434a6d61584a6c596d467a5a53493665794a705a47567564476c306157567a496a7037496e426f6232356c496a7062496973304f5445334e7a45334f446b794d7a496958583073496e4e705a3235666157356663484a76646d6c6b5a5849694f694a77614739755a534a3966512e5656547443476c6a7836474d64437644744b5772686f4139724d466736696e63484a66364363626b457a4c576e535a68313442536b5952562d4f4d687054517a5166526a4955676e475839544a64576670346c577553755254386e6f5266424754344962696c4d6f6741424350497653724232312d532d78746a494b567165462d4a6568444871787559704c354b6b4749655a3463345735377264416c69514770462d71507479564c647062416a434550686c6b4b31427446314f353236626966306755704c4273694774774a34685f70477732775338643450795f32455643334a4c74527778594e6e54512d56464d4f45626452567053415658486d58596d57794b6a4446757a696e6c543457666552512d523742595759786578796878794c574b5445507565457a4870446b6c50754653446c6b52345057417a4146325f7332626c5f79622d6c5643454c527376734141774b413a9801663571664b317265304b343a415041393162456b534b424d30674b764b7a326c356c733934364b68786b4a61666f4e4e30466f5663692d444a5a366b4c2d4b44305f5a4353452d6d7a6154757a4c715a546738366b4b6171387542464e59415a6744635650312d4d53436f43796c6f7a51784f6f6c694a6e58326b46537a47304f5f6137623643616e6c67723844696d5a626d774b6f39704a07616e64726f69646a04312e32307206322e31332e307800"
        bin =  binascii.unhexlify(pl)
        self.sendMessage(bin,isBinary = True)

    def onOpen(self):
        self.sendCode('0300080d1210346433663337393432666533643439381a0974384e717a2d766e67222036616265393536613431383430666330666465653665376563646364663839313a980166516a7a373948316454633a4150413931624630307642713644645451334f65634b70695a4d79546d523038647475496564396634636771346f6c2d304b50776b5a516752615a72566270716d664d45634f6f36355256746f47485547616f5157685373526e36346e79395039486e34682d6e4c45484633386c584e4a5233545971316146594b54487a43714a4f325f4e563357386832434a07616e64726f69646a04312e32307206322e31332e307800')
        self.sendCode('6c01') #GET neue Cash Termine
        self.sendCode('6c01') #GET neue Cash Termine
        self.sendCode('3b01') #GET links für streams
        self.sendCode('5d010801') #First Keep Alive Package
        #reactor.callLater(1,self.onMessage,binascii.unhexlify('3d0108011088cdbec9da2c1a33089c32121745696e205066657264206861742076696572202e2e2e3f1a0441726d651a0853636877656966651a054265696e6530c6df2f38c88bbfc9da2c'),True)
        #reactor.callLater(14,self.onMessage,binascii.unhexlify('3d0110e0cef6d8da2c1a3f08a73212244b65696e652048756665206861742077656c63686573206469657365722054696572653f1a0550666572641a075363687765696e1a0448756e64200130dbe12a38a08df7d8da2c'),True)
        


    def onMessage(self, payload, isBinary):
        logger.info("---------Package received-----------")
        logger.info(binascii.hexlify(payload))
        if payload[0] is 61: # erhalten: Frage
            logger.info("----Frage erhalten----")
            subprocess.Popen("python questParser.py "+str(binascii.hexlify(payload),'utf-8'))
           

        if (payload[0] is 94) and (len(payload) > 3): #erhalten: Keep Alive Packet
            logger.info("---sende Keep Alive-----")
            #print("send keep alive:")
            newKAPacket = (int.from_bytes(b'\x5d\x01\x08\x00','big')+payload[3]+1).to_bytes(4,byteorder ='big')
            #print(newKAPacket)
            time.sleep(3)
            self.sendCode(binascii.hexlify(newKAPacket))

        if not isBinary:
            print("Text message received: {}".format(payload))
        
        #reactor.callLater(1, self.react)




     
if __name__ == '__main__':

    logger.info("---------start session----------")

    headers = {'Origin': 'http://live-de-prod-eb.tuanguwen.com:80','Sec-WebSocket-Protocol':'default-protocol','Sec-WebSocket-Extensions':''}
    factory = MyClientFactory('ws://live-de-prod-eb.tuanguwen.com:80', headers=headers)
    factory.protocol = EchoClientProtocol
    connectWS(factory)

    reactor.run()



    


