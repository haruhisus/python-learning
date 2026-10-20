num, result = int(input()), 0

while num:
    result = num % 10 if num % 10 > result else result
    num = num // 10
print(result)