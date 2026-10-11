import random
matchWon = int(input("Matches won: "))
matchLost = int(input("Matches lost: "))
gainList = []
lossList = []
netChange = 0

if matchWon >= 0 and matchLost >= 0:
    for i in range(matchWon):
        gain = random.randint(200,400)
        gainList.append(gain)
        netChange += gain

    for i in range(matchLost):
        loss = random.randint(-400,-200)
        lossList.append(loss)
        netChange += loss

    gainAvg = sum(gainList) / matchWon if matchWon > 0 else 0
    lossAvg = sum(lossList) / matchLost if matchLost > 0 else 0

    print("Average rating gained: ", gainAvg)
    print("Average rating lost: ", lossAvg)
    print("Net rating change: ", netChange)

else:
    print("Invalid input(s) (", matchWon, ",", matchLost, ")")


