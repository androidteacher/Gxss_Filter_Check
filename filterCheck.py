import requests
import sys
lines = []
testList = []

with open("bypass.txt","r") as bypass:
    lines = bypass.readlines();
with open("site.txt","r") as curSite:
    testList = curSite.readlines()

for x in testList:
    for i in lines:
        charReplace = i.replace("\n","")
        testListReplace = x.replace("\n","")
        finalReplace = testListReplace.replace("Gxss",charReplace + "Gxss")
        #print(finalReplace)        
        
        response = requests.get("{}".format(finalReplace))
        
        for currentText in response.text.splitlines():
            if "Gxss" in currentText:
                    a =currentText.find("Gxss")
                    print(currentText[(a-30):(a+15)])
                    fileToWrite = open("output/output.txt","a")
                    fileToWrite.write("INPUT:"+charReplace+"\n")
                    fileToWrite.write(currentText[(a-30):(a+20)]+"\n")