import random
matchWon = int(input("Matches won: "))
matchLost = int(input("Matches lost: "))
netList = []
gainList = []
lossList = []
netChange = 0

gain = [random.randint(200,400) for i in range(matchWon)]
loss = [random.randint(-400,-200) for i in range(matchLost)]

netChange += sum(gain)
netChange += sum(loss)

gainAvg = sum(gain) / matchWon
lossAvg = sum(loss) / matchLost

