#!/usr/bin/env python3
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys
import Games
import Questions
from Users import *
import xml.etree.ElementTree as ET
tree = ET.ElementTree('memory.xml')
tree.parse('memory.xml')
root = tree.getroot()

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

def answerQuestion(question) :
    # first check the xml file for responses
    if Questions.answerQuestionFromXML(question, user) :
       return
    # not answered, so keep going

    if matchPhrase(question, c):
        Questions.eastereggnumber()
        return

    if matchPhrase(question, f) :
      Country = Questions.live()
      Living = ET.SubElement(user, "Country")
      Living.text=str(Country)
      Living.set('id', "Country =")
      tree.write('memory.xml')
      return

    if matchPhrase(question, g) :
      Game = ET.SubElement(user, "Games")
      Game.text=str(Games)
      Game.set('id', "Games =")
      tree.write('memory.xml')
      return

    if matchPhrase(question, i) :
      Passing = Questions.passingby()
      Pass = ET.SubElement(user, "Regular")
      Pass.text=str(Passing)
      Pass.set('id', "Regular visitor? =")
      tree.write('memory.xml')
      return

    if matchPhrase(question, j) :
      Sport = Questions.sports()
      sporting = ET.SubElement(user, "Sports")
      sporting.text=str(Sport)
      sporting.set('id', "Sports =")
      tree.write('memory.xml')
      return

    if matchPhrase(question, k) :
      Food = Questions.food()
      foood = ET.SubElement(user, "Food")
      foood.text=str(Food)
      foood.set('id', "Food =")
      tree.write('memory.xml')
      return

    if matchPhrase(question, l) :
      colourst = Questions.colour()
      Colour = ET.SubElement(user, "Colour")
      Colour.text=str(colourst)
      Colour.set('id', "Colour =")
      tree.write('memory.xml')
      return

    if matchPhrase(question, m) or matchPhrase(question,['help']) :
       Questions.helpme()
       return

    if matchPhrase(question, ["no"]):
       sys.exit("Bye.")

    if matchPhrase(question, o) :
       Games.RPS()
       return

    if matchPhrase(question, p) :
       Games.ttc()
       return
    
    if matchPhrase(question, h):
        Questions.times()
        return
    
    if matchPhrase(question, a):
        Questions.dates()
        return
    
    if matchPhrase(question, n):
       Questions.family()
       return

    if matchPhrase(question, e):
       Games.quizrobotics()
       return
    Questions.unknownquestion()

Questions.loadReponses('response.xml')
User.loadUserMemory('memory.xml')

print ("Hello, my name is BOB")
name = input("What is your name?")
user = User.find(name)
if user is None :
   user = User.newUser(name)

#update name from actual user db to fix any caps problems
name = user.name

if matchPhrase(name, ['your','mom']) or \
     matchPhrase(name, ['your','mother'] or \
     matchPhrase(name, ['your','momma'])):
   question = input("Your momma who?")
   print ("I get what you mean.")
else:
   print ("Hey", name)


a = ["what","is","the","date"]
#b = "8ball"
c = "randomnumber"
#d = ["how", "old", "are", "you"]
e = ["Lets", "do","a","little","quiz"]
f = ["where", "do", "you", "live"]
g = ["what", "games", "do", "you", "play"]
h = ["how","late","is","it"]
i = ["do", "you", "come", "here", "often"]
j = ["do", "you", "play", "any", "sports"]
k = ["what", "is", "your", "favourite", "food"]
l = ["what", "is", "your", "favourite", "colour"]
m = ["help", "me", "master"]
n = ["do","you","have","family"]
o = ["lets","play","rock","paper","sissors"]
p= ["lets","play","tic","tac","toe"]

question = input("what do you want to know?, if you need help thinking of something, say: Help Me Master.")
answerQuestion(question)

for ii in range(5) :
    question = input("So, Is there anything else you want to ask?")
    answerQuestion(question)
    if question is None:
        sys.exit("Bye")

#c = ET.SubElement(user, 'c')
#d = ET.SubElement(user, 'd')
tree.write('memory.xml')
print("Okay", name)
print("Thats all you can ask.... Come back another time please....")
byebye = input("Bye.")


#How is the weather?, What time is it? When is your birthday?(make him say happy birthday on that date)

