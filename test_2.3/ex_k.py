num, result = int(input()), int()

while num:
    result += num % 10
    num = num // 10
print(result)