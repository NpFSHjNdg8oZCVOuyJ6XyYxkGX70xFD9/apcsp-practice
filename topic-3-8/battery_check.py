charges = [62, 28, 85, 14, 47]
amtBelow30 = 0
lowest = 100

for i in range(0, len(charges), 1):
    if charges[i] < 30:
        amtBelow30 += 1
    if charges[i] >= 80:
        print("True")
    if lowest > charges[i]:
        lowest = charges[i]

print(amtBelow30)
print(lowest)