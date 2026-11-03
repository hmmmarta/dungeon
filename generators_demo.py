def countdown(n):
    while n > 0:
        yield n
        n -= 1


numbers = countdown(3)
print(next(numbers))  # 3
print(next(numbers))  # 2
print(next(numbers))  # 1

for x in countdown(3):
    print("Round", x)