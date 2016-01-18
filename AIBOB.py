#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#---  tab

#while True:
#--- userInput = input(">>> ")
#userInput = str(input(">>> "))
#------ print("Hello")
#--- else:
#------ print("I did not understand what you said")
import Questions
#import xml.etree.ElementTree as ET
#tree = ET.parse('memory.xml')
#root = tree.getroot()
fd = open('memory',"a+")

print "Hello, my name is BOB"
name = raw_input("What is your name?")
if name in ["your Mother", "your Momma","Your Mother","your momma","Your Momma","your mother"]:
 question = raw_input("Your momma who?")
 print "I get what you mean."
else:
    print "Hey %s" % (name)
fd.write(name)

question = raw_input("what do you want to know?, if you need help thinking of something, say: Help Me Master.")
#BigQuestion = question
while question :
 a = ["what does BOB stand for?" , "What does BOB stand for?", "What does bob stand for?", "what does bob stand for?", "what does BOB stand for", "What does BOB stand for", "What does bob stand for", "what does bob stand for"]
 b = "8ball"
 c = "randomnumber"
 d = ["how old are you","How old are you","How old are you?","how old are you?"]
 e = ["how are you","how are you?","How are you","How are you?"]
 f = ["where do you live","where do you live?","Where do you live?","Where do you live"]
 g = ["what games do you play","what games do you play?","What games do you play?","What games do you play"]
 h = ["do you have an avatar?","do you have an avatar","Do you have an avatar?","Do you have an avatar"]
 i = ["Do you come here often?","do you come here often?","Do you come here often","do you come here often"]
 j = ["do you play any sports?","do you play any sports","Do you play any sports?","Do you play any sports"]
 k = ["what is your favourite food?","What is your favourite food?","what is your favourite food","What is your favourite food"]
 l = ["what is your favourite colour","what is your favourite color?","What is your favourite colour?","What is your favourite colour"]
 m = ["Help Me Master","help me Master", "Help me Master"]
 if question in a:
  Questions.questionsbob()
  break
 elif question in b:
  Questions.eastereggball()
  break
 elif question in c:
  Questions.eastereggnumber()
  break
 elif question in d:
  Questions.age()
  break
 elif question in e:
  Questions.mood()
  break
 elif question in f:
  Questions.live()
  break
 elif question in g:
  Questions.games()
  break
 elif question in h:
  Questions.picture()
  break
 elif question in i:
  Questions.passingby()
  break
 elif question in j:
  Questions.sports()
  break
 elif question in k:
  Questions.food()
  break
 elif question in l:
  Questions.colour()
  break
 elif question in m:
  Questions.helpme()
  break
 else:
  Questions.unknownquestion()
  break
#if BigQuestion in Questions.questionsbob:
#    print ("hai muthafuckah")
question = raw_input("So, Is there anything else you want to ask?")
while question :
 if question in a:
  Questions.questionsbob()
  break
 elif question in b:
  Questions.eastereggball()
  break
 elif question in c:
  Questions.eastereggnumber()
  break
 elif question in d:
  Questions.age()
  break
 elif question in e:
  Questions.mood()
  break
 elif question in f:
  Questions.live()
  break
 elif question in g:
  Questions.games()
  break
 elif question in h:
  Questions.picture()
  break
 elif question in i:
  Questions.passingby()
  break
 elif question in j:
  Questions.sports()
  break
 elif question in k:
  Questions.food()
  break
 elif question in l:
  Questions.colour()
  break
 elif question in m:
  Questions.helpme()
  break
 else:
  Questions.unknownquestion()
  break
question = raw_input("So, Is there anything else you want to ask?")
while question :
 if question in a:
  Questions.questionsbob()
  break
 elif question in b:
  Questions.eastereggball()
  break
 elif question in c:
  Questions.eastereggnumber()
  break
 elif question in d:
  Questions.age()
  break
 elif question in e:
  Questions.mood()
  break
 elif question in f:
  Questions.live()
  break
 elif question in g:
  Questions.games()
  break
 elif question in h:
  Questions.picture()
  break
 elif question in i:
  Questions.passingby()
  break
 elif question in j:
  Questions.sports()
  break
 elif question in k:
  Questions.food()
  break
 elif question in l:
  Questions.colour()
  break
 elif question in m:
  Questions.helpme()
  break
 else:
  Questions.unknownquestion()
  break
  
byebye = raw_input("Okay, i have to go sadly. Bye.")
fd.close()
#print"so $s, thats all you can ask.... come back another time please...." % (name)
#wat is het weer? hoelaat is het? 
