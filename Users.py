#class to store users information
import xml.etree.ElementTree as ET

users=[]

class User() :
    def __init__(self) :
        self.name=''
        #use a dictionary so we can put anything w/o constantly changing this class
        self.values={}

    def load(self, xmlNode):
        print('load from xml')

def loadUserMemory(filename) :
    tree = ET.ElementTree()
    tree.parse(filename)
    root = tree.getroot()
    for item in root :
        usr = User()
        usr.load(item)
        users.append(usr)
