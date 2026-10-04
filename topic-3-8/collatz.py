integer = int(input())
steps = 0
integerarray = [integer]


while True:

    if integer == 1:
        break
    if steps >= 1000:
        break
    if integer > 1000000:
        break 

    if integer % 2 == 0:
        integer = integer // 2
    else:
        integer = (integer * 3) + 1

    steps = steps + 1
    integerarray.append(integer)

print(integerarray)
print(steps)
print(max(integerarray))
print(integer)
      
if integer == 1:
    print("REACHED 1")
else:
    print("LIMIT REACHED")