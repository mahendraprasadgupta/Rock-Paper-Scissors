"""
Created on 2021-08-16 || Version 0.0.1
@author: Mahendra Prasad Gupta

Project: Rock Paper Scissors  (RPSGAME)

"""
import random

class RPSGAME:

    WELCOME = "====== Welcome To Rock Paper Scissors Game ======\n"
    MSG1 = "Let's play with Boat \n"
    RULE = "Minimum 5 round and maximum 25 round you can play this game.\n"
    BOAT = "\n Hey {} this is {} your playing partner.\n You want to beat me It's not possible,\n Let's see who is the winner."
    TURN = "\n Available choice.\n 1. Rock \n 2. Paper \n 3. Scissor \n 0. Quit game."
    DICE = "\n Hey {} you choose {} and {} choose {}.\n"
    QUIT = "You want to QUIT this game TRUE or FALSE."
    ITEM = ['Rock','Paper','Scissors']
    GREETINGS = "\nHello {} RPSGAME welcomes you all to our planet."
    SELECT = "\n Please Enter your choice."
    START = "\n Let's start the Game."
    ROUND = "\n     Round {} Score {} : {} and {} : {}."
    FINALS = "\n    Total  Scores  {} : {} and {} : {}."
    BYE   = "======== Thank You For Playing This Game. ========\n"

 


    # __init__(): are used to initialize the object’s state...!

    def __init__(self, round_count=0, players_name=[], score=[], decision=False):
        self.round_count = round_count
        self.players_name = players_name
        self.score = score
        self.decision = decision

    def checkInput(self):
        try:
             print(RPSGAME.TURN)
             decision = int(input(RPSGAME.SELECT))
             l = [1,2,3,0]
             if decision in l:
                return decision
             else:
               print(" Please input valid integer only...\n")
               self.checkInput()
        except ValueError:
            print(" Please input valid integer only...\n")
            self.checkInput()

        
    def result(self):
        print("\n================= SCOREBOARD ===================")
        print()
        res1=0 
        res2 =0
        for x in range(len(self.score)):
            print(RPSGAME.ROUND.format(x+1,self.players_name[0],self.score[x][self.players_name[0]],self.players_name[1],self.score[x][self.players_name[1]]))
            #res1 , res2 = 0
            res1 = res1 + (self.score[x][self.players_name[0]])
            res2 = res2 + (self.score[x][self.players_name[1]])

        print()
        print(RPSGAME.FINALS.format(self.players_name[0],res1,self.players_name[1],res2))
        print()
        print(RPSGAME.BYE)
        print()
        exit()

    

    def input(self):
        try:
            self.round_count = int(input("How many rounds you want to play.?"))
            print(self.round_count)
        except ValueError:
            print("Please input integer only...\n")
            self.input()

    # getInput(self): are used to take input Name and no. of player to play from the user and  work according to input and condition...!

    def getInput(self):

        self.input()

        if self.round_count > 4 and self.round_count <= 25:
            self.players_name.append("Dudlu")
            self.players_name.append(input(f"\nEnter your name.:"))
            print(RPSGAME.BOAT.format(self.players_name[1],self.players_name[0])) 
        else:
         
         return False
            

    def turns(self):
        i = 0
    
        while i < self.round_count:
            decision = self.checkInput()

            if decision == 0:
                self.decision = True
                if self.decision:
                   self.result()
            else:
                boat = random.randrange(1, 4)
                plyer = decision
                fpos = self.move(boat, plyer,i)    
            i += 1
    
    def move(self, boat, plyer,i):

        print(RPSGAME.DICE.format(self.players_name[0],self.ITEM[boat-1],self.players_name[1],self.ITEM[plyer-1]))

        if plyer == boat:
            print(f" Both players selected {self.ITEM[plyer-1]}. It's a tie!")
            self.score.append({self.players_name[0]:1, self.players_name[1]:1})
        elif plyer == 1:
            if boat == 3:
                print(f" Rock smashes scissors! {self.players_name[1]} win!")
                self.score.append({self.players_name[0]:0, self.players_name[1]:1})
            else:
                print(f" Paper covers rock! {self.players_name[1]} lose.")
                self.score.append({self.players_name[0]:1, self.players_name[1]:0})
        elif plyer == 2:
            if boat == 1:
                print(f" Paper covers rock! {self.players_name[1]} win!")
                self.score.append({self.players_name[0]:0, self.players_name[1]:1})
            else:
                print(f" Scissors cuts paper! {self.players_name[1]} lose.")
                self.score.append({self.players_name[0]:1, self.players_name[1]:0})
        elif plyer == 3:
            if boat == 2:
                print(f" Scissors cuts paper! {self.players_name[1]} win!")
                self.score.append({self.players_name[0]:0, self.players_name[1]:1})
            else:
                print(f" Rock smashes scissors! {self.players_name[1]} lose.")
                self.score.append({self.players_name[0]:1, self.players_name[1]:0})
        print(RPSGAME.ROUND.format(i+1,self.players_name[0],self.score[i][self.players_name[0]],self.players_name[1],self.score[i][self.players_name[1]]))

        



    def main(self):

        print(RPSGAME.WELCOME)
        print(RPSGAME.MSG1)
        print(RPSGAME.RULE)
        if self.getInput() == False:
            print(RPSGAME.RULE)
            self.decision = input(RPSGAME.QUIT).capitalize()
            if self.decision:
               self.getInput()
            else:
               self.result()
        else:
            print(RPSGAME.GREETINGS.format(self.players_name[1]))
            print(RPSGAME.START)
            if self.decision != True:
                self.turns()
            
            self.result()
            
        
        
RPS = RPSGAME()
RPS.main()
        


