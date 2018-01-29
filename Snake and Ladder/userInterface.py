import random
from tkinter import *
from Players import player
from diceMove import dice

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle

class MatchPosition():
    def __init__(self):
        self.snake = {"340,70":[100,550],
                      "580,310":[460,550],
                      "700,190":[700,430],
                      "460,190":[460,430]}

        self.ladder = {"340,550":[340,190],
                       "580,550":[580,430],
                       "220,430":[220,70],
                       "580,190":[580,70]}


    def position(self, position):
        pos = str(position[0])+","+str(position[1])
        if(pos in self.snake):
            return self.snake[pos]
        elif(pos in self.ladder):
            return self.ladder[pos]
        else:
            return position
        

##    def __str__(self):
##        for j in range(len(self.match)):
##            if self.pos == (j+1):
##                self.position_actual.append(self.match[j][0])
##                self.position_actual.append(self.match[j][1])
##
##    def actualpos(self):
##        return self.position_actual

class Display(object):
    def __init__(self,master,img,name):
        canvas_width = 850
        canvas_height = 600
        self.name = name
        print(self.name)
        #self.pos = Match_Position(self.name).actualpos()
        #print(self.pos)
        self.canvas = Canvas(master, width = canvas_width, height = canvas_height, bg = "brown")
        self.canvas.grid(padx=0, pady=0)
        self.canvas.create_image(360,300,anchor=CENTER, image = img)
        self.canvas.create_rectangle(810, 150, 760, 100, fill='white', outline='black')
        self.x = 100
        self.y = 550
        self.m = 1
        self.c = self.canvas.create_circle(self.x, self.y, 15, fill="#FFF", outline="")
        #Drop Menu
        OPTIONS = ["Players", "2", "3", "4", "5", "6"]
        variable = StringVar(master)
        variable.set(OPTIONS[0]) # default value
        w = OptionMenu(self.canvas, variable, *OPTIONS)
        w.pack()
        w.place(x=740, y=225)
        w.config(font=('calibri',(10)),bg='white',width=5)
            
        self.canvas.pack(fill=BOTH, expand=1)
        self.diceRoll = Button(self.canvas, text="Roll", background='white', command = self.diceMove, font=("Helvetica"))
        self.diceRoll.place(x=770, y=165)


    def diceMove(self):
        move = dice()
        #move = 1
        self.canvas.delete(self.c)
        self.peices(move)
        text = Label(self.canvas, text=str(move), background='white', font=("Helvetica", 25))
        text.pack()
        text.place(x=775, y=105)
        
    def peices(self, move):
        #Starting value of and x and y should be 120 and 120
        #In create_circle initial value of x and y should be 100 and 550
        #To reach to the last block x should be 5*x and y should be 4*y
        #X should be added to value and Y should be subtracted
        # 5x120=600 and 4*120=480
        
        for i in range(move,0,-1):
            self.x = self.x+120*self.m
            if(self.x>700):
                self.y = self.y - 120
                self.x = 700
                self.m = -1
            if(self.x<100):
                self.x = 100
                self.y -= 120
                self.m = 1
            if(self.y<70):
                self.y=70
        self.x,self.y = MatchPosition().position([self.x,self.y])
        if(any(self.y == ai for ai in [430,190])):
            self.m = -1
        else:
            self.m = 1
        print(self.x,self.y)
        if(self.x==700, self.y==70):
            print("Won")
            self.diceRoll(STATE=DISABLED)
        self.c = self.canvas.create_circle(self.x, self.y, 15, fill="#FFF", outline="")
        

        

        
