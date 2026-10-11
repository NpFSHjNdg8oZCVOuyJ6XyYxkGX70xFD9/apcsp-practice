import random
matchWon = int(input("Matches won: "))
matchLost = int(input("Matches lost: "))
netList = []
gainList = []
lossList = []
netChange = 0

for i in range(matchWon):
    gain = random.randint(200,400)
    gainList.append(gain)
    netChange += gain

for i in range(matchLost):
    loss = random.randint(-400,-200)
    lossList.append(loss)
    netChange += loss

gainAvg = sum(gain) / matchWon
lossAvg = sum(loss) / matchLost

