
import json
import time
import math
import random
#Read JSON data into the datastore variable
with open("ITCrowd_message.json", 'r') as f:
    datastore = json.load(f)

#Common Method logic
#"for a in datastore[x]" iterate the datastore dictonary matching x
#"thisDict" "return thisDict" output matching data as a dictionary
#"theTime  = time.gmtime(value/1000)" convert facebook timestamp into python time object
#"thisDict.get(x, 0) + 1" access the dictionary at key x and return 0 if there is no value
#"try: value = a["content"]" some messages have no content that can be processed so they must be handled

#How many messages sent per month - output dict with year/month keys and count values
def timeStamp():
    thisDict = {}
    thisList = 0
    for a in datastore["messages"]:
		#sometimes data comes in with duplicate messages, checks if last message was recieved has the same timestamp, if true ignore that message
        if value == a["timestamp_ms"]:
            continue
        value = a["timestamp_ms"]
        theTime  = time.gmtime(value/1000)
        temp = time.strftime('%Y-%m-%d %H:%M:%S', theTime)
		#store count on the year/month key
        thisDict[temp[:7]] = thisDict.get(temp[:7], 0) + 1
    return thisDict

#How many messages sent per month - output dict with name keys and count values
def people():
    q = 0
    thisDict = {}
    for a in datastore["messages"]:
        value = a["sender_name"]
		#store message count on user name
        thisDict[value] = thisDict.get(value, 0) + 1
    return thisDict

#Value of messages sent (1+ length of message / 5) - output dict with name keys and count values
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
        #store message count + bonus on user name
        thisDict[dictKey] = thisDict.get(dictKey, 0) + bonus
    return thisDict

#Messages by hour of day - output dict with hour keys and count values
def timeOfDay():
    q = 0
    thisDict = {}
    for a in datastore["messages"]:
        value = int(a["timestamp_ms"])
        theTime  = time.gmtime(value/1000)
        temp = time.strftime('%H:%M:%S', theTime)
		#store counts on hour keys
        thisDict[temp[:2]] = thisDict.get(temp[:2], 0) + 1
    return thisDict

#Find longest message - return message string
def longestMessage():
	#q is the current stored message's length
    q = 0
	#currently stored longest message and the users name
    message = ""
    for a in datastore["messages"]:
        try:
            value = a["content"]
            if(len(value) > q):
                q = len(value)
				#username + newline +message content
                message = a["sender_name"] +"\n" + value
        except:
            continue
	#return stored username and message
    return message

#Find the amount of instances of a string - args the string that should be found - return count of word
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

#Find the amount of instances of each word - return dict keys word values counts
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

#find largest string in a dictionary - return that string
def oneBiggest(thisDict):
    q = 0
    word = ""
    outDict = thisDict
    for outKey in outDict.keys():
        if outDict[outKey] > q:
            word = outKey
            q = outDict[outKey]
    return word

#output messages in a human readable format sorted in chronological order (ascending)
def writeAllMessages():
    f = open("out.html", "w")
    messages = {}
    for a in datastore["messages"]:
		#ignore messages that are missing content
        try:
            messages[a["timestamp_ms"]] = [a["sender_name"],a["content"]]
        except:
            continue
	#sort the messages
    listed = sorted(messages)
	#writ messages to html, names in <h1> tags and messages in <p> tags
    for out in listed:
        try:
            print("<h1>",messages[out][0],"</h1>","<p>",messages[out][1],"</p>", end='')
            print("")
        except:
            print("</p>")

			
def randomParticipant():
    theListofParticipants = []
    for a in datastore["participants"]:
        theListofParticipants.append(a["name"])
    print(random.choice(theListofParticipants))
#the method that will get run
randomParticipant()


