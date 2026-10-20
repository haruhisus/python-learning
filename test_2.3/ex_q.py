num = int(input())
result = 0
count = 1

while num:
    if num % 10 % 2 != 0:
        result = result * 10 + num % 10
        count *=10
    num //= 10
print(result)