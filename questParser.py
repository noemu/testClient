import logging
import tkinter as tk
import urllib.request
import urllib
import ssl
import webbrowser
import re
import numpy as np
import matplotlib.pyplot as plt
import os
import binascii
import sys

fh = logging.FileHandler('parser.log')
fh.setLevel(logging.INFO)
logger = logging.getLogger('testClient')
logger.setLevel(logging.INFO)
logger.addHandler(fh)

def countWords(text,words):
    textl = text.lower()
    counter1 = 0
    for wordA in words.split():
        index = textl.find(wordA.lower())  
        while(index is not -1):
            counter1+=1
            index = textl.find(wordA.lower(),index+1)
    return counter1

def countEachWord(text,words):
    textl = text.lower()
    counter1 = 1.0
    result = {}
    for wordA in words.split():
        result[wordA] = 0.0
    for wordA in words.split():
        index = textl.find(wordA.lower())  
        while(index is not -1):
            result[wordA]+=1
            counter1+=1
            index = textl.find(wordA.lower(),index+1)

    for wordA in words.split():
        result[wordA] /= counter1
    return result

def openSearcher(frage,antwort1,antwort2,antwort3,root):
    pattern=['["?!]+']
    frage = re.sub(r'[^\w\s]','',frage)
    antwort1 = re.sub(r'[^\w\s]','',antwort1)
    antwort2 = re.sub(r'[^\w\s]','',antwort2)
    antwort3 = re.sub(r'[^\w\s]','',antwort3)    

    new=2
    if os.name == 'nt':
        webbrowser.get(using='windows-default').open("https://www.google.de/search?q=" +urllib.parse.quote_plus(frage+" "+antwort1+" OR "+antwort2+" OR "+antwort3+""),new=new)
    else:
        webbrowser.get(using='google-chrome').open("https://www.google.de/search?q=" +urllib.parse.quote_plus(frage+" "+antwort1+" OR "+antwort2+" OR "+antwort3+""),new=new)
    #webbrowser.get(using='google-chrome').open("https://www.google.de/search?q=" +urllib.parse.quote_plus(frage+" AND ("+antwort1+" OR "+antwort2+" OR "+antwort3+")"),new=new)
    #webbrowser.get(using='google-chrome').open("https://www.google.de/search?q=" +urllib.parse.quote_plus(antwort1),new=new)
    #webbrowser.get(using='google-chrome').open("https://www.google.de/search?q=" +urllib.parse.quote_plus(antwort2),new=new)
    #webbrowser.get(using='google-chrome').open("https://www.google.de/search?q=" +urllib.parse.quote_plus(antwort3),new=new)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    webInput = urllib.parse.quote_plus(frage)      
    url = "https://www.google.de/search?q=" + webInput
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    req = urllib.request.Request(url,None,hdr)
    response = urllib.request.urlopen(req,context=ctx).read().decode('utf-8')

    counter1 = countWords(response,antwort1)
    counter2 = countWords(response,antwort2)
    counter3 = countWords(response,antwort3)

    print("----answer in question-----")
    print(antwort1+" : "+str(100.0*counter1/(counter1+counter2+counter3+1))+"%")
    print(antwort2+" : "+str(100.0*counter2/(counter1+counter2+counter3+1))+"%")
    print(antwort3+" : "+str(100.0*counter3/(counter1+counter2+counter3+1))+"%")
  
    webInput = urllib.parse.quote_plus(antwort1)
    url = "https://www.google.de/search?q=" + webInput
    req = urllib.request.Request(url,None,hdr)
    response = urllib.request.urlopen(req,context=ctx).read().decode('utf-8')
    counterQ1=countEachWord(response,frage)

    webInput = urllib.parse.quote_plus(antwort2)
    url = "https://www.google.de/search?q=" + webInput
    req = urllib.request.Request(url,None,hdr)
    response = urllib.request.urlopen(req,context=ctx).read().decode('utf-8')
    counterQ2=countEachWord(response,frage)

    webInput = urllib.parse.quote_plus(antwort3)
    url = "https://www.google.de/search?q=" + webInput
    req = urllib.request.Request(url,None,hdr)
    response = urllib.request.urlopen(req,context=ctx).read().decode('utf-8')
    counterQ3=countEachWord(response,frage)  

    print("----answer in question-----")
    sumC = counter1+counter2+counter3
    printStatistics(frage,antwort1,counter1,sumC,counterQ1)
    printStatistics(frage,antwort2,counter2,sumC,counterQ2)
    printStatistics(frage,antwort3,counter3,sumC,counterQ3)

    plt.close()
    plt.subplot(2, 1, 1)
    answers = (antwort3,antwort2,antwort1)
    y_pos = np.arange(len(answers))
    values = np.array([counter3,counter2,counter1])
    plt.barh(y_pos,values,color=('blue','green','red'))
    plt.yticks(y_pos,answers)
    #plt.gcf().subplots_adjust(left=0.50)
    
    plt.subplot(2, 1, 2)

    index = np.arange(len(counterQ1))
    bar_width = 0.1

    plt.bar(index,list(counterQ1.values()),bar_width,color="red")
    plt.bar(index+bar_width,list(counterQ2.values()),bar_width,color="green")
    plt.bar(index+bar_width*2.0,list(counterQ3.values()),bar_width,color="blue")
    plt.xticks(np.arange(len(counterQ1)),list(counterQ1.keys()))

    plt.tight_layout()
    plt.show()
    root.destroy()
    exit()

