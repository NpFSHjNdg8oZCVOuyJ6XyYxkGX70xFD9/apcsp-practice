integer = int(input())
steps = 0
integerarray = []


while integer != 1:
    if integer % 2 == 0:
        integer = integer // 2
        steps = steps + 1
        integerarray.append(integer)
    else:
        integer = (integer * 3) + 1
        steps = steps + 1
        integerarray.append(integer)

print("steps: " , steps)
print(integer)
print(max(integerarray))