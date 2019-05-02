import json
import Players
import random

players = [Players.FirstHalfPlayer(),Players.SecondHalfPlayer()]
propertiesRaw = open("properties.json")
properties = json.load(propertiesRaw)
properties = properties["cards"]

gameActive = True
turnNumber = 0

owned = {}

houses = {}
for h in range(1,41):
    houses[h] = 0

numberOfMatches = 100

def ownedRowSpaces(p):
    """Returs an array of all the spaces where a player owns the row"""
    allProperties = []
    for o in owned:
        if owned[o] == p:
            allProperties.append(o)
    
    print("Player owns:" + str(allProperties))
    
    completeProperties = []

    if (2 in allProperties) and (4 in allProperties):
        completeProperties += [2,4]
    if (7 in allProperties) and (9 in allProperties) and (10 in allProperties):
        completeProperties += [7,9,10]
    if (12 in allProperties) and (13 in allProperties) and (15 in allProperties):
        completeProperties += [12,13,15]
    if (17 in allProperties) and (19 in allProperties) and (20 in allProperties):
        completeProperties += [17,19,20]
    if (22 in allProperties) and (24 in allProperties) and (25 in allProperties):
        completeProperties += [22,24,25]
    if (27 in allProperties) and (28 in allProperties) and (30 in allProperties):
        completeProperties += [27,28,30]
    if (32 in allProperties) and (33 in allProperties) and (35 in allProperties):
        completeProperties += [32,33,35]
    if (38 in allProperties) and (40 in allProperties):
        completeProperties += [38,40]

    return completeProperties


def playGame():
    global gameActive
    global turnNumber
    winner = ""
    while(gameActive):
        turnNumber+=1
        print(">>>Turn number " + str(turnNumber))

        for i in range(0,len(players)):
            print("Players turn:" + str(i))
            #attempt to buy houses
            


            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            player = players[i]

            potentialHouses = ownedRowSpaces(i)
            print("could buy houses on " + str(potentialHouses))
            for h in potentialHouses:
                if int(properties[str(h)]["houseCost"]) < (player.money * 0.25 ):
                    if(houses[h] < 4):
                        houses[h] = houses[h] + 1
                        player.money -= int(properties[str(h)]["houseCost"])


            
            if player.inJail:
                #case for in jail
                #roll dice
                player.turnsInJail += 1
            else:
                player.position += (dice1+dice2)

            if(player.position > 40):
                """Player has completed a loop around the board"""
                player.money += 200
                player.position -= 40

            print(player.position)

            if player.position in [1,21,31]:
                """Player had landed on a space that does nothing"""
                continue
            elif player.position in [3,18,34]:
                """Player has landed on Community"""

            elif player.position in [8,23,37]:
                """Player had landed on Chance"""

            elif player.position in [5,39]:
                """Player had landed on taxes"""
                player.money -= 75
            elif player.position in [6,16,26,36]:
                """Player had landed on railroad"""
            elif player.position in [11]:
                """Player goes to jail"""
            elif player.position in [13,29]:
                """Player has landed on utility"""
            else:
                """Player landed on a regular space"""
                if player.position in owned:
                    ammountOwed = 0
                    if houses[player.position] > 0:
                        ammountOwed = int(properties[str(player.position)][str(houses[player.position])])
                    else:
                        ammountOwed = int(properties[str(player.position)]["rent"])
                    print("player lost money " + str(ammountOwed))
                    player.money -= ammountOwed
                    players[owned[player.position]].money += ammountOwed
                elif player.buy(int(player.position)):
                    if player.money > int(properties[str(player.position)]["cost"]):
                        owned[player.position] = i
                        player.money -= int(properties[str(player.position)]["cost"])
            players[i] = player
            print("player " + str(i) + " has balance " + str(player.money))
            if player.money < 0:
                players.remove(player)
            if len(players) == 1:
                print("Winner is player" + str(players[0].name) + " after " + str(turnNumber) + " turns.") 
                winner = str(players[0].name)
                gameActive = False
                break
            if turnNumber > 1000:
                print("Stalemate, trading functionality required.")
                gameActive = False
                break
    return winner

