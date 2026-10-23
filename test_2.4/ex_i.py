result = 0
for _ in range(int(input())):
    num = int(input())
    max_digit = 0
    while num:
        if (mod := num % 10) > max_digit:
            max_digit = mod
        num //= 10
    result = result * 10 + max_digit
print(result)