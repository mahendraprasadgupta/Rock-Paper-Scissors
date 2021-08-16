"""
Created on 2021-08-16 || Version 0.0.1
@author: Mahendra Prasad Gupta

Project: Rock Paper Scissors  (RPSGAME)

"""
import random

class RPSGAME:

    WELCOME = "====== Welcome To Rock Paper Scissors ======"
    RULE = "Minimum 2 players and maximum 4 players can play this game."
    

    # __init__(): are used to initialize the object’s state...!

    def __init__(self, players_count=0, players_name=[], players_pos=[], winners=[], decision=False):
        self.players_count = players_count
        self.players_name = players_name
        self.players_pos = players_pos
        self.winners = winners
        self.decision = decision
        

    def main():

        print(RPSGAME.WELCOME)
        print(RPSGAME.RULE)
        pass
        
RPS = RPSGAME()
RPS.main()
        


