"""
Created on 2021-08-16 || Version 0.0.1
@author: Mahendra Prasad Gupta

Project: Rock Paper Scissors  (RPSGAME)

"""
import random

class RPSGAME:

    WELCOME = "====== Welcome To Rock Paper Scissors Game ======"
    RULE = "This iS 1 players game, minimum 5 round and maximum 25 round you can play this game."
    QUIT = "You want to QUIT this game TRUE or FALSE."
    GREETINGS = "Hello {} RPSGAME welcomes you all to our planet."
    START = "Let's start the Game."
    YOURTURN = "Hey {} please enter 1 for Rock, 2 for Paper, 3 for Scissor to continue or 0 to QUIT."
    DICE = "You select {} and computer select {}."


    # __init__(): are used to initialize the object’s state...!

    def __init__(self, players_count=2, players_name=[], players_pos=[], winners=[], decision=False):
        self.players_count = players_count
        self.players_name = players_name
        self.players_pos = players_pos
        self.winners = winners
        self.decision = decision

    def checkInput(self):
        try:
             decision = input(RPSGAME.YOURTURN.format(
                self.players_name)).upper()
        except ValueError:
            print("Please input integer only...")
            self.checkInput
        
        return decision
    
    

    def input(self):
        try:
            self.players_count = int(input("How many Rounds want to play.?"))
        except ValueError:
            print("Please input integer only...")
            self.input()

    # getInput(self): are used to take input Name and no. of player to play from the user and  work according to input and condition...!

    def getInput(self):

        self.input()

        if self.players_count > 4 and self.players_count <= 25:
        
            self.players_name.append(input(f"Enter your name.:"))
        else:
         
         return False
            

    def turns(self):
        i = 0
        while i < self.players_count:

            decision = self.checkInput()

            if decision == '0':
                self.decision = True
            if self.decision:
                self.result()
            else:
                boat = random.randrange(1, 4)
                plyer = decision
                fpos = self.move(boat, plyer)
                if fpos != True:
                    self.players_pos[i] = fpos
                i += 1
    
    def move(self, boat, plyer):

         print(RPSGAME.DICE.format(plyer,boat))

        



    def main(self):

        print(RPSGAME.WELCOME)
        print(RPSGAME.RULE)
        if self.getInput() == False:
            print(RPSGAME.RULE)
            self.decision = input(RPSGAME.QUIT).capitalize()
            if self.decision:
                self.getInput()
            else:
                self.result()
        else:
            print(RPSGAME.GREETINGS.format(self.players_name))
            print(RPSGAME.START)
            while self.decision != True:
                self.turns()
        pass
        
RPS = RPSGAME()
RPS.main()
        


