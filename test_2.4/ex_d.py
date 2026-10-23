result = 0
for _ in range(int(input())):
    num = int(input())
    while num:
        result += num % 10
        num //= 10
print(result)