#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys
import Games
import Questions
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
    if Questions.answerQuestionFromXML(question) :
       return
    # not answered, so keep going

    if matchPhrase(question, c):
        Questions.eastereggnumber()
        return

    if matchPhrase(question, d):
      Ages = Questions.age()
      Age = ET.SubElement(user, "Age")
      Age.text=str(Ages)
      Age.set('id', "Age =")
      tree.write('memory.xml')
      return

    if matchPhrase(question, e) :
      Feels = Questions.mood()
      Feel = ET.SubElement(user, "Mood")
      Feel.text=str(Feels)
      Feel.set('id', "mood =")
      tree.write('memory.xml')
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

    Questions.unknownquestion()


Questions.loadReponses('response.xml')


print "Hello, my name is BOB"
name = raw_input("What is your name?")
if matchPhrase(name, ['your','mom']) or \
     matchPhrase(name, ['your','mother'] or \
     matchPhrase(name, ['your','momma'])):
   question = raw_input("Your momma who?")
   print "I get what you mean."
else:
   print "Hey", name

user = ET.SubElement(root, "user")
user.set('id', name )

#a = ["what", "does", "bob", "stand", "for"]
#b = "8ball"
c = "randomnumber"
d = ["how", "old", "are", "you"]
e = ["how", "are", "you"]
f = ["where", "do", "you", "live"]
g = ["what", "games", "do", "you", "play"]
#h = ["do", "you", "have", "an", "avatar"]
i = ["do", "you", "come", "here", "often"]
j = ["do", "you", "play", "any", "sports"]
k = ["what", "is", "your", "favourite", "food"]
l = ["what", "is", "your", "favourite", "colour"]
m = ["help", "me", "master"]
#n = ["tell", "me", "a", "joke"]
o = ["lets","play","rock","paper","sissors"]
p= ["lets","play","tic","tac","toe"]

question = raw_input("what do you want to know?, if you need help thinking of something, say: Help Me Master.")
answerQuestion(question)

question = raw_input("So, Is there anything else you want to ask?")
answerQuestion(question)

question = raw_input("So, Is there anything else you want to ask?")
answerQuestion(question)

question = raw_input("So, Is there anything else you want to ask?")
answerQuestion(question)

question = raw_input("So, Is there anything else you want to ask?")
answerQuestion(question)

question = raw_input("So, Is there anything else you want to ask?")
answerQuestion(question)

#c = ET.SubElement(user, 'c')
#d = ET.SubElement(user, 'd')
tree.write('memory.xml')
print"Okay %s, thats all you can ask.... Come back another time please...." % (name)
byebye = raw_input("Bye.")


#How is the weather?, What time is it? When is your birthday?(make him say happy birthday on that date)

