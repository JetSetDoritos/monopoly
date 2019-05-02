
from collections import Counter
import sys

winners = {}

for i in range(0,100):
    import monopoly
    winner = monopoly.playGame()
    if winner in winners:
        winners[winner] += 1
    else:
        winners[winner] = 1
    del sys.modules['monopoly']
    

print(winners)