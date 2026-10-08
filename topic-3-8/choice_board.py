import random
matchWon = int(input("Matches won: "))
matchLost = int(input("Matches lost: "))
netList = []
gainList = []
lossList = []

gain = [random.randint(200,400) for i in range(matchWon)]
loss = [random.randint(-200,400) for i in range(matchLost)]

gainAvg = sum(gain) / matchWon
lossAvg = sum(loss) / matchLost

