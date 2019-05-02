from random import randint

class Player:
    money = 1500
    houses = 0
    inJail = False
    turnsInJail = 0
    position = 0

class AggressivePlayer(Player):
    """A player that will always buy"""
    name="Aggressive"
    
    def buy(self,x):
        return True

class RandomPlayer(Player):
    """A player that has a random chance of buying"""
    name="Random"
    
    def buy(self,x):
        chance = [True,False]
        return chance[randint(0,1)]

class FirstHalfPlayer(Player):
    name = "FirstHalf"

    def buy(self,x):
        if x < 21:
            return True
        else:
            return False

class SecondHalfPlayer(Player):
    name = "SecondHalf"

    def buy(self,x):
        if x > 21:
            return True
        else:
            return False
