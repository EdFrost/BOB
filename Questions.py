# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import random
fd = open('memory',"a+")
def unknownquestion():
 print "Sorry, I dont know what you mean"
 return

def questionsbob():
  print "BOB stands for Binairy Observant Bot"
  return

def eastereggball():
 ball = ["Yes", "Eh.. The answer you seek is 84", "Yes + Yes = No", "No + No = Yes", "No of course not!", "I dont think so.", "Maaaaaaaaaaaaaaaaaybe.","No.","Perhaps...","Most Definitively!","Not so sure about this one.","What? Of Course!"]
 random_item = random.choice(ball)
 print random_item
 return

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
 fd.write(Mood)
 return Mood
 
def age(  ):
 print "Im 40 years old."
 Age = raw_input("And you?")
 print "Cool!"
 fd.write(Age)
 return Age
 
def live():
 print "Im from England"
 Country = raw_input("And you?")
 print "cool"
 fd.write(Country)
 return Country
 
def games():
 print "All KeenSoftwareHouse games"
 Games = raw_input("And yours?")
 print "Those are cool too"
 fd.write(Games)
 return Games
 
def picture():
    print "No, Im a bot.... Bots dont need pictures"
    question = raw_input("You humans do need them, dont you?")
    return

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
    print "this is what you can ask: What does BOB stand for?, How old are you?, How are you?, Where do you live?, Do you have an avatar?, Do you come here often?, Do you play any sports?, What is your favourite food?, What is your favourite colour?"
    return

