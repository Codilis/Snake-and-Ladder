class player:
    
    def __init__(self,name):
        self.position = 1
        self.name = name

    def setName(self,name):
        self.name = name

    def changePosition(self,number):
        self.position = self.position + number

    def setPosition(self,pos):
        self.position = pos
        return self.position

    def getPosition(self):
        return self.position

    def getName(self):
        return self.name
