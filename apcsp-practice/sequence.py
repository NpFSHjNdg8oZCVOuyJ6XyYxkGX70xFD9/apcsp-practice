scores = [72, 85, 91, 68, 88]
title = "weekly score report"

#print(scores[0], scores[3], scores[4])

#scores[1]=86
#print(scores)

#scores.append(93)
#print(scores)

#print(title[0:6])
#print(title[12:19])

#new_title="new"+title[12:]
#print(new_title)

substring= title[12:19]
label=substring  + ":" +str(len(scores))
print(substring)
print(label)

#lists can be changed after they are created, strings cannot be changed after they are created