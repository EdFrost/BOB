#class to store users information
import xml.etree.ElementTree as ET

class User() :
    users={}
    memoryFileName=None

    @classmethod
    def find(cls, userName) :
        #returns the user object or None if there isnt a user with that name
        return cls.users.get(userName.lower())

    @classmethod
    def loadUserMemory(cls, filename) :
        cls.memoryFileName = filename
        tree = ET.ElementTree()
        tree.parse(filename)
        root = tree.getroot()
        for item in root :
            usr = User()
            usr.load(item)
            cls.users[usr.name.lower()] = usr

    @classmethod
    def newUser(cls, userName) :
        #create a new user and update the memory file
        user = cls()
        user.name = userName
        cls.users[user.name.lower()] = user
        cls.save()
        return user

    @classmethod
    def save(cls) :
        #save memory.xml to disk
        root = ET.Element("root")
        for item in cls.users.values() :
            userElement = ET.SubElement(root, "user", id=item.name)
            for key in item.values :
                keyElement = ET.SubElement(userElement, key )
                keyElement.text = item.values[key]

        tree = ET.ElementTree(root)
        tree.write(cls.memoryFileName)

    def __init__(self) :
        self.name=''
        #use a dictionary so we can put anything w/o constantly changing this class
        self.values={}

    def load(self, xmlNode) :
        self.name = xmlNode.attrib['id']
        for valueNode in xmlNode :
            self.values[valueNode.tag] = valueNode.text

    def setAttribute(self, attr, value) :
        # add (or update) the attribute with value for this user
        self.values[attr] = value
        User.save()
