from userInterface import *

class BounceController(object):
    def __init__(self):
        master = Tk()
        master.title("Snake and Ladder")
        master.geometry("850x600")
        img = PhotoImage( file = "lenna.gif")
        name = ['n','s']
        Display(master,img,name)
        master.mainloop()

def main():
    BounceController()

main()
