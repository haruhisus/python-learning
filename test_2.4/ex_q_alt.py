count = 0
for _ in range(int(input())):
    num = num_og = int(input())
    num_rev = 0
    while num:
        num_rev = num_rev * 10 + num % 10
        num //= 10
    if num_rev == num_og:
        count += 1
print(count)