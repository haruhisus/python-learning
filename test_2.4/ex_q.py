count = 0
for _ in range(int(input())):
    num = int(input())
    if num % 10 == num:
        count += 1
        continue
    if num % 10 == 0:
        continue
    num_right = 0
    while num > num_right:
        num_right = num_right * 10 + num % 10
        num //= 10
    if len(str(num_right)) != len(str(num)):
        num = num * 10 + num_right % 10
    if num == num_right:
        count += 1
print(count)