def printStatistics(frage,antwort,count,sumC,inverse):
    text = antwort+str(" %.2f \t:"%(100*count/(sumC+1)))
    for word in frage.split():
        text += str("%s:%.2f "%(word,100*inverse[word]))
    print(text)

def popAndCompare(a, b):
    compareBytes = bytearray(binascii.unhexlify(b))
    #a = bytearray(pl)
    result = True
    for cb in compareBytes:
        if a[0] == cb:
            del a[0]
        else:
            result = False
    return result

def pop(a, size):
    result = bytearray()
    for index in range(0,size):
        result.append(a[0])
        del a[0]
    return result

def parseQuest(payload):
    pl = bytearray(payload)
    print(pl[0])
    print(pl)
    if not popAndCompare(pl,'3D01'):
        logger.info("not a question")
        logger.info(payload)
        return
    questNR = 0
    if popAndCompare(pl,'08'):
        questNR = pop(pl,1)[0]
    else:
        questNR = 12
    if popAndCompare(pl,'10'):
        logger.info(pl)
        pop(pl,5)
    else:
        logger.info("no 0x10 byte")
        logger.info(pl)
    if popAndCompare(pl,'2c'):
        pop(pl,2)
    else:
        logger.info("no 0x2c byte")
        logger.info(pl)
    popAndCompare(pl,'01')
    if popAndCompare(pl,'08'):
        pop(pl,2)
    else:
        logger.info("no 0x08 byte")
        logger.info(pl)
    if popAndCompare(pl,'12'):
        questLen = pop(pl,1)[0]
        quest = pop(pl,questLen).decode(encoding="utf-8")
    else:
        logger.info("no questLength id 0x12")
        logger.info(payload)
        return
    if popAndCompare(pl,'1a'):
        ans1Len = pop(pl,1)[0]
        ans1 = pop(pl,ans1Len).decode(encoding="utf-8")
    else:
        logger.info("sth weird 5")
        logger.info(payload)
    if popAndCompare(pl,'1a'):
        ans2Len = pop(pl,1)[0]
        ans2 = pop(pl,ans2Len).decode(encoding="utf-8")
    else:
        logger.info("sth weird 6")
        logger.info(payload)
    if popAndCompare(pl,'1a'):
        ans3Len = pop(pl,1)[0]
        ans3 = pop(pl,ans3Len).decode(encoding="utf-8")
    else:
        logger.info("sth weird 7")
        logger.info(payload)
    print("-----------------------")
    print("-----------------------")
    print(quest)
    print("-----------------------")
    selector(quest,ans1,ans2,ans3)

class selector(object):
    questArray = []
    questState = {}

    buttonDic = {}
    a1 = ""
    a2 = ""
    a3 = ""
    def __init__(self,quest,a1,a2,a3):
        self.root = tk.Tk()
        self.root.title("Select KeyWords")
        self.frame = tk.Frame(self.root)
        self.setNewQuest(quest,a1,a2,a3)
        self.root.mainloop()

    def setNewQuest(self,frage,a1,a2,a3):
        self.frame.destroy()
        self.frame = tk.Frame(self.root)
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.questArray = frage.split()
        id = 0
        for word in self.questArray:
            self.questState[word] = False
            button = tk.Button(self.frame, text=word, width=15, command=lambda id = word: self.click(id))
            button.pack(side=tk.LEFT)
            self.buttonDic[word] = button
            id+=1
        button = tk.Button(self.frame, text="gogo Gadget", width=25, command=self.go)
        button.pack(side=tk.BOTTOM)
        self.frame.pack()
        self.root.lift()

    def click(self,id):
        self.questState[id] = not self.questState[id]
        if self.questState[id]:
            self.buttonDic[id].config(fg="red")
            self.buttonDic[id].config(highlightbackground="red")
        else:
            self.buttonDic[id].config(fg="black")
            self.buttonDic[id].config(highlightbackground="white")

    def go(self):
        frage = ""
        for word in self.questArray:
            if self.questState[word]:
                frage = frage+" "+word
        openSearcher(frage,self.a1,self.a2,self.a3,self.root)

if __name__ == '__main__':
    print("a"+str(sys.argv[1])+"b")
    parseQuest(binascii.unhexlify(sys.argv[1]))