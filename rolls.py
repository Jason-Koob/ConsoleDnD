import random


def collectRolls():
    currentrolls = []

    currentrolls.append(random.randrange(1, 6))
    currentrolls.append(random.randrange(1, 6))
    currentrolls.append(random.randrange(1, 6))
    currentrolls.append(random.randrange(1, 6))
    sorted(currentrolls)
    currentrolls.pop(0)

    sum(currentrolls)

    return sum(currentrolls)


playerRolls = []
# Roll for stats and add them to the playerRolls array
playerRolls.append(collectRolls())
playerRolls.append(collectRolls())
playerRolls.append(collectRolls())
playerRolls.append(collectRolls())
playerRolls.append(collectRolls())
playerRolls.append(collectRolls())


playerRollsModifer = []

for rolls in playerRolls:
    playerRollsModifer.append((int(rolls) - 10)//2)

print(sorted(playerRolls))
