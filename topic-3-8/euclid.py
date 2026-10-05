a = int(input())
b = int(input())
repetitions = 0


while a <= 0 or a > 1000000 or b < 0 or b > 1000000:
    a = int(input())
    b = int(input())

repititions = 0

while b != 0:
    temp = a % b
    a = b
    b = temp
    repetitions = repetitions + 1

print(a)
print(repetitions)
