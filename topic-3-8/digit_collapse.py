n  = int(input())
passes = 0

while n >= 10:
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10

    n = total
    passes = passes + 1

print(n)
print(passes)
    
    