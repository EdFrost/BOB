# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import random
import xml.etree.ElementTree as ET
import time
from Users import *
responses=[]

class Response() :
    # class to save/load responses
    def __init__(self) :
        self.question=''
        self.answers=[]
        self.responseText=None
        self.memoryKey=None
        self.replyText=None

    def load(self, xmlNode) :
        #load a single response from the xmlNode
        for item in xmlNode :
            if item.tag == 'question' :
               self.question = getWords(item.text)
            if item.tag == 'answers' :
               for answerNode in item :
                   self.answers.append(answerNode.text)
            if item.tag == 'responseText' :
               self.responseText=item.text
               self.memoryKey = item.attrib.get('memoryKey')
               self.replyText = item.attrib.get('replyText')

    def save(self,rootNode) :
        #add this response to the xml node
        print('save to xml')

    def questionString(self) :
        #return the question in a displayable format
        return ' '.join(self.question)

    def printAnswer(self) :
        choice = random.choice(self.answers)
        print(choice)

    def handleAnswer(self, user) :
        self.printAnswer()
        if self.responseText is None :
           return True
        answer=raw_input(self.responseText)
        if self.memoryKey is not None :
           user.setAttribute(self.memoryKey, answer)
        if self.replyText is not None :
           print(self.replyText)


def loadReponses(filename) :
    #load up all the question / response pairs from filename
    tree = ET.ElementTree()
    tree.parse(filename)
    root = tree.getroot()
    for item in root :
        resp = Response()
        resp.load(item)
        responses.append(resp)

def getWords(question) :
    # return a list of ONLY the words from question
    # remove any punctuation marks
    parts = question.split(None)
    nParts=[]
    for word in parts[:] :
        nWord = ''
        for ch in word :
            if ch.isalpha() :
               nWord = nWord+ch
        if len(nWord) > 0 :
           nParts.append(nWord.lower())
    return nParts

def matchPhrase(question, phrase) :
    #return true if the question and the phrase match
    parts = getWords(question)
    if len(parts) != len(phrase) :
       return False
    for i in range(len(parts)) :
        if parts[i] != phrase[i].lower() :
           return False
    return True

def answerQuestionFromXML(question, user) :
    # return False if there is no xml answer for this question
    # otherwise
    #    -- if the question has a followup, display that and return the response
    #    -- if the question has no followup, just return true

    for response in responses :
        if matchPhrase(question, response.question) :
           return response.handleAnswer(user)
    return False



def unknownquestion():
 print "Sorry, I dont know what you mean"
 return

# Moved to response.xml
#def questionsbob():
#  print "BOB stands for Binairy Observant Bot"
#  return

# Moved to response.xml
#def eastereggball():
# ball = ["Yes", "Eh.. The answer you seek is 84", "Yes + Yes = No", "No + No = Yes", "No of course not!", "I dont think so.", "Maaaaaaaaaaaaaaaaaybe.","No.","Perhaps...","Most Definitively!","Not so sure about this one.","What? Of Course!"]
# random_item = random.choice(ball)
# print random_item
# return

def eastereggnumber():
 max_number = 10
 print random.choice( range(1,max_number) )
 return
 
def mood():
  feel = ["Im fine.","Im okay","I feel a bit sick.","Why would you care?"]
  random_item = random.choice(feel)
  print random_item
  Mood = raw_input("And you?")
  print "okay, good for you i guess"
  
  return Mood

# moved to response.xml
#def age(  ):
# print "Im 40 years old."
#Age = raw_input("And you?")
# print "Cool!"
# return Age
 
def live():
 print "Im from England"
 Country = raw_input("And you?")
 print "cool"
 
 return Country
 
def games():
 print "All KeenSoftwareHouse games"
 gamenames = raw_input("And yours?")
 print "Those are cool too"
 
 return gamenames

# moved to response.xml
#def picture():
#    print "No, Im a bot.... Bots dont need pictures"
#    print "You humans do need them, dont you?"
#    return

def passingby():
    print "Well, every now and then"
    passing = raw_input("And you?")
    print "Well, be safe, dont talk with strangers."
    return passing

def sports():
    print "Bots dont do sports"
    sport = raw_input("And you?")
    print "Well, dont break your bones"
    return sport

def food():
    print "Sadly bots dont need food"
    foood = raw_input("And yours?")
    print "Sounds yummie"
    return foood

def colour():
    print "Black with green letters on it."
    colourst = raw_input("And yours?")
    print "Thats also a nice colour."
    return colourst

def helpme():
    print "this is what you can ask:"
    for response in responses :
        print "  "+response.questionString()+"?"

    print "  How old are you?"
    print "  How are you?"
    print "  Where do you live?"
    print "  Do you come here often?, "
    print "  Do you play any sports?, "
    print "  What is your favourite food?, "
    print "  What is your favourite colour?, "
    print "  Do you have family?,  "
    print "  How late is it?,  "
    print "  What is the date?,  "
    print "  Lets play rock paper sissors,  "
    print "  Lets play tic tac toe,  "
    return

# moved to response.xml
#def jokes():
#    goodjoke = [ ]
#    random_item = random.choice(goodjoke)
#    print random_item
#    return

def times():
    now = time.ctime()
    parse = time.strptime(now)
    print time.strftime("%H:%M:%S", parse)
    return
def dates():
    now = time.ctime()
    parse = time.strptime(now)
    print time.strftime("%a %d %b %Y", parse)
    return

def family():
    print"Well, actually, sort of..."
    print"My creator was once very active on a chat, long gone... But not forgotten."
    print"He had a friend there.... A bot. His name was Bob the Bot."
    print"They spoke for days, days turned into weeks and weeks into months."
    print"But then, the admin of the chat, Dr Vagax, announced he was going to take the chat offline."
    print"taking Bob with it.... Me creator was devastated, and thus decided to create his own BOB, a better Bob."
    print"And so he did. and now you're talking to me..."
    print"Thus you could say, my father, was Bob."
    return