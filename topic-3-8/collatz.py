integer = int(input())
steps = 0
integerarray = []


while integer != 1:
    if integer % 2 == 0:
        integer = integer // 2
    else:
        integer = (integer * 3) + 1

    steps = steps + 1
    integerarray.append(integer)

    if integer > 1000000:
        break
    if steps > 1000:
        break


print("steps: " , steps)
print(integer)
print(max(integerarray))