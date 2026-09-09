scores = [72, 85, 91, 68, 88]
title = "weekly score report"
name = "reyaan"

#1:
print(scores[0], scores[2], scores[-1])

#2:
scores[1]=86
print(scores)

#3:
scores.append(93)
print(scores)

#4:
weekly = title[0:6]
report = title[13:19]
print(weekly)
print(report)

#5:
label = report + ": " + str(len(scores))
print(label)

#6:
print(name + "'s " + label)
print(scores)

#7:
#lists can be changed after they are created, strings cannot be changed after they are created