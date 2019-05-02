from collections import Counter
import sys
import Players

winners = {}
players = []

def startSim(p,num):
    players = p
    for i in range(0,int(num)):
        import monopoly
        winner = monopoly.playGame(players)
        if winner in winners:
            winners[winner] += 1
        else:
            winners[winner] = 1
        del sys.modules['monopoly']
    return players
        

"""
numplayers = input("Number of players: ")

for p in  range(0,int(numplayers)):
    print("1. Aggressive")
    print("2. First Half")
    print("3. Second Half")
    print("4. Random")
    choice = input("Select a strategy:")
    players.append(choice)


num = input("Number of iterations: ")

for i in range(0,int(num)):
    import monopoly
    winner = monopoly.playGame(players)
    if winner in winners:
        winners[winner] += 1
    else:
        winners[winner] = 1
    del sys.modules['monopoly']
    

print(winners) """