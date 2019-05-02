from random import randint

class Player:
    money = 200
    houses = 0
    inJail = False
    turnsInJail = 0
    position = 0

class AggressivePlayer:
    """A player that will always buy"""
    name="Aggressive"
    money = 200
    houses = 0
    inJail = False
    turnsInJail = 0
    position = 0
    
    def buy(self,x):
        return True

class RandomPlayer:
    """A player that has a random chance of buying"""
    name="Random"
    money = 200
    houses = 0
    inJail = False
    turnsInJail = 0
    position = 0
    
    def buy(self,x):
        chance = [True,False]
        return chance[randint(0,1)]

class RandomPlayer:
    """A player that has a random chance of buying"""
    name="Random"
    money = 200
    houses = 0
    inJail = False
    turnsInJail = 0
    position = 0
    
    def buy(self,x):
        chance = [True,False]
        return chance[randint(0,1)]