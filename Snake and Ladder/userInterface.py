import random
from tkinter import *
from Players import player

class Match_Position(player):
    def __init__(self,name):
        super(Match_Position,self).__init__(name)
        self.match = [[70,235],
                    [180,235],
                    [290,235],
                    [400, 235],
                    [400, 140],
                    [290, 140],
                    [180, 140],
                    [70, 140],
                    [70, 45],
                    [180, 45],
                    [290, 45],
                    [400, 45]]
        self.name = name
        self.players = player(self.name)
        self.pos = self.players.getPosition()
        self.position_actual = []
        self.__str__()
        self.actualpos()

    def __str__(self):
        for j in range(len(self.match)):
            if self.pos == (j+1):
                self.position_actual.append(self.match[j][0])
                self.position_actual.append(self.match[j][1])

    def actualpos(self):
        return self.position_actual

class Display(object):
    def __init__(self,master,img,name):
        canvas_width = 850
        canvas_height = 600
        self.name = name
        print(self.name)
        self.pos = Match_Position(self.name).actualpos()
        print(self.pos)
        self.canvas = Canvas(master, width = canvas_width, height = canvas_height, bg = "brown")
        self.canvas.grid(padx=0, pady=0)
        self.canvas.create_image(360,300,anchor=CENTER, image = img)
        self.canvas.create_rectangle(810, 150, 760, 100, fill='white', outline='black')
        self.animate(master)


    
    def animate(self,master):
        Button(master, text= "ROLL", command=self.say_hello(self.name[0])).grid( row=3, column=0, sticky=E)
        Button(master, text= "ROLL", command=self.say_hello1(self.name[1])).grid( row=3, column=1, sticky=E)

    def say_hello(self,name):
        self.name = name
        self.name = Player(self.name)
        self.name.spin()
        Check.checkLadders(self.name)
        Check.checkChutes(self.name)   
        x = self.pos[0]
        y = self.pos[1]
        self.canvas.create_oval(x,y,x+20,y+20, fill='blue')

    def say_hello1(self,name):
        self.name = name
        self.name = Player(self.name)
        self.name.spin()
        Check.checkLadders(self.name)
        Check.checkChutes(self.name)   
        x = self.pos[0]
        y = self.pos[1]
        self.canvas.create_oval(x,y,x+20,y+20, fill='red')


