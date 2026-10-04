a = int(input())
b = int(input())
repetitions = 0

while b != 0:
    temp = a % b
    a = b
    b = temp
    repetitions = repetitions + 1

print(a)
print(repetitions)
