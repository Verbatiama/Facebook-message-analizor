
import json
import time
import math
#Read JSON data into the datastore variable
with open("ITCrowd_message.json", 'r') as f:
    datastore = json.load(f)

#Use the new datastore datastructure
def timeStamp():
    q = 0
    thisDict = {}
    thisList = []
    for a in datastore["messages"]:
        value = int(a["timestamp_ms"])
        if value in thisList:
            continue
        thisList.append(value)
        theTime  = time.gmtime(value/1000)
        temp = time.strftime('%Y-%m-%d %H:%M:%S', theTime)
        thisDict[temp[:7]] = thisDict.get(temp[:7], 0) + 1
    return thisDict

def people():
    q = 0
    thisDict = {}
    for a in datastore["messages"]:
        value = a["sender_name"]
        thisDict[value] = thisDict.get(value, 0) + 1
    return thisDict

def peopleComplex():
    q = 0
    thisDict = {}
    for a in datastore["messages"]:
        dictKey = a["sender_name"]
        bonus = 1
        try:
            value = a["content"]
            bonus = 1 + (len(value)/5)
        except:
            print("error")
        
        thisDict[dictKey] = thisDict.get(dictKey, 0) + bonus
    return thisDict

def timeOfDay():
    q = 0
    thisDict = {}
    for a in datastore["messages"]:
        value = int(a["timestamp_ms"])
        theTime  = time.gmtime(value/1000)
        temp = time.strftime('%H:%M:%S', theTime)
        thisDict[temp[:2]] = thisDict.get(temp[:2], 0) + 1
    return thisDict

def longestMessage():
    q = 0
    message = ""
    for a in datastore["messages"]:
        try:
            value = a["content"]
            if(len(value) > q):
                q = len(value)
                message = a["sender_name"] +"\n" + value
        except:
            print("error")
    return message

def moreForLeagueCount(word):
    q = 0
    for a in datastore["messages"]:

        try:
            value = a["content"]
            if(word in value):
               q = q + 1
        except:
            print("error")
    return q

def wordCounts():
    q = 0
    thisDict = {}
    for a in datastore["messages"]:
        try:
            value = a["content"]
            word = value.split(" ")
            for eachWord in word:
                thisDict[eachWord] = thisDict.get(eachWord, 0) + 1
        except:
            print("error")
    return thisDict

def oneBiggest(thisDict):
    q = 0
    word = ""
    outDict = thisDict
    for outKey in outDict.keys():
        if outDict[outKey] > q:
            word = outKey
            q = outDict[outKey]
    return word

def writeAllMessages():
    f = open("out.html", "w")
    messages = {}
    for a in datastore["messages"]:
        try:
            messages[a["timestamp_ms"]] = [a["sender_name"],a["content"]]
        except:
            1
    listed = sorted(messages)
    for out in listed:
        try:
            print("<h1>",messages[out][0],"</h1>","<p>",messages[out][1],"</p>", end='')
            print("")
        except:
            print("</p>")

writeAllMessages()